# AI 전자정부프레임워크 설계서 v1.0

## 1. 개요

### 1.1 목적

본 시스템은 전자정부프레임워크(eGovFramework)를 사용하는 공공·민간 프로젝트에서 **Controller / Service / Mapper / Mapper XML / DTO(Java)** 코드를 자동 생성하기 위한 **웹 기반 캔버스 도구**이다.

캔버스 상에서 노드를 배치하고 연결하면, 서버에서 해당 모델을 해석하여 실제 Java 소스 및 MyBatis XML을 생성하고, ZIP 파일로 다운로드할 수 있도록 한다.

### 1.2 주요 특징

- **프로젝트 단위 관리**
  - 여러 시스템/업무 도메인을 프로젝트로 관리
  - 각 프로젝트 내부에 여러 개의 캔버스(메뉴/화면/업무단위)를 생성
- **캔버스 기반 코드 설계**
  - Controller, Service, Mapper, Mapper XML, DTO 노드 배치
  - 노드 간 연결을 통해 의존 관계 및 호출 흐름 표현
- **자동 코드 생성**
  - eGov + MyBatis 패턴에 맞춘 Java 클래스 및 XML Mapper 자동 생성
  - ZIP 다운로드 기능 제공
- **확장 가능 아키텍처**
  - 추후 KiCad 회로 설계, 기타 코드 생성 엔진 등으로 확장 가능한 구조

---

## 2. 시스템 구조

### 2.1 전체 아키텍처 개요

- **프론트엔드**
  - Vue/React 등 SPA 프레임워크 기반 웹 UI
  - 주요 메뉴: 대시보드, 학습, 모델 관리, 모델 파이프라인, **AI 전자정부(프로젝트 관리, 캔버스 에디터)**
- **백엔드**
  - REST API 서버 (예: Spring Boot / NestJS 등)
  - 프로젝트/캔버스/노드 정보 관리
  - 코드 생성 엔진 호출 및 ZIP 생성
- **파일 시스템**
  - 실제 생성된 Java / XML 파일을 임시 디렉터리에 생성
  - ZIP으로 압축 후 HTTP 응답으로 전송

### 2.2 주요 모듈

1. **프로젝트 관리 모듈**
   - 프로젝트 CRUD
   - 프로젝트별 캔버스 목록 관리

2. **캔버스 에디터 모듈**
   - 노드/연결(Edge) 편집
   - 속성 패널에서 클래스명, 패키지, URL, 메소드 목록 등 설정
   - 모델을 JSON으로 직렬화하여 서버에 저장

3. **코드 생성 엔진**
   - 입력: 프로젝트 정보 + 캔버스 모델(JSON)
   - 출력: Controller, Service, Mapper, DTO, Mapper XML 파일 세트
   - 결과를 ZIP으로 압축 후 반환

4. **공통 설정/메타데이터**
   - eGov 프레임워크 스타일(Controller 어노테이션, Service 어노테이션 등)
   - MyBatis Mapper 및 XML 네이밍 규칙
   - 패키지/디렉터리 매핑 규칙

---

## 3. 화면 설계

### 3.1 좌측 메뉴 구조

- 대시보드
- 학습
- 실행/평가
- 모델 관리
- 모델 파이프라인
- **AI 전자정부**
  - **프로젝트 관리**
  - **캔버스 에디터**
- 채팅
- 설정

### 3.2 프로젝트 관리 화면

**경로:** `/ai-egov/projects`

#### 3.2.1 레이아웃

- 좌측: 프로젝트 리스트
  - 프로젝트 그룹/카테고리(예: 운영서비스, 시스템)
  - 각 그룹 내 프로젝트 카드
- 우측: 선택된 프로젝트의 상세 및 캔버스 리스트
  - 선택된 프로젝트 정보(이름, 설명, 생성일, 수정일)
  - 프로젝트에 속한 캔버스 카드(게시판, 메뉴, 권한관리 등)
  - “새 캔버스 만들기” 카드

#### 3.2.2 기능

1. **프로젝트 생성**
   - 버튼: [새 프로젝트]
   - 입력 항목:
     - 프로젝트명
     - 설명
     - Base Path (소스 생성 루트 경로)
     - Base Package (예: `kr.go.egov.example.board`)
   - 저장 시 서버 API 호출 → 프로젝트 생성

2. **프로젝트 수정/삭제**
   - 상단 우측: [수정], [삭제]
   - 수정: 기본 정보 변경 후 저장
   - 삭제: 소프트 삭제(사용여부 플래그) 또는 실제 삭제

