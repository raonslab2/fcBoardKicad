"""
Symbols Package - 심볼 레지스트리 및 관리

심볼 정의를 카테고리별로 관리하고 검색 기능을 제공합니다.
"""

import logging
from typing import Optional
from collections import defaultdict

from .base import SymbolDefinition, SymbolCategory, PinDefinition

logger = logging.getLogger(__name__)


class SymbolRegistry:
    """심볼 레지스트리 - 내장/외부 심볼 통합 관리.

    싱글톤 패턴으로 구현되어 전역에서 동일한 인스턴스 사용.
    """

    _instance: Optional['SymbolRegistry'] = None
    _initialized: bool = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True

        self._symbols: dict[str, SymbolDefinition] = {}
        self._by_category: dict[SymbolCategory, list[str]] = defaultdict(list)
        self._loaded_categories: set[str] = set()

    @classmethod
    def instance(cls) -> 'SymbolRegistry':
        """싱글톤 인스턴스 반환."""
        return cls()

    @classmethod
    def reset(cls):
        """레지스트리 초기화 (테스트용)."""
        if cls._instance:
            cls._instance._symbols = {}
            cls._instance._by_category = defaultdict(list)
            cls._instance._loaded_categories = set()

    def register(self, symbol: SymbolDefinition) -> None:
        """심볼을 등록합니다.

        Args:
            symbol: 등록할 심볼 정의
        """
        if symbol.name in self._symbols:
            logger.debug(f"심볼 덮어쓰기: {symbol.name}")

        self._symbols[symbol.name] = symbol
        if symbol.name not in self._by_category[symbol.category]:
            self._by_category[symbol.category].append(symbol.name)

    def register_raw(
        self,
        name: str,
        kicad_symbol: str,
        category: SymbolCategory = SymbolCategory.MISC,
        reference_prefix: str = "U",
        **kwargs
    ) -> SymbolDefinition:
        """KiCad 심볼 문자열로 직접 등록합니다.

        Args:
            name: 심볼 이름
            kicad_symbol: KiCad 심볼 정의 문자열
            category: 카테고리
            reference_prefix: 레퍼런스 접두사
            **kwargs: SymbolDefinition의 추가 인자

        Returns:
            등록된 SymbolDefinition
        """
        symbol = SymbolDefinition(
            name=name,
            kicad_symbol=kicad_symbol,
            category=category,
            reference_prefix=reference_prefix,
            **kwargs
        )
        self.register(symbol)
        return symbol

    def get(self, name: str) -> Optional[SymbolDefinition]:
        """심볼을 조회합니다.

        Args:
            name: 심볼 이름

        Returns:
            SymbolDefinition 또는 None
        """
        # 지연 로딩: 처음 접근 시 카테고리 로드
        if not self._loaded_categories:
            self._load_all_categories()

        return self._symbols.get(name)

    def get_kicad_symbol(self, name: str) -> Optional[str]:
        """KiCad 심볼 문자열을 반환합니다 (기존 BUILTIN_SYMBOLS 호환).

        Args:
            name: 심볼 이름

        Returns:
            KiCad 심볼 정의 문자열 또는 None
        """
        symbol = self.get(name)
        if symbol:
            return symbol.kicad_symbol
        return None

    def has(self, name: str) -> bool:
        """심볼 존재 여부 확인."""
        if not self._loaded_categories:
            self._load_all_categories()
        return name in self._symbols

    def list_category(self, category: SymbolCategory) -> list[str]:
        """카테고리별 심볼 목록을 반환합니다.

        Args:
            category: 조회할 카테고리

        Returns:
            심볼 이름 목록
        """
        if not self._loaded_categories:
            self._load_all_categories()
        return list(self._by_category.get(category, []))

    def list_all(self) -> list[str]:
        """모든 심볼 이름 목록을 반환합니다."""
        if not self._loaded_categories:
            self._load_all_categories()
        return list(self._symbols.keys())

    @property
    def categories(self) -> list[SymbolCategory]:
        """등록된 카테고리 목록."""
        if not self._loaded_categories:
            self._load_all_categories()
        return list(self._by_category.keys())

    def to_dict(self) -> dict[str, str]:
        """기존 BUILTIN_SYMBOLS 형식 딕셔너리로 변환 (호환용).

        Returns:
            {name: kicad_symbol_str, ...}
        """
        if not self._loaded_categories:
            self._load_all_categories()
        return {name: sym.kicad_symbol for name, sym in self._symbols.items()}

    def _load_all_categories(self):
        """모든 카테고리 모듈을 로드합니다."""
        if self._loaded_categories:
            return

        try:
            from .categories import passive
            passive.register_symbols(self)
            self._loaded_categories.add("passive")
        except ImportError as e:
            logger.debug(f"passive 모듈 로드 실패: {e}")

        try:
            from .categories import power
            power.register_symbols(self)
            self._loaded_categories.add("power")
        except ImportError as e:
            logger.debug(f"power 모듈 로드 실패: {e}")

        try:
            from .categories import connectors
            connectors.register_symbols(self)
            self._loaded_categories.add("connectors")
        except ImportError as e:
            logger.debug(f"connectors 모듈 로드 실패: {e}")

        try:
            from .categories import regulators
            regulators.register_symbols(self)
            self._loaded_categories.add("regulators")
        except ImportError as e:
            logger.debug(f"regulators 모듈 로드 실패: {e}")

        try:
            from .categories import transistors
            transistors.register_symbols(self)
            self._loaded_categories.add("transistors")
        except ImportError as e:
            logger.debug(f"transistors 모듈 로드 실패: {e}")

        try:
            from .categories import opamps
            opamps.register_symbols(self)
            self._loaded_categories.add("opamps")
        except ImportError as e:
            logger.debug(f"opamps 모듈 로드 실패: {e}")

        try:
            from .categories import interface
            interface.register_symbols(self)
            self._loaded_categories.add("interface")
        except ImportError as e:
            logger.debug(f"interface 모듈 로드 실패: {e}")

        logger.debug(f"심볼 로드 완료: {len(self._symbols)}개")


# 편의 함수
def get_symbol(name: str) -> Optional[str]:
    """심볼 문자열을 가져옵니다 (편의 함수)."""
    return SymbolRegistry.instance().get_kicad_symbol(name)


def get_builtin_symbol(name: str) -> Optional[str]:
    """기존 API 호환용 함수."""
    return get_symbol(name)


__all__ = [
    "SymbolRegistry",
    "SymbolDefinition",
    "SymbolCategory",
    "PinDefinition",
    "get_symbol",
    "get_builtin_symbol",
]
