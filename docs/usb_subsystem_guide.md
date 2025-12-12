# fcBoard USB 서브시스템 가이드

## 개요

fcBoard USB 서브시스템은 Zynq UltraScale+ MPSoC의 USB 3.0 포트를 4개의 외부 USB Type-A 포트로 확장합니다.

```
Zynq MPSoC USB 3.0 (PS)
         │
         ▼
    ┌─────────┐
    │ USB3320 │  ULPI PHY (U1)
    │  (U1)   │
    └────┬────┘
         │ USB 2.0 DP/DN
         ▼
    ┌─────────┐
    │ USB5744 │  4-Port USB 3.0 Hub (U2)
    │  (U2)   │
    └────┬────┘
         │
    ┌────┴────┬────────┬────────┐
    ▼         ▼        ▼        ▼
  Port1     Port2    Port3    Port4
  (J17)     (J18)    (J19)    (J20)
```

---

## 주요 IC

### U1: USB3320 - ULPI USB PHY

| 파라미터 | 값 |
|----------|-----|
| 제조사 | Microchip (SMSC) |
| 기능 | USB 2.0 ULPI PHY |
| 패키지 | QFN-32 (5x5mm) |
| 전원 | 3.3V (VDD33), 1.8V (VDD18 내부 생성) |

**역할:**
- FPGA의 ULPI 인터페이스를 USB 2.0 물리 계층으로 변환
- USB5744 허브의 업스트림 포트에 연결

**ULPI 인터페이스 핀:**
| 신호 | 방향 | 핀 | 설명 |
|------|------|-----|------|
| DATA[7:0] | Bidir | 1-8 | 8비트 양방향 데이터 버스 |
| CLK | Output | 9 | 60MHz ULPI 클럭 출력 |
| DIR | Output | 10 | 데이터 방향 제어 |
| NXT | Output | 11 | 다음 데이터 요청 |
| STP | Input | 12 | 전송 정지 신호 |
| DP | Bidir | 13 | USB D+ |
| DN | Bidir | 14 | USB D- |

**전원 핀:**
| 핀 | 이름 | 연결 |
|----|------|------|
| 16 | VDD33 | +3V3 |
| 17 | VDD18 | 내부 1.8V LDO (외부 커패시터) |
| 15 | GND | GND |

**Zynq 연결 (ULPI):**
```
USB3320          Zynq UltraScale+
────────         ────────────────
DATA0   ◄──────► MIO52 (ULPI_D0)
DATA1   ◄──────► MIO53 (ULPI_D1)
DATA2   ◄──────► MIO54 (ULPI_D2)
DATA3   ◄──────► MIO55 (ULPI_D3)
DATA4   ◄──────► MIO56 (ULPI_D4)
DATA5   ◄──────► MIO57 (ULPI_D5)
DATA6   ◄──────► MIO58 (ULPI_D6)
DATA7   ◄──────► MIO59 (ULPI_D7)
CLK     ───────► MIO60 (ULPI_CLK)
DIR     ───────► MIO61 (ULPI_DIR)
NXT     ───────► MIO62 (ULPI_NXT)
STP     ◄─────── MIO63 (ULPI_STP)
```

---

### U2: USB5744 - 4-Port USB 3.0 Hub

| 파라미터 | 값 |
|----------|-----|
| 제조사 | Microchip |
| 기능 | 4-Port USB 3.0 Super-Speed Hub |
| 패키지 | QFN-48 (7x7mm) |
| 전원 | 5V (VDD5), 3.3V (VDD33), 1.2V (내부 생성) |

**역할:**
- USB 2.0 업스트림을 4개의 USB 2.0 다운스트림으로 분배
- USB 3.0 Super-Speed 지원 (5Gbps)
- 각 포트별 전류 제한 지원

**업스트림 포트 (USB3320에서):**
| 신호 | 핀 | 설명 |
|------|-----|------|
| UP_DP | - | USB 2.0 D+ (USB3320 DP) |
| UP_DN | - | USB 2.0 D- (USB3320 DN) |