3. **캔버스 관리**
   - 각 캔버스 카드에 표시:
     - 캔버스명 (예: 게시판, 메뉴, 권한관리)
     - 생성일
     - 노드 개수 / 연결 개수
   - 버튼:
     - [편집] → 캔버스 에디터로 이동(`/ai-egov/canvas?canvasId={id}`)
     - [삭제] → 해당 캔버스 삭제
   - “새 캔버스 만들기” 버튼 → 캔버스 생성 모달

### 3.3 캔버스 에디터 화면

**경로:** `/ai-egov/canvas?canvasId={id}`

#### 3.3.1 상단 툴바

- [노드 추가]  : 새 노드 생성 메뉴
- [불러오기]    : 저장된 캔버스 모델 로드(옵션)
- [샘플]        : 샘플 구조 자동 생성 (예: 기본 CRUD)
- [CRUD 세트]   : 엔티티명 기준으로 Controller/Service/Mapper/DTO/Mapper XML 세트 자동 생성
- [저장]        : 현재 캔버스 상태 서버 저장
- [미리보기]    : 생성될 코드 스니펫/구조 미리보기
- [ZIP]         : 코드 생성 API 호출 후 ZIP 다운로드

#### 3.3.2 캔버스 영역

- 노드 타입:
  - Controller (파란색)
  - Service (초록색)
  - Mapper (주황색)
  - Mapper XML (빨간색)
  - DTO (노란색)
- 노드 간 연결(Edge):
  - Controller → Service
  - Service → Mapper
  - Service → DTO
  - Mapper → Mapper XML

각 노드는 드래그로 위치 변경 가능, 연결점(포트)을 통한 링크 생성 가능.

#### 3.3.3 우측 속성 패널

선택된 노드의 타입에 따라 서로 다른 속성을 표시.

1. **공통 정보**
   - 클래스명
   - 패키지
2. **Controller 노드**
   - URL Prefix (예: `/api/boards`)
   - 메소드 목록
     - HTTP 메소드 (GET/POST/PUT/DELETE)
     - 메소드명 (예: `getBoardList`, `insertBoard`)
     - 경로 (예: `/`, `/{id}`)
3. **Service 노드**
   - Service 이름
   - 인터페이스/구현 분리 여부(확장용)
4. **Mapper 노드**
   - Mapper 인터페이스명
5. **Mapper XML 노드**
   - 파일명
   - 테이블명 (예: `TB_BOARD`)
6. **DTO 노드**
   - DTO 클래스명 (또는 VO)
   - 필드 목록(향후 확장): 이름, 타입, 컬럼명, 필수 여부 등

---

## 4. 백엔드 설계

### 4.1 데이터베이스 설계

#### 4.1.1 프로젝트 테이블 (예: `TB_AI_EGOV_PROJECT`)

- PROJECT_ID (PK, BIGINT)
- PROJECT_NAME (VARCHAR)
- DESCRIPTION (VARCHAR)
- BASE_PATH (VARCHAR)       : 코드 생성 루트 경로
- BASE_PACKAGE (VARCHAR)    : 기본 패키지
- CREATED_AT (DATETIME)
- UPDATED_AT (DATETIME)
- USE_YN (CHAR(1))

#### 4.1.2 캔버스 테이블 (예: `TB_AI_EGOV_CANVAS`)

- CANVAS_ID (PK, BIGINT)
- PROJECT_ID (FK)
- CANVAS_NAME (VARCHAR)
- DESCRIPTION (VARCHAR)
- NODE_COUNT (INT)
- EDGE_COUNT (INT)
- MODEL_JSON (CLOB/TEXT)    : 노드/엣지 전체 구조 JSON 직렬화
- CREATED_AT (DATETIME)
- UPDATED_AT (DATETIME)

※ 1차 버전에서는 노드/엣지를 개별 테이블로 분리하지 않고, `MODEL_JSON`으로 통합 관리.  
   추후 필요 시 `TB_AI_EGOV_NODE`, `TB_AI_EGOV_EDGE`로 분리 가능.

### 4.2 API 설계

#### 4.2.1 프로젝트 API

- `GET  /api/ai-egov/projects`
  - 프로젝트 리스트 조회
- `POST /api/ai-egov/projects`
  - 새 프로젝트 생성
- `GET  /api/ai-egov/projects/{id}`
  - 프로젝트 상세 조회
- `PUT  /api/ai-egov/projects/{id}`
  - 프로젝트 수정
- `DELETE /api/ai-egov/projects/{id}`
  - 프로젝트 삭제(Soft Delete)

#### 4.2.2 캔버스 API

- `GET  /api/ai-egov/projects/{projectId}/canvases`
  - 프로젝트 내 캔버스 리스트
- `POST /api/ai-egov/projects/{projectId}/canvases`
  - 새 캔버스 생성
