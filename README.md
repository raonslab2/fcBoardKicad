# fcBoard - ACU5EV SoM Carrier Board

ACU5EV (Zynq UltraScale+ XCZU5EV) SoM용 캐리어 보드 KiCad 프로젝트

## 프로젝트 구조

```
fcBoardKicad/
├── fcBoard.kicad_pro          # KiCad 프로젝트 파일
├── fcBoard.kicad_sch          # 메인 회로도
├── fcBoard.kicad_pcb          # PCB 레이아웃
├── libraries/                  # 커스텀 라이브러리
│   ├── fcBoard.kicad_sym      # 심볼 라이브러리
│   └── fcBoard.pretty/        # 풋프린트 라이브러리
├── datasheets/                # 데이터시트
├── docs/                      # 설계 문서
│   └── pinmap/                # SoM 커넥터 핀맵
├── gerber/                    # 거버 출력
└── production/                # 생산 파일 (BOM, PnP)
```

## SoM 커넥터 정보

| 커넥터 | 핀 수 | 주요 신호 |
|--------|-------|----------|
| J29 | 120핀 | BANK65, BANK66 (HDMI, MIPI, Ethernet PL) |
| J30 | 120핀 | BANK25, BANK26, MGT505 (PCIe, SFP) |
| J31 | 120핀 | BANK24, BANK44 (RS485, LED, 버튼) |
| J32 | 120핀 | PS MIO, 전원 (+12V, VCCO) |

**커넥터 모델:** Panasonic AXK6A2337YG (120핀, 0.5mm 피치)

## 인터페이스 목록

### PS (Processing System) 인터페이스
- USB 3.0 x4 (USB Hub: USB5744)
- Gigabit Ethernet (PS GEM3, RGMII)
- SD Card (SDIO1)
- UART (USB-UART: CP2102)
- CAN x2
- DisplayPort (SoM 커넥터에서 직접 출력)

### PL (Programmable Logic) 인터페이스
- HDMI 입력 (IT6801FN)
- HDMI 출력 (IT66121FN)
- Gigabit Ethernet (PL RGMII)
- PCIe x2 (MGT505)
- MIPI CSI-2 (2 Lane)
- RS485 x2
- SFP+ x2 (옵션)

## 전원 요구사항

| 전원 | 전압 | 용도 |
|------|------|------|
| 입력 | DC 12V | 메인 전원 (최소 5A) |
| VCCO_65 | 1.8V | BANK65 I/O (캐리어 공급) |
| VCCO_66 | 1.8V | BANK66 I/O (캐리어 공급) |
| 내부 | 5V, 3.3V | 주변 IC 전원 |

## 참조 자료

- [ACU5EV SoM 회로도](../ACU2CG_ACU3EG_ACU4EV_ACU5EV/Schematics/ACU5EV_SCH.pdf)
- [AXU5EV-P 캐리어 보드 참조](../AXU4EV-P_AXU5EV-P/hardware/Schematics/)
- [ACU5EV 사용자 매뉴얼](../ACU2CG_ACU3EG_ACU4EV_ACU5EV/Technical_Reference_Manual/)

## 핀맵 파일

- `docs/pinmap/J29_BANK65_66.csv` - HDMI, MIPI, Ethernet PL
- `docs/pinmap/J30_BANK25_26_MGT.csv` - PCIe, SFP
- `docs/pinmap/J31_BANK24_44.csv` - RS485, GPIO
- `docs/pinmap/J32_MIO_POWER.csv` - PS MIO, 전원

## 설계 시작하기

1. KiCad 8.0 이상 설치
2. `fcBoard.kicad_pro` 열기
3. 라이브러리 경로 설정 (libraries/ 폴더)
4. 핀맵 CSV 참조하여 회로도 작성
5. PCB 레이아웃 (6층 권장)

## PCB 권장 사양

- 층수: 6층
- 두께: 1.6mm
- 임피던스: 단일 50Ω, 차동 100Ω
- 최소 선폭/간격: 0.1mm / 0.1mm
- 최소 비아: 0.3mm 드릴

## 라이선스

MIT License