**다운스트림 포트 핀:**
| 포트 | D+ 핀 | D- 핀 | 연결 |
|------|-------|-------|------|
| DN1 | 13 | 14 | J17 (USB Port 1) |
| DN2 | 15 | 16 | J18 (USB Port 2) |
| DN3 | 17 | 18 | J19 (USB Port 3) |
| DN4 | 19 | 20 | J20 (USB Port 4) |

**ULPI 인터페이스 (업스트림):**
| 신호 | 핀 | 연결 |
|------|-----|------|
| CLK | 1 | USB3320.CLK |
| DIR | 2 | USB3320.DIR |
| NXT | 3 | USB3320.NXT |
| STP | 4 | USB3320.STP |
| DATA[0:7] | 5-12 | USB3320.DATA[0:7] |

**전원 핀:**
| 핀 | 이름 | 연결 | 설명 |
|----|------|------|------|
| 22 | VDD33 | +3V3 | 3.3V 디지털 전원 |
| 23 | VDD12 | 내부 LDO | 1.2V 코어 (외부 커패시터) |
| - | VDD5 | +5V | 5V 입력 (VBUS 생성용) |
| 21 | GND | GND | 접지 |

---

## USB 커넥터

### J17, J18, J19, J20: USB Type-A 커넥터

| 파라미터 | 값 |
|----------|-----|
| 타입 | USB Type-A Female |
| 풋프린트 | Stewart SS-52100-001 Horizontal |

**핀 배치:**
| 핀 | 이름 | 연결 |
|----|------|------|
| 1 | VBUS | TPS2041B 출력 (+5V 스위치) |
| 2 | D- | USB5744 DNx_DN (ESD 보호 후) |
| 3 | D+ | USB5744 DNx_DP (ESD 보호 후) |
| 4 | GND | GND |
| Shell | Shield | GND (페라이트 비드 통해) |

---

## 전원 스위치

### U7, U8, U9, U10: TPS2041B - USB 전원 스위치

| 파라미터 | 값 |
|----------|-----|
| 제조사 | Texas Instruments |
| 기능 | 단일 채널 전류 제한 전원 스위치 |
| 패키지 | SOT-23-5 |
| 전류 제한 | 500mA (내부 설정) |

**역할:**
- 각 USB 포트에 VBUS (+5V) 공급
- 과전류 보호 (500mA 제한)
- 소프트 스타트 (돌입 전류 제한)
- 폴트 표시 출력

**핀 연결:**
| 핀 | 이름 | 연결 | 설명 |
|----|------|------|------|
| 1 | VIN | +5V | 5V 전원 입력 |
| 2 | VOUT | USB VBUS | 스위치 출력 |
| 3 | EN | 제어 신호/+3V3 | 활성화 (Active Low) |
| 4 | FAULT | 폴트 표시 | 과전류 시 Low 출력 |
| 5 | GND | GND | 접지 |

**포트별 할당:**
| IC | USB 포트 | EN 제어 |
|----|----------|---------|
| U7 | J17 (Port 1) | 상시 ON 또는 GPIO |
| U8 | J18 (Port 2) | 상시 ON 또는 GPIO |
| U9 | J19 (Port 3) | 상시 ON 또는 GPIO |
| U10 | J20 (Port 4) | 상시 ON 또는 GPIO |

---

## ESD 보호

### U3, U4, U5, U6: TPD4S012 - USB ESD 보호

| 파라미터 | 값 |
|----------|-----|
| 제조사 | Texas Instruments |
| 기능 | 4채널 USB ESD 보호 |
| 패키지 | UQFN-10 (1.4x1.8mm) |
| ESD 내성 | ±8kV (접촉), ±15kV (공기) |

**역할:**
- USB 데이터 라인 (D+/D-) ESD 보호
- 낮은 기생 커패시턴스 (USB 2.0 High-Speed 호환)
- IEC 61000-4-2 레벨 4 준수

