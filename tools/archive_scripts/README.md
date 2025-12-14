# Archive Scripts (Deprecated)

이 디렉토리의 스크립트는 **더 이상 공식 실행 경로로 사용되지 않습니다**.

레거시 레퍼런스 용도로만 보관됩니다.

## 정식 실행 방법

```bash
# 설정 검증
python -m kicad_auto_builder.cli validate <yaml>

# 빌드 실행
python -m kicad_auto_builder.cli build <yaml>
```

## YAML 예제

```bash
# 전원 공급 회로
python -m kicad_auto_builder.cli build kicad_auto_builder/examples/fcboard_power.yaml

# USB 인터페이스
python -m kicad_auto_builder.cli build kicad_auto_builder/examples/fcboard_usb.yaml

# 계층 시트
python -m kicad_auto_builder.cli build kicad_auto_builder/examples/hierarchical_board.yaml
```

## 레거시 스크립트 목록

### 회로도 생성 (generate_*)
| 파일 | 설명 |
|------|------|
| generate_power_sch.py | 전원 회로도 생성 |
| generate_usb_sch.py | USB 회로도 생성 |
| generate_ethernet_sch.py | Ethernet 회로도 생성 |
| generate_hdmi_sch.py | HDMI 회로도 생성 |
| generate_peripherals_sch.py | 주변장치 회로도 생성 |

### 수정/보정 (fix_*)
| 파일 | 설명 |
|------|------|
| fix_annotations.py | 어노테이션 수정 |
| fix_all_refs.py | 참조 지정자 수정 |
| fix_missing_footprints.py | 누락된 풋프린트 수정 |

### 추가 (add_*)
| 파일 | 설명 |
|------|------|
| add_3d_models.py | 3D 모델 추가 |
| add_footprints_all.py | 풋프린트 일괄 추가 |
| add_global_labels.py | 글로벌 라벨 추가 |

### 검증 (check_*, verify_*)
| 파일 | 설명 |
|------|------|
| check_3d_models.py | 3D 모델 검증 |
| verify_connections.py | 연결 검증 |

### 유틸리티
| 파일 | 설명 |
|------|------|
| gen_jlc_lib.py | JLCPCB 라이브러리 생성 |
| kicad_tools.py | KiCad 유틸리티 |
| place_components.py | 부품 배치 |

### 서브모듈 (kicad_lib/)
| 파일 | 설명 |
|------|------|
| symbols.py | 심볼 정의 |
| components.py | 컴포넌트 정의 |
| generator.py | 생성기 유틸리티 |
