# JLCPCB/LCSC to KiCad Library Generator

LCSC 부품 번호를 기반으로 KiCad 심볼, 풋프린트, 3D 모델을 자동 생성하는 도구입니다.

## 설치

### 1. easyeda2kicad 설치

```bash
pip install easyeda2kicad
```

### 2. 설치 확인

```bash
easyeda2kicad --help
```

## 사용법

### 1. 부품 추가

`scripts/parts_jlc.csv` 파일에 부품을 추가합니다:

```csv
lcsc_id,ref_prefix,comment,footprint_hint,notes
C25804,R,10k 0402 1%,0402,Basic resistor
C25752,R,4.7k 0402 1%,0402,Basic resistor
C11702,C,100nF 0402 X7R 16V,0402,Decoupling cap
```

| 컬럼 | 설명 | 예시 |
|------|------|------|
| `lcsc_id` | LCSC 부품 번호 (필수) | C25804 |
| `ref_prefix` | 참조 접두사 | R, C, U, Q, L |
| `comment` | 부품 설명 | 10k 0402 1% |
| `footprint_hint` | 패키지 힌트 | 0402, SOT-23-5 |
| `notes` | 메모 | Basic resistor |

### 2. 스크립트 실행

```bash
# 프로젝트 루트에서 실행
cd D:\git2\fcBoardKicad

# 전체 부품 처리
python scripts/gen_jlc_lib.py

# 특정 부품만 처리
python scripts/gen_jlc_lib.py --only C25804

# 강제 덮어쓰기
python scripts/gen_jlc_lib.py --force

# 부품 목록만 확인
python scripts/gen_jlc_lib.py --list
```

### 3. 출력 파일

```
jlc_lib_output/
├── jlc_components.kicad_sym      # 심볼 라이브러리
├── jlc_components.pretty/        # 풋프린트 라이브러리
│   └── *.kicad_mod
└── jlc_components.3dshapes/      # 3D 모델
    ├── *.step
    └── *.wrl
```

## KiCad 라이브러리 등록

### 심볼 라이브러리 등록

1. KiCad 열기
2. **Preferences → Manage Symbol Libraries** (또는 Ctrl+Shift+S)
3. **Project Specific Libraries** 탭 선택
4. **+** 버튼 클릭
5. 다음 정보 입력:
   - **Nickname**: `jlc_components`
   - **Library Path**: `${KIPRJMOD}/jlc_lib_output/jlc_components.kicad_sym`

### 풋프린트 라이브러리 등록

1. KiCad 열기
2. **Preferences → Manage Footprint Libraries** (또는 Ctrl+Shift+F)
3. **Project Specific Libraries** 탭 선택
4. **+** 버튼 클릭
5. 다음 정보 입력:
   - **Nickname**: `jlc_components`
   - **Library Path**: `${KIPRJMOD}/jlc_lib_output/jlc_components.pretty`

### 3D 모델 경로 설정

풋프린트에서 3D 모델 경로가 자동으로 설정됩니다.
필요 시 **Preferences → Configure Paths**에서 환경 변수를 추가할 수 있습니다.

## JLCPCB BOM/CPL 활용

생성된 심볼에는 `LCSC` 필드가 자동으로 추가됩니다.
BOM 생성 시 이 필드를 포함하면 JLCPCB 주문이 간편해집니다.

### BOM 생성 방법

1. KiCad Schematic Editor에서 **Tools → Generate BOM**
2. BOM 플러그인에서 `LCSC` 필드 포함
3. CSV 또는 Excel로 내보내기

### JLCPCB BOM 포맷

JLCPCB에서 요구하는 BOM 형식:

| Designator | Footprint | LCSC Part # |
|------------|-----------|-------------|
| R1,R2,R3   | 0402      | C25804      |
| C1,C2      | 0402      | C11702      |

## 문제 해결

### easyeda2kicad 설치 오류

```bash
# 가상 환경 사용 권장
python -m venv venv
venv\Scripts\activate  # Windows
pip install easyeda2kicad
```

### 부품을 찾을 수 없음

- LCSC 번호가 정확한지 확인 (예: `C25804`)
- 인터넷 연결 확인
- LCSC 웹사이트에서 부품 존재 여부 확인: https://www.lcsc.com/product-detail/C25804.html

### 심볼/풋프린트 검증

easyeda2kicad로 생성된 라이브러리는 항상 수동 검증이 필요합니다:
- 핀 번호 및 이름 확인
- 풋프린트 패드 크기 확인
- 3D 모델 방향 확인

## 참고 자료

- [easyeda2kicad GitHub](https://github.com/uPesy/easyeda2kicad.py)
- [LCSC 부품 검색](https://www.lcsc.com/)
- [JLCPCB SMT 조립](https://jlcpcb.com/smt-assembly)
