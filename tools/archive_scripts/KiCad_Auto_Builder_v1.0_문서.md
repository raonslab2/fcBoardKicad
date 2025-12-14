# KiCad Auto Builder v1.0 사용 및 설계 문서

## 1. 개요

**KiCad Auto Builder v1.0**은 YAML 설정 파일 한 장으로 KiCad 회로도(.kicad_sch)와 심볼 라이브러리(.kicad_sym), 그리고 JLCPCB BOM(.csv)을 자동 생성하는 CLI 도구입니다.

- 목표
  - 부품 선택 → 심볼/풋프린트 수집 → 회로도 생성 → BOM 출력까지를 자동화
  - LCSC 부품 번호 및 내부 역할(role) 기반으로 회로를 빠르게 프로토타이핑

---

## 2. 설치 및 실행 환경

### 2.1 필수 환경

- Python 3.10 이상
- KiCad 8.x 포맷을 이해하는 사용자 (툴 자체는 KiCad 설치 없이도 동작 가능)
- OS: Windows / macOS / Linux

### 2.2 권장 도구

- `easyeda2kicad`
  - LCSC/LCSC 기반 EasyEDA 라이브러리에서 심볼/풋프린트 추출에 사용
  - 설치되어 있으면 KiCad Auto Builder가 자동으로 호출하여 심볼/풋프린트를 다운로드

---

## 3. 기본 사용법

### 3.1 기본 빌드

```bash
python -m kicad_auto_builder.cli build kicad_auto_builder/examples/power_board.yaml
```

### 3.2 Dry-run (실제 파일 생성 없이 확인)

```bash
python -m kicad_auto_builder.cli build power_board.yaml --dry-run
```

- YAML을 파싱하고, 부품/넷/역할 매핑 결과만 터미널 로그로 출력
- 실제 파일(`.kicad_sch`, `.kicad_sym`, `.csv`)은 생성하지 않음

### 3.3 출력 디렉터리 지정

```bash
python -m kicad_auto_builder.cli build power_board.yaml -o output/my_project
```

- 기본 `out/` 대신 지정한 디렉터리에 결과 파일 생성

---

## 4. 생성 결과 구조

기본 예시(`power_board.yaml`) 기준 디렉터리 구조는 다음과 같습니다.

```text
out/power_board/
├── lib/
│   └── custom.kicad_sym          # 자동 생성 심볼 라이브러리
├── PowerBoard_5V_3V3.kicad_sch   # 자동 생성 회로도
└── bom_jlc.csv                   # JLCPCB BOM CSV
```

- `lib/custom.kicad_sym`
  - LCSC/easyeda2kicad 및 내부 라이브러리에서 수집한 심볼을 통합한 라이브러리
- `PowerBoard_5V_3V3.kicad_sch`
  - YAML 설정을 기반으로 자동 배치된 회로도