**핀 연결:**
| 핀 | 이름 | 연결 |
|----|------|------|
| 1 | D+ | USB5744 DNx_DP |
| 2 | D- | USB5744 DNx_DN |
| 3 | D+_OUT | USB 커넥터 D+ |
| 4 | D-_OUT | USB 커넥터 D- |
| 5 | GND | GND |
| 6 | VCC | +3V3 |

**포트별 할당:**
| IC | USB 포트 | 보호 대상 |
|----|----------|----------|
| U3 | J17 (Port 1) | DN1_DP, DN1_DN |
| U4 | J18 (Port 2) | DN2_DP, DN2_DN |
| U5 | J19 (Port 3) | DN3_DP, DN3_DN |
| U6 | J20 (Port 4) | DN4_DP, DN4_DN |

---

## 신호 연결도

### USB3320 ↔ USB5744 연결

```
USB3320 (U1)              USB5744 (U2)
─────────────             ───────────
CLK (9)      ──────────►  CLK (1)
DIR (10)     ──────────►  DIR (2)
NXT (11)     ──────────►  NXT (3)
STP (12)     ◄──────────  STP (4)
DATA0 (1)    ◄─────────►  DATA0 (5)
DATA1 (2)    ◄─────────►  DATA1 (6)
DATA2 (3)    ◄─────────►  DATA2 (7)
DATA3 (4)    ◄─────────►  DATA3 (8)
DATA4 (5)    ◄─────────►  DATA4 (9)
DATA5 (6)    ◄─────────►  DATA5 (10)
DATA6 (7)    ◄─────────►  DATA6 (11)
DATA7 (8)    ◄─────────►  DATA7 (12)
DP (13)      ◄─────────►  UP_DP
DN (14)      ◄─────────►  UP_DN
```

### USB5744 → USB 포트 연결

```
USB5744 (U2)    ESD (U3-U6)    Power (U7-U10)    Connector
────────────    ───────────    ──────────────    ─────────
DN1_DP (13) ──► TPD4S012 ──────────────────────► J17.D+ (3)
DN1_DN (14) ──► (U3)     ──────────────────────► J17.D- (2)
                              TPS2041B (U7) ───► J17.VBUS (1)

DN2_DP (15) ──► TPD4S012 ──────────────────────► J18.D+ (3)
DN2_DN (16) ──► (U4)     ──────────────────────► J18.D- (2)
                              TPS2041B (U8) ───► J18.VBUS (1)

DN3_DP (17) ──► TPD4S012 ──────────────────────► J19.D+ (3)
DN3_DN (18) ──► (U5)     ──────────────────────► J19.D- (2)
                              TPS2041B (U9) ───► J19.VBUS (1)

DN4_DP (19) ──► TPD4S012 ──────────────────────► J20.D+ (3)
DN4_DN (20) ──► (U6)     ──────────────────────► J20.D- (2)
                              TPS2041B (U10) ──► J20.VBUS (1)
```

---

## 전원 공급

### 전압 레일

| 전압 | 사용처 | 공급원 |
|------|--------|--------|
| +5V | TPS2041B VIN, USB VBUS | fcBoard_Power |
| +3V3 | USB3320, USB5744, TPD4S012 | fcBoard_Power |
| +1V8 | USB3320 내부 | 내부 LDO |
| +1V2 | USB5744 코어 | 내부 LDO |

### 전원 심볼 사용

| IC | 전원 핀 | 파워 심볼 |
|----|---------|----------|
| U1 (USB3320) | VDD33 | +3V3 |
| U2 (USB5744) | VDD33 | +3V3 |
| U2 (USB5744) | VDD5 | +5V |
| U3-U6 (TPD4S012) | VCC | +3V3 |
| U7-U10 (TPS2041B) | VIN | +5V |
| All | GND | GND |

---

## 바이패스 커패시터

각 IC에 적절한 바이패스 커패시터가 필요합니다:

| IC | 전원 | 권장 커패시터 |
|----|------|--------------|
| USB3320 | VDD33 | 100nF + 10µF |
| USB3320 | VDD18 | 1µF (LDO 출력) |
| USB5744 | VDD33 | 100nF + 10µF |
| USB5744 | VDD12 | 4.7µF (LDO 출력) |
| USB5744 | VDD5 | 100nF + 10µF |
| TPD4S012 | VCC | 100nF |
| TPS2041B | VIN | 100nF |

---

## PCB 레이아웃 가이드라인

### USB 2.0 차동 쌍

| 파라미터 | 권장값 |
|----------|--------|
| 임피던스 | 90Ω (차동) |
| 트레이스 폭 | 0.15mm (4층 기준) |
| 간격 | 0.15mm |
| 길이 매칭 | ±2.5mm 이내 |

### 배치 권장사항

1. **USB3320**: Zynq에 가깝게 배치 (ULPI 신호 길이 최소화)
2. **USB5744**: USB3320 근처에 배치
3. **TPD4S012**: 각 USB 커넥터에 최대한 가깝게
4. **TPS2041B**: 각 USB 커넥터에 가깝게
5. **크리스털**: USB3320 근처, GND 플레인 위

### GND 처리

- USB 커넥터 쉴드는 페라이트 비드를 통해 GND 연결
- 디지털 GND와 USB GND 분리 고려
- Star 접지 또는 단일 포인트 연결

---

## 소프트웨어 설정

### Zynq USB 컨트롤러

PetaLinux/Vivado에서 USB 컨트롤러 설정:

```
# Device Tree 예시
&usb0 {
    status = "okay";
    dr_mode = "host";
    phy-names = "usb3-phy";
    phys = <&lane2 PHY_TYPE_USB3 0 2 26000000>;
};
```

### USB3320 초기화

USB3320은 하드웨어 스트랩으로 자동 설정됩니다:
- REFCLK: 외부 26MHz 또는 내부 오실레이터
- 모드: ULPI

---

## 트러블슈팅

### USB 장치 인식 안 됨

1. VBUS 전압 확인 (4.75V ~ 5.25V)
2. TPS2041B EN 핀 상태 확인
3. TPS2041B FAULT 출력 확인
4. USB3320 CLK 출력 확인 (60MHz)

### 열거 실패

1. ULPI 신호 연결 확인
2. USB3320 전원 (3.3V) 확인
3. 바이패스 커패시터 확인
4. D+/D- 임피던스 확인

### 간헐적 연결 끊김

1. VBUS 전류 확인 (과전류?)
2. ESD 보호 IC 확인
3. 커넥터 접촉 상태 확인
4. EMI/노이즈 확인

### 전류 제한 동작

TPS2041B는 500mA에서 전류 제한:
- FAULT 핀이 Low로 변경
- 출력 전압 감소
- 열 차단 가능

---

## 부품 리스트

| Reference | Part | Value/Type | Footprint |
|-----------|------|------------|-----------|
| U1 | USB3320 | ULPI PHY | QFN-32 (5x5mm) |
| U2 | USB5744 | USB 3.0 Hub | QFN-48 (7x7mm) |
| U3-U6 | TPD4S012 | ESD Protection | UQFN-10 |
| U7-U10 | TPS2041B | Power Switch | SOT-23-5 |
| J17-J20 | USB_A | Type-A Female | SS-52100-001 |
| C_bypass | Capacitor | 100nF | 0402 |
| C_bulk | Capacitor | 10µF | 0603 |
| FB | Ferrite Bead | 600Ω@100MHz | 0402 |

---

## 참고 자료

- [USB3320 데이터시트](https://ww1.microchip.com/downloads/en/DeviceDoc/00001792E.pdf)
- [USB5744 데이터시트](https://ww1.microchip.com/downloads/en/DeviceDoc/USB5744-Data-Sheet-DS00001855D.pdf)
- [TPS2041B 데이터시트](https://www.ti.com/lit/ds/symlink/tps2041b.pdf)
- [TPD4S012 데이터시트](https://www.ti.com/lit/ds/symlink/tpd4s012.pdf)
- KiCad 프로젝트: `fcBoard_USB.kicad_sch`