- `GET  /api/ai-egov/canvases/{canvasId}`
  - 캔버스 상세(모델 JSON 포함) 조회
- `PUT  /api/ai-egov/canvases/{canvasId}`
  - 캔버스 모델 저장 (노드/엣지/속성 포함)
- `DELETE /api/ai-egov/canvases/{canvasId}`
  - 캔버스 삭제

#### 4.2.3 코드 생성 API

- `POST /api/ai-egov/canvases/{canvasId}/generate`
  - 입력:
    - 캔버스 ID (URL 경로)
    - (옵션) 엔티티명, 덮어쓰기 옵션 등
  - 처리:
    - DB에서 프로젝트/캔버스 정보 조회
    - MODEL_JSON을 파싱하여 노드/엣지/속성을 내부 도메인 모델로 변환
    - 코드 생성 엔진 호출 → 임시 디렉터리에 파일 생성
    - ZIP으로 압축 후 바이너리 스트림으로 응답
  - 출력:
    - Content-Type: `application/zip`
    - 파일명 예: `{projectName}_{canvasName}_crud.zip`

---

## 5. 코드 생성 규칙

### 5.1 디렉터리 및 패키지 매핑

- Base Path: 예) `D:/git/project/src/main/java`
- Base Package: 예) `egovframework.example.board`

| 노드 타입   | 패키지                         | 디렉터리 경로                              |
|------------|--------------------------------|-------------------------------------------|
| Controller | `{BASE_PACKAGE}.web`          | `/egovframework/example/board/web`        |
| Service    | `{BASE_PACKAGE}.service`      | `/egovframework/example/board/service`    |
| Mapper     | `{BASE_PACKAGE}.service.impl` 또는 `{BASE_PACKAGE}.mapper` | 구현 정책에 따라 선택 |
| DTO        | `{BASE_PACKAGE}.service.vo` 또는 `{BASE_PACKAGE}.dto`      | `/service/vo` 또는 `/dto`                 |
| Mapper XML | `resources/mapper/{module}`   | 예: `/resources/mapper/board`             |

※ `module`은 프로젝트명 또는 Base Package의 마지막 세그먼트를 기준으로 결정.

### 5.2 Controller 템플릿

- 어노테이션
  - `@Controller`
  - `@RequestMapping("...")`
- Service 주입
  - `@Resource(name = "xxxService")`
- 메소드 생성 규칙(샘플 CRUD 세트 기준)
  - `GET  /`        → 목록 조회
  - `GET  /{id}`    → 단건 조회
  - `POST /`        → 등록
  - `PUT  /{id}`    → 수정
  - `DELETE /{id}`  → 삭제

### 5.3 Service / Mapper / DTO / XML 템플릿

- Service
  - `xxxService` 인터페이스 또는 클래스
  - `selectXxxList`, `selectXxx`, `insertXxx`, `updateXxx`, `deleteXxx` 메소드
- Mapper
  - 동일 시그니처의 인터페이스 메소드 정의
- DTO
  - Lombok(@Data) 또는 getter/setter 방식
  - 필드명은 추후 DTO 속성 편집 기능에서 확장
- Mapper XML
  - namespace: `{BASE_PACKAGE}.service.impl.XxxMapper` 또는 `{BASE_PACKAGE}.mapper.XxxMapper`
  - `<select>`, `<insert>`, `<update>`, `<delete>` 쿼리 기본 템플릿
  - 테이블명은 속성 패널에서 입력한 값 사용(없으면 기본 규칙 적용)

---

## 6. 향후 확장 및 로드맵 (요약)

1. **DTO 필드 편집 기능**
   - 속성 패널에서 필드 추가/삭제/타입 설정
   - Mapper XML 컬럼 자동 반영

2. **공공표준용어/도메인 연계**
   - 행안부 공통표준용어 사전과 연동하여
   - DTO 필드명, DB 컬럼명, 타입 추천

3. **KiCad 회로 설계 엔진 연계(장기)**
   - 동일 캔버스 엔진을 활용하여
   - Sheet/Part/Net 기반 회로도 자동 생성

4. **템플릿 관리 기능**
   - Controller/Service/Mapper 템플릿을 프로젝트/조직 단위로 커스터마이징

---

## 7. 요약

- 본 문서는 **AI 전자정부프레임워크 – 프로젝트 관리 및 캔버스 에디터 기반 코드 자동 생성 시스템**의 설계서를 정의한다.
- 이미 구현된 웹 UI(프로젝트 관리, 캔버스 에디터)를 기준으로
  - 데이터 모델(DB)
  - API 스펙
  - 코드 생성 규칙
  을 명시했으며,
- 향후 DTO/도메인 확장 및 KiCad 등 타 도메인으로의 확장 가능성을 고려한 구조이다.