- `bom_jlc.csv`
  - JLCPCB 업로드를 고려한 기본 BOM 포맷 (Comment, Designator, Footprint, LCSC Part# 등)

---

## 5. YAML 설정 파일 구조

기본 구조는 다음과 같습니다.

```yaml
project:
  name: "ProjectName"
  kicad_version: 8
  out_dir: "out/project"

net_presets:
  VIN: "VIN"
  V5: "+5V"
  GND: "GND"

parts:
  - ref: "U1"
    role: "buck_5v"           # 내부 역할 매핑 사용
    lcsc: "C12345"            # LCSC 부품번호
    value: "LM2596"
    nets:
      VIN: "VIN"
      VOUT: "+5V"
      GND: "GND"
```

### 5.1 `project` 섹션

- `name` : 프로젝트/회로도 이름 (예: `PowerBoard_5V_3V3`)
- `kicad_version` : 타깃 KiCad 포맷 버전 (현재 8 기준)
- `out_dir` : 출력 디렉터리 루트 경로

### 5.2 `net_presets` 섹션

자주 사용하는 넷 이름을 미리 정의하는 영역입니다.

- 키: 논리 키 (도구 내부에서 사용)
- 값: 실제 회로도에 표시될 넷 라벨

예:

```yaml
net_presets:
  VIN: "VIN"
  V5: "+5V"
  GND: "GND"
```

- 이후 `parts[].nets`에서 `VIN`, `VOUT`, `GND` 등으로 참조합니다.

### 5.3 `parts` 섹션

각 부품(Part)을 정의하는 리스트입니다.

#### 필드 설명

- `ref`
  - 회로도 상의 레퍼런스 (예: U1, R3, C10)
- `role`
  - 내부 역할 기반 템플릿 이름
  - 예: `buck_5v`, `resistor`, `capacitor`, `led` 등
  - 역할에 따라 기본 심볼/풋프린트/핀 구조를 매핑
- `lcsc`
  - LCSC 부품 번호 (예: `C12345`)
  - `easyeda2kicad`가 설치되어 있으면 해당 부품의 심볼/풋프린트를 자동 다운로드 후 사용
- `value`
  - 회로도에 표시될 값 (예: `LM2596`, `10k`, `100nF`)
- `nets`
  - 부품의 핀과 넷을 매핑하는 객체
  - 키: 핀 또는 역할명 (예: VIN, VOUT, GND)
  - 값: 실제 넷 이름(보통 `net_presets`에 정의된 값을 사용)

예:

```yaml
parts:
  - ref: "U1"
    role: "buck_5v"
    lcsc: "C12345"
    value: "LM2596"
    nets:
      VIN: "VIN"
      VOUT: "+5V"
      GND: "GND"
```

---

## 6. 지원 기능 요약

1. **내부 역할 매핑**
   - `buck_5v`, `resistor`, `capacitor`, `led` 등 역할 기반으로
   - 기본 심볼/풋프린트/핀 구조를 자동으로 선택

2. **LCSC 연동 (easyeda2kicad 사용)**
   - `lcsc` 필드를 통해 LCSC 번호를 지정하면
   - `easyeda2kicad` CLI를 호출하여 심볼/풋프린트 파일을 다운로드
   - 캐시 디렉터리를 사용하여 동일 부품의 중복 호출 최소화

3. **자동 배치**
   - 부품을 단순한 그리드 규칙으로 자동 배치
   - X/Y 좌표를 행/열 단위로 자동 계산하여 회로도에 배치

4. **JLCPCB BOM 생성**
   - `bom_jlc.csv` 파일 생성
   - 각 파트의 `ref`, `value`, `footprint`, `lcsc` 정보를 포함
   - JLCPCB 업로드용 기본 템플릿에 맞춘 컬럼 구성

---

## 7. 아키텍처 개요

KiCad Auto Builder는 크게 다음 3개 모듈로 구성됩니다.

1. **config_loader**
   - YAML 파일을 파싱하여 내부 도메인 모델(`ProjectConfig`, `PartSpec` 등)로 변환

2. **part_resolver**
   - `role`, `lcsc` 값을 기반으로
     - 내부 매핑
     - LCSC/easyeda2kicad 호출
   - 결과로 `ResolvedPart`(심볼 이름, footprint, 메타데이터)를 반환

3. **kicad_builder**
   - 모든 `ResolvedPart`를 입력으로 받아
     - `custom.kicad_sym` 심볼 라이브러리 생성
     - `.kicad_sch` 회로도 파일 생성
     - `bom_jlc.csv` BOM 파일 생성

CLI는 이 세 모듈을 순차적으로 호출하는 얇은 래퍼 역할을 합니다.

---

## 8. 향후 확장 아이디어

- **다중 시트 지원**
  - `sheets:` 섹션을 도입하여 시트별 부품 정의 및 별도 `.kicad_sch` 생성
- **회로 블록 템플릿**
  - `buck_5v`처럼 하나의 역할이 여러 부품(R/L/C 포함)을 자동 배치하도록 확장
- **웹 UI 연동**
  - YAML 대신 웹 폼/캔버스에서 부품을 입력 후
  - 서버에서 KiCad Auto Builder를 호출해 결과 ZIP 제공
- **PCB 자동 라우팅 연계**
  - 추후 PCBNew/FreeRouting 등과 연계하는 별도 모듈 추가

---

## 9. 요약

- KiCad Auto Builder v1.0은 **YAML 파일 하나로 회로도 + 심볼 라이브러리 + JLC BOM**을 자동 생성하는 도구입니다.
- 내부 역할(role)과 LCSC 연동을 통해
  - 반복적인 전원보드/공통모듈 설계를 빠르게 자동화할 수 있습니다.
- 현재 버전은 단일 시트와 단순 배치에 초점을 맞추고 있으며,
  - 향후 다중 시트, 블록 템플릿, 웹 UI 연동 등으로 확장 가능하도록 설계되었습니다.
