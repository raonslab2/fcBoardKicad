"""
KiCad Auto Builder - 커스텀 예외 클래스

에러 유형별 예외를 정의하여 명확한 에러 처리와 친절한 메시지를 제공합니다.
"""


class KicadAutoBuilderError(Exception):
    """kicad_auto_builder의 기본 예외 클래스."""

    def __init__(self, message: str, error_code: str = None, hint: str = None):
        """초기화.

        Args:
            message: 에러 메시지
            error_code: 에러 코드 (예: "LCSC_NOT_FOUND")
            hint: 해결 방법 힌트
        """
        self.message = message
        self.error_code = error_code
        self.hint = hint
        super().__init__(self._format_message())

    def _format_message(self) -> str:
        """포맷된 에러 메시지 생성."""
        parts = [self.message]
        if self.error_code:
            parts.insert(0, f"[{self.error_code}]")
        if self.hint:
            parts.append(f"\n힌트: {self.hint}")
        return " ".join(parts)


class ConfigError(KicadAutoBuilderError):
    """설정 파일 관련 에러."""
    pass


class ConfigValidationError(ConfigError):
    """YAML 스키마 검증 에러."""

    def __init__(self, message: str, field: str = None, value=None, hint: str = None):
        """초기화.

        Args:
            message: 에러 메시지
            field: 문제가 있는 필드 경로 (예: "parts[0].ref")
            value: 현재 값
            hint: 해결 방법
        """
        self.field = field
        self.value = value

        full_message = message
        if field:
            full_message += f"\n  위치: {field}"
        if value is not None:
            full_message += f"\n  현재 값: {value}"

        super().__init__(full_message, error_code="CONFIG_VALIDATION", hint=hint)


class PartResolveError(KicadAutoBuilderError):
    """부품 리졸브 관련 에러."""

    def __init__(self, message: str, ref: str = None, role: str = None, **kwargs):
        """초기화.

        Args:
            message: 에러 메시지
            ref: 부품 레퍼런스 (예: "U1")
            role: 부품 역할
        """
        self.ref = ref
        self.role = role

        if ref or role:
            message += f" (ref={ref}, role={role})"

        super().__init__(message, **kwargs)


class EasyEDAError(PartResolveError):
    """easyeda2kicad 관련 에러."""

    ERROR_HINTS = {
        "LCSC_NOT_FOUND": "LCSC 부품번호가 올바른지 확인하세요 (예: C12345)",
        "RATE_LIMITED": "잠시 후 다시 시도하세요 (API 호출 제한)",
        "NETWORK_ERROR": "인터넷 연결을 확인하세요",
        "TIMEOUT": "네트워크가 느리거나 서버가 응답하지 않습니다",
        "NOT_INSTALLED": "easyeda2kicad가 설치되어 있는지 확인하세요: pip install easyeda2kicad",
        "PARSE_ERROR": "다운로드된 파일이 손상되었을 수 있습니다. 캐시를 삭제하고 재시도하세요",
    }

    def __init__(self, message: str, lcsc_id: str = None, error_code: str = None, **kwargs):
        """초기화.

        Args:
            message: 에러 메시지
            lcsc_id: LCSC 부품번호
            error_code: 에러 코드
        """
        self.lcsc_id = lcsc_id

        if lcsc_id:
            message = f"LCSC {lcsc_id}: {message}"

        # 자동 힌트 추가
        hint = kwargs.pop("hint", None) or self.ERROR_HINTS.get(error_code)

        super().__init__(message, error_code=error_code, hint=hint, **kwargs)


class NetworkError(EasyEDAError):
    """네트워크 연결 에러."""
    pass


class CacheError(KicadAutoBuilderError):
    """캐시 손상 또는 접근 에러."""

    def __init__(self, message: str, cache_path: str = None, **kwargs):
        """초기화.

        Args:
            message: 에러 메시지
            cache_path: 캐시 경로
        """
        self.cache_path = cache_path

        if cache_path:
            message += f"\n  캐시 경로: {cache_path}"

        hint = kwargs.pop("hint", None) or "캐시 디렉토리를 삭제하고 재시도하세요"
        super().__init__(message, error_code="CACHE_ERROR", hint=hint, **kwargs)


class SymbolParseError(KicadAutoBuilderError):
    """심볼 파일 파싱 에러."""

    def __init__(self, message: str, file_path: str = None, **kwargs):
        """초기화.

        Args:
            message: 에러 메시지
            file_path: 심볼 파일 경로
        """
        self.file_path = file_path

        if file_path:
            message += f"\n  파일: {file_path}"

        super().__init__(message, error_code="SYMBOL_PARSE", **kwargs)


class NetValidationError(KicadAutoBuilderError):
    """핀-넷 검증 에러."""

    def __init__(self, message: str, ref: str = None, pin: str = None, **kwargs):
        """초기화.

        Args:
            message: 에러 메시지
            ref: 부품 레퍼런스
            pin: 핀 이름
        """
        self.ref = ref
        self.pin = pin

        if ref or pin:
            message += f" (ref={ref}, pin={pin})"

        super().__init__(message, error_code="NET_VALIDATION", **kwargs)


class BuildError(KicadAutoBuilderError):
    """빌드 프로세스 에러."""

    def __init__(self, message: str, stage: str = None, **kwargs):
        """초기화.

        Args:
            message: 에러 메시지
            stage: 빌드 단계 (예: "symbol_library", "schematic")
        """
        self.stage = stage

        if stage:
            message = f"[{stage}] {message}"

        super().__init__(message, error_code="BUILD_ERROR", **kwargs)
