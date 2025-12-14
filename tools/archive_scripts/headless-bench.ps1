# Simple headless routing benchmark runner for Freerouting (PowerShell).
# - Builds the executable JAR (unless -SkipBuild)
# - Runs a small and a medium DSN headlessly
# - Captures runtime and logs to build/benchmarks

param(
    [switch]$SkipBuild,
    [switch]$Parallel
)

$root = Split-Path -Parent $PSScriptRoot
$jar  = Join-Path $root "build\libs\freerouting-executable.jar"
$benchDir = Join-Path $root "build\benchmarks"

if (-not $SkipBuild) {
    Write-Host "Building executable JAR..." -ForegroundColor Cyan
    & "$root\gradlew.bat" executableJar
    if ($LASTEXITCODE -ne 0) { throw "Gradle build failed ($LASTEXITCODE)" }
}

if (-not (Test-Path $jar)) {
    throw "Jar not found: $jar (build failed?)"
}

New-Item -ItemType Directory -Force -Path $benchDir | Out-Null

# Disable GUI/API and telemetry for headless runs.
$env:FREEROUTING__GUI__ENABLED = "false"
$env:FREEROUTING__API_SERVER__ENABLED = "false"
$env:FREEROUTING__USAGE_AND_DIAGNOSTIC_DATA__DISABLE_ANALYTICS = "true"

$cases = @(
    @{ name = "Issue555-small";  dsn = "tests\Issue555-BBD_Mars-64.dsn";     ses = "build\benchmarks\Issue555.ses" },
    @{ name = "Issue269-medium"; dsn = "tests\Issue269-caniot-tiny-arm.dsn"; ses = "build\benchmarks\Issue269-caniot.ses" }
)

function Invoke-BenchCase {
    param(
        [string]$Jar,
        [string]$Root,
        [string]$BenchDir,
        [string]$Name,
        [string]$DsnRel,
        [string]$SesRel
    )

    $dsnPath = Join-Path $Root $DsnRel
    if (-not (Test-Path $dsnPath)) {
        Write-Warning "Skip $Name: DSN not found at $dsnPath"
        return $null
    }
    $sesPath = Join-Path $Root $SesRel
    New-Item -ItemType Directory -Force -Path (Split-Path $sesPath -Parent) | Out-Null
    $logPath = Join-Path $BenchDir "$Name.log"

    # Ensure headless/telemetry-off inside each run (also applies to background jobs).
    $env:FREEROUTING__GUI__ENABLED = "false"
    $env:FREEROUTING__API_SERVER__ENABLED = "false"
    $env:FREEROUTING__USAGE_AND_DIAGNOSTIC_DATA__DISABLE_ANALYTICS = "true"

    Write-Host "Running $Name..." -ForegroundColor Green
    $elapsed = Measure-Command {
        & java -jar $Jar -de $dsnPath -do $sesPath -dl *>&1 | Tee-Object -FilePath $logPath
    }
    return [PSCustomObject]@{
        Name    = $Name
        Seconds = [math]::Round($elapsed.TotalSeconds, 2)
        Log     = $logPath
        Output  = $sesPath
    }
}

$results = @()

if ($Parallel) {
    $jobs = @()
    foreach ($case in $cases) {
        $jobs += Start-Job -ScriptBlock ${function:Invoke-BenchCase} -ArgumentList $jar, $root, $benchDir, $case.name, $case.dsn, $case.ses
    }
    Wait-Job $jobs | Out-Null
    foreach ($job in $jobs) {
        $res = Receive-Job $job
        if ($res) { $results += $res }
    }
    Remove-Job $jobs | Out-Null
}
else {
    foreach ($case in $cases) {
        $res = Invoke-BenchCase -Jar $jar -Root $root -BenchDir $benchDir -Name $case.name -DsnRel $case.dsn -SesRel $case.ses
        if ($res) { $results += $res }
    }
}

if ($results.Count -gt 0) {
    "`nBenchmark results:"
    $results | Format-Table -AutoSize
} else {
    Write-Warning "No benchmarks executed."
}
