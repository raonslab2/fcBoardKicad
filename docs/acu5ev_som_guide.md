# ALINX ACU5EV SoM 가이드

## 제품 개요

ALINX ACU5EV는 AMD/Xilinx Zynq UltraScale+ MPSoC XCZU5EV 기반 System-on-Module(SoM)입니다.

| 항목 | 사양 |
|------|------|
| FPGA | XCZU5EV-2SFVC784I |
| 크기 | 80mm × 60mm |
| PCB | 16층, 침금(Immersion Gold) |
| 전원 | +12V 단일 전원 |
| 커넥터 | 4× Panasonic AXK6A2337YG (120핀) |
| 동작 온도 | -40°C ~ +85°C |

---

## 프로세서 사양

### Processing System (PS)

| 항목 | 사양 |
|------|------|
| Application Processor | 4× ARM Cortex-A53 @ 1.333GHz |
| Real-Time Processor | 2× ARM Cortex-R5F @ 533MHz |
| GPU | ARM Mali-400 MP2 |
| Video Codec | H.264/H.265 VCU |

### Programmable Logic (PL)

| 항목 | 사양 |
|------|------|
| Logic Cells | 256K |
| CLB Flip-Flops | 234K |
| LUTs | 117K |
| UltraRAM | 18.0Mb |
| Block RAM | 11.0Mb |
| DSP Slices | 1,248 |

---

## 메모리 구성

| 메모리 | 용량 | 버스 | 속도 |
|--------|------|------|------|
| PS DDR4 | 4GB | 64-bit | 2400Mbps |
| PL DDR4 | 1GB | 16-bit | 2400Mbps |
| eMMC Flash | 8GB | - | - |
| QSPI Flash | 256Mbit (32MB) | - | - |

---

## 고속 인터페이스

### PS 측

| 인터페이스 | 사양 |
|-----------|------|
| PCIe | Gen2 ×4 |
| USB | 2× USB 3.0 |
| SATA | SATA 3.1 |
| DisplayPort | DP 1.2 |
| Ethernet | 4× Tri-mode GbE |
| PS-GTR | 4× (최대 6Gbps) |

### PL 측

| 인터페이스 | 사양 |
|-----------|------|
| GTH Transceiver | 16× (최대 16.3Gbps) |
| PCIe | Gen3 ×4 |
| HP I/O | 96개 |
| HD I/O | 84개 |

---

## 커넥터 사양

### Panasonic AXK6A2337YG

| 항목 | 사양 |
|------|------|
| 핀 수 | 120핀 (2열) |
| 피치 | 0.5mm |
| 메이팅 높이 | 3.0mm |
| 타입 | SMD, Vertical |
| 접점 | Gold plating |

**메이팅 커넥터:** AXK5A2337YG (캐리어 보드용)

---

## SoM 커넥터 배치

### 뒷면 배치도

```
                    80mm
    ┌─────────────────────────────────────┐
    │                                     │
    │   ┌─────┐              ┌─────┐     │
    │   │ J29 │              │ J30 │     │
    │   │     │              │     │     │
    │   └─────┘              └─────┘     │ 60mm
    │                                     │
    │   ┌─────┐              ┌─────┐     │
    │   │ J31 │              │ J32 │     │
    │   │     │              │     │     │
    │   └─────┘              └─────┘     │
    │                                     │
    └─────────────────────────────────────┘
```

### 커넥터 기능

| 커넥터 | Bank | 주요 기능 |
|--------|------|----------|
| J29 | BANK65/66 | HDMI I/O, MIPI, Ethernet PL |
| J30 | MGT505/BANK25/26 | PCIe ×2, SFP+ ×2 |
| J31 | BANK24/44 | RS485, GPIO, LED |
| J32 | PS MIO/Power | USB, Ethernet PS, +12V |

---

## 커넥터별 핀맵 요약

### J29 - HDMI, MIPI, Ethernet PL

| 핀 | 용도 |
|----|------|
| 1-7 | MIPI CSI-2 (CLK, D0, D1) |
| 13-50 | HDMI 입력 (24-bit + 제어) |
| 58-75 | Ethernet PL RGMII |
| 76-110 | HDMI 출력 (24-bit + 제어) |
| 111-112 | PL CLK 200MHz |

### J30 - PCIe, SFP

| 핀 | 용도 |
|----|------|
| 1-2 | PCIe RefCLK |
| 3-11 | PCIe TX/RX ×2 |
| 13-21 | SFP+ TX/RX ×2 |
| 22-23 | SFP RefCLK |
| 25-86 | Reserved |

### J31 - Peripherals

| 핀 | 용도 |
|----|------|
| 1-7 | RS485 ×2 |
| 8-9 | PL_LED ×2 |
| 10-11 | PL_KEY ×2 |
| 13 | FAN_PWM |
| 14-62 | Reserved |

### J32 - USB, Ethernet PS, Power

| 핀 | 용도 |
|----|------|
| 29-31 | I2C1 |
| 38-41 | CAN1 |
| 41-55 | Ethernet PS RGMII |
| 56-61 | SD Card |
| 63-77 | USB0 ULPI |
| 99-104 | VCCO 1.8V |
| 107-120 | +12V (14핀) |

---

## 캐리어 보드 설계

### 권장 보드 크기

- 최소: 100mm × 80mm
- 권장: 150mm × 100mm

### 커넥터 배치 좌표

보드 중심 (75mm, 50mm) 기준:

| 커넥터 | X | Y |
|--------|---|---|
| J29 | 55mm | 35mm |
| J30 | 95mm | 35mm |
| J31 | 55mm | 65mm |
| J32 | 95mm | 65mm |

### 커넥터 간격

- 수평: 40mm (J29-J30, J31-J32)
- 수직: 30mm (J29-J31, J30-J32)

---

## 전원 요구사항

| 전압 | 용도 | 공급 |
|------|------|------|
| +12V | SoM 메인 | J32 핀 107-120 |
| +1.8V | BANK65/66 VCCO | J32 핀 99-104 |

예상 전류: 2-5A (부하에 따라)

---

## 참고 자료

- [ALINX ACU5EV 공식](https://www.en.alinx.com/Product/SoC-System-on-Modules/Zynq-UltraScale-plus-MPSoC/ACU5EV.html)
- [CodeRobin ACU5EV](https://coderobin.com/products/alinx-acu5ev-xilinx-zynq-ultrascale-mpsoc-xczu5ev-fpga-som)
- [JLCPCB AXK6A2337YG](https://jlcpcb.com/partdetail/PANASONIC-AXK6A2337YG/C2843222)
- [SnapEDA Footprint](https://www.snapeda.com/parts/AXK6A2337YG/Panasonic/view-part/)
