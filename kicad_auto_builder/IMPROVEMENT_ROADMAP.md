# KiCad Auto Builder 개선 로드맵

## 현재 버전: v1.3.0

**최종 업데이트:** 2025-12-12

---

## 소스 구조

```
kicad_auto_builder/
├── __init__.py           # 버전 정의 (__version__ = "1.3.0")
├── cli.py                # CLI 인터페이스 (build, validate 명령)
├── config_loader.py      # YAML 설정 파서
├── part_resolver.py      # LCSC 부품 리졸버
├── kicad_builder.py      # KiCad 파일 생성 (심볼, 풋프린트, 회로도, BOM)
├── net_validator.py      # 핀-넷 매칭 검증
├── templates/
│   ├── schematic.py      # 회로도 템플릿
│   └── symbol.py         # 심볼 템플릿 (BUILTIN_SYMBOLS)
└── examples/
    ├── fcboard_power.yaml
    ├── hierarchical_board.yaml
    ├── hierarchical_board_ports_obj.yaml  # v1.3 ports 객체 예제
    └── test_resolve_fail.yaml
```

---

## v1.3.0 완료 기능

### 1. 버전 단일화 (Single Source of Truth)
- `__init__.py`의 `__version__`이 유일한 버전 소스
- CLI, manifest.json, report.md, .kicad_sch 모두 동일 버전 표시

### 2. 타이틀 블록 동적 생성
```yaml
project:
  title_block:
    rev: "2.0"              # 리비전
    company: "My Company"   # 회사명
    date: "auto"            # "auto" 또는 "YYYY-MM-DD"
    comment1: "Description"
    comment2: "Additional info"
```

### 3. Ports 확장 명세
```yaml
ports:
  # 문자열 형식 (기존 호환)
  - "+5V"
  - "GND"

  # 객체 형식 (v1.3 확장)
  - name: "DATA0"
    shape: "bidirectional"  # input/output/bidirectional/passive
    side: "right"           # left/right (시트 심볼 핀 배치)
```

### 4. validate 커맨드
```bash
python -m kicad_auto_builder.cli validate config.yaml
# 파일 생성 없이 설정/리졸브/핀-넷 검증만 수행
```

### 5. BOM 고도화
- `bom_jlc.csv`: JLCPCB용 (DNP 제외, 수량 그룹화)
- `bom_full.csv`: 상세 BOM (MPN, Manufacturer, Description, DNP, Qty)
- `report.md`: 빌드 리포트 (통계, 부품목록, DNP목록, 시트정보)

---

## 향후 개선 방향 (vNEXT)

### P0 (필수)

| 항목 | 설명 | 복잡도 |
|------|------|--------|
| **Role 매핑 확장** | 더 많은 부품 역할 지원 (op-amp, mosfet, relay 등) | 중 |
| **LCSC 캐시 고도화** | 캐시 만료/갱신 로직, 오프라인 모드 | 중 |
| **핀 위치 자동 계산** | 심볼 핀 좌표에서 라벨/와이어 위치 자동 계산 | 상 |

### P1 (권장)

| 항목 | 설명 | 복잡도 |
|------|------|--------|
| **ERC 검증** | Electrical Rule Check (전원/접지 연결 검증) | 상 |
| **심볼 자동 생성** | LCSC 데이터시트에서 핀 정보 파싱 | 상 |
| **프로젝트 템플릿** | 자주 사용하는 회로 블록 템플릿 (USB, 전원, MCU 등) | 중 |
| **다중 출력 포맷** | Altium/Eagle 변환 지원 | 상 |

### P2 (선택)

| 항목 | 설명 | 복잡도 |
|------|------|--------|
| **GUI 래퍼** | 웹/데스크톱 GUI 인터페이스 | 상 |
| **PCB 배치 힌트** | 회로도에서 PCB 배치 제약조건 주석 | 중 |
| **버전 관리 통합** | Git 커밋과 연동한 자동 리비전 | 하 |

---

## 제외 범위 (Out of Scope)

아래 기능은 현재 프로젝트 범위 외:
- PCB 레이아웃 (.kicad_pcb) 자동 생성
- 배치 최적화/오토라우팅
- DRC/LVS 검증
- Gerber 출력

---

## 사용법

### 빌드
```bash
# 단일 시트
python -m kicad_auto_builder.cli build examples/fcboard_power.yaml

# 계층 시트
python -m kicad_auto_builder.cli build examples/hierarchical_board.yaml

# Dry-run (파일 생성 없이 계획 확인)
python -m kicad_auto_builder.cli build examples/hierarchical_board.yaml --dry-run
```

### 검증
```bash
python -m kicad_auto_builder.cli validate examples/hierarchical_board.yaml
```

### 출력 파일
```
out/<project>/
├── <project>.kicad_sch     # 회로도 (단일 또는 루트)
├── <sheet>.kicad_sch       # 서브시트 (계층 모드)
├── lib/
│   ├── custom.kicad_sym    # 심볼 라이브러리
│   └── custom.pretty/      # 풋프린트 라이브러리
├── bom_jlc.csv             # JLCPCB BOM
├── bom_full.csv            # 상세 BOM
├── report.md               # 빌드 리포트
└── manifest.json           # 빌드 메타데이터
```

---

## YAML 스키마 (v1.3)

```yaml
project:
  name: "ProjectName"        # 필수
  kicad_version: 9           # 8 또는 9
  out_dir: "out/project"     # 출력 디렉토리
  title_block:               # v1.3 타이틀 블록 옵션
    rev: "1.0"
    company: "Auto Generated"
    date: "auto"
    comment1: ""
    comment2: ""

net_presets:
  VIN: "+12V"
  GND: "GND"

# 단일 시트 모드
parts:
  - ref: "R1"
    role: "resistor"
    lcsc: "C17414"
    value: "10k"
    nets:
      "1": "+5V"
      "2": "GND"
    # v1.3 BOM 필드
    mpn: "RC0402FR-0710KL"
    manufacturer: "Yageo"
    dnp: false
    description: "Pull-up resistor"

# 계층 시트 모드
sheets:
  - name: "Power"
    filename: "Power.kicad_sch"
    ports:                   # 문자열 또는 객체
      - "+5V"
      - name: "GND"
        shape: "passive"
        side: "left"
    parts:
      - ref: "U1"
        role: "buck_5v"
        ...
```

---

## 변경 이력

### v1.3.0 (2025-12-12)
- 버전 단일화 (`__version__` 기반)
- 타이틀 블록 동적 생성 (rev/company/date YAML 옵션)
- Ports 확장 명세 (shape/side 지원)
- `validate` CLI 커맨드 추가
- BOM 고도화 (MPN, manufacturer, DNP, 수량 그룹화)

### v1.2.0
- 계층 시트 지원 (sheets YAML 키)
- 루트/서브시트 자동 생성

### v1.1.0
- 핀-넷 검증 (net_validator)
- 와이어 자동 생성 (그리드 스냅, L자 라우팅)
- manifest.json 생성

### v1.0.0
- 초기 릴리스
- YAML 기반 설정
- LCSC 부품 리졸브
- 심볼/풋프린트 라이브러리 생성
- 회로도 자동 생성
