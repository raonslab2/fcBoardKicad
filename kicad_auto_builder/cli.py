"""
CLI - 커맨드라인 인터페이스 v1.4

Usage:
    python -m kicad_auto_builder.cli build power_board.yaml
    python -m kicad_auto_builder.cli build power_board.yaml --dry-run
    python -m kicad_auto_builder.cli validate power_board.yaml
"""

import argparse
import logging
import sys
from pathlib import Path

from . import __version__
from .config_loader import load_config, validate_config
from .part_resolver import PartResolver
from .kicad_builder import KicadBuilder
from .net_validator import validate_nets
from .exceptions import (
    KicadAutoBuilderError,
    ConfigError,
    ConfigValidationError,
    EasyEDAError,
    NetworkError,
    CacheError,
)

logger = logging.getLogger(__name__)


def setup_logging(verbose: bool = False, log_file: Path = None):
    """로깅을 설정합니다.

    Args:
        verbose: 상세 로그 출력 여부
        log_file: 로그 파일 경로 (None이면 파일 로깅 비활성화)
    """
    level = logging.DEBUG if verbose else logging.INFO

    # 포맷 설정
    detailed_format = '%(asctime)s [%(levelname)s] %(name)s:%(lineno)d - %(message)s'
    simple_format = '%(asctime)s [%(levelname)s] %(message)s'

    # 루트 로거 설정
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.handlers = []

    # 콘솔 핸들러
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(logging.Formatter(
        detailed_format if verbose else simple_format,
        datefmt='%H:%M:%S'
    ))
    root_logger.addHandler(console_handler)

    # 파일 핸들러 (옵션)
    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter(detailed_format))
        root_logger.addHandler(file_handler)
        logger.info(f"로그 파일: {log_file}")


def build_command(args):
    """build 명령어 실행."""
    config_path = Path(args.config)

    # 로깅 설정
    log_file = None
    if hasattr(args, 'log') and args.log:
        output_dir = Path(args.output) if args.output else Path('out')
        log_file = output_dir / 'build.log'
    setup_logging(args.verbose, log_file)

    logger.info("=" * 60)
    logger.info(f"KiCad Auto Builder v{__version__}")
    logger.info("=" * 60)

    # 1. 설정 파일 로드
    logger.info(f"설정 파일 로드: {config_path}")
    try:
        config = load_config(config_path)
    except ConfigValidationError as e:
        logger.error(f"설정 검증 실패:\n{e}")
        sys.exit(1)
    except ConfigError as e:
        logger.error(f"설정 파일 오류: {e}")
        sys.exit(1)
    except FileNotFoundError as e:
        logger.error(f"파일을 찾을 수 없습니다: {config_path}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"설정 파일 로드 실패: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

    logger.info(f"프로젝트: {config.name}")
    logger.info(f"부품 수: {len(config.parts)}")

    # 캐시 디렉토리 오버라이드
    if args.cache_dir:
        config.cache_dir = args.cache_dir

    # 출력 디렉토리 오버라이드
    if args.output:
        config.out_dir = args.output

    # 2. 설정 검증
    warnings = validate_config(config)
    for w in warnings:
        logger.warning(f"설정 경고: {w}")

    # 3. Dry-run 모드
    if args.dry_run:
        logger.info("")
        logger.info("[DRY-RUN] 실제 파일을 생성하지 않습니다.")
        logger.info("")
        logger.info(f"프로젝트: {config.name}")
        logger.info(f"출력 디렉토리: {config.out_dir}")
        logger.info(f"KiCad 버전: {config.kicad_version}")
        logger.info(f"Builder 버전: {__version__}")
        logger.info("")

        # 계층/단일 모드에 따라 부품 표시
        if config.is_hierarchical:
            logger.info(f"모드: 계층 시트 ({len(config.sheets)}개 시트)")
            for sheet in config.sheets:
                logger.info(f"  [{sheet.name}] ({len(sheet.parts)}개 부품)")
                for part in sheet.parts[:3]:
                    logger.info(f"    - {part.ref}: {part.role} (LCSC: {part.lcsc or 'N/A'})")
                if len(sheet.parts) > 3:
                    logger.info(f"    ... (+{len(sheet.parts) - 3} more)")
        else:
            logger.info("모드: 단일 시트")
            logger.info("부품 목록:")
            for part in config.parts:
                logger.info(f"  - {part.ref}: {part.role} (LCSC: {part.lcsc or 'N/A'})")

        logger.info("")
        logger.info("네트 프리셋:")
        for name, value in config.net_presets.items():
            logger.info(f"  - {name}: {value}")
        return

    # 4. 부품 리졸브 (all_parts: 단일/계층 모드 통합)
    logger.info("")
    logger.info("부품 리졸브 중...")
    resolver = PartResolver(
        cache_dir=config.cache_dir,
        prefer_kicad_lib=config.prefer_kicad_lib,
    )

    all_parts = config.all_parts  # 단일/계층 모드 통합

    try:
        resolved_parts = resolver.resolve_all(all_parts)
    except EasyEDAError as e:
        logger.error(f"LCSC 부품 다운로드 실패: {e}")
        sys.exit(1)
    except NetworkError as e:
        logger.error(f"네트워크 오류: {e}")
        sys.exit(1)
    except CacheError as e:
        logger.error(f"캐시 오류: {e}")
        sys.exit(1)
    except ValueError as e:
        logger.error(str(e))
        sys.exit(1)

    logger.info(f"리졸브 완료: {len(resolved_parts)}개 부품")

    # 5. 핀-넷 검증
    logger.info("")
    logger.info("핀-넷 검증 중...")
    net_errors, net_warnings = validate_nets(resolved_parts, all_parts)

    # warnings 출력
    for w in net_warnings:
        logger.warning(w)

    # errors가 있으면 중단
    if net_errors:
        logger.error("핀-넷 검증 실패:")
        for e in net_errors:
            logger.error(f"  {e}")
        sys.exit(1)

    logger.info(f"핀-넷 검증 완료 (warnings: {len(net_warnings)})")

    # 6. 빌드
    logger.info("")
    builder = KicadBuilder(config, resolved_parts)

    try:
        result = builder.build_all(warnings=net_warnings)
    except KicadAutoBuilderError as e:
        logger.error(f"빌드 실패: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"빌드 실패: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        else:
            logger.info("상세 정보는 --verbose 옵션을 사용하세요")
        sys.exit(1)

    # 7. 결과 출력
    logger.info("")
    logger.info("생성된 파일:")
    for name, path in result.items():
        if path:
            logger.info(f"  - {name}: {path}")


def validate_command(args):
    """validate 명령어 실행 (v1.3: 파일 생성 없이 검증만)."""
    config_path = Path(args.config)

    logger.info("=" * 60)
    logger.info(f"KiCad Auto Builder v{__version__} - Validate Mode")
    logger.info("=" * 60)

    # 1. 설정 파일 로드
    logger.info(f"설정 파일 로드: {config_path}")
    try:
        config = load_config(config_path)
    except Exception as e:
        logger.error(f"설정 파일 로드 실패: {e}")
        sys.exit(1)

    logger.info(f"프로젝트: {config.name}")

    if config.is_hierarchical:
        logger.info(f"모드: 계층 시트 ({len(config.sheets)}개 시트)")
        total_parts = sum(len(s.parts) for s in config.sheets)
        logger.info(f"총 부품 수: {total_parts}")
    else:
        logger.info(f"모드: 단일 시트")
        logger.info(f"부품 수: {len(config.parts)}")

    # 2. 설정 검증
    logger.info("")
    logger.info("설정 검증 중...")
    config_warnings = validate_config(config)
    for w in config_warnings:
        logger.warning(f"설정 경고: {w}")

    # 3. 부품 리졸브 (가능하면)
    logger.info("")
    logger.info("부품 리졸브 중...")
    resolver = PartResolver(
        cache_dir=config.cache_dir,
        prefer_kicad_lib=config.prefer_kicad_lib,
    )

    all_parts = config.all_parts
    resolve_errors = []

    try:
        resolved_parts = resolver.resolve_all(all_parts)
        logger.info(f"리졸브 완료: {len(resolved_parts)}개 부품")
    except ValueError as e:
        resolve_errors.append(str(e))
        logger.error(f"리졸브 실패: {e}")
        resolved_parts = []

    # 4. 핀-넷 검증 (리졸브 성공 시)
    net_errors = []
    net_warnings = []

    if resolved_parts:
        logger.info("")
        logger.info("핀-넷 검증 중...")
        net_errors, net_warnings = validate_nets(resolved_parts, all_parts)

        for w in net_warnings:
            logger.warning(w)

        if net_errors:
            logger.error("핀-넷 검증 실패:")
            for e in net_errors:
                logger.error(f"  {e}")

        logger.info(f"핀-넷 검증 완료 (errors: {len(net_errors)}, warnings: {len(net_warnings)})")

    # 5. 결과 요약
    logger.info("")
    logger.info("=" * 60)
    logger.info("검증 결과 요약")
    logger.info("=" * 60)

    total_errors = len(resolve_errors) + len(net_errors)
    total_warnings = len(config_warnings) + len(net_warnings)

    logger.info(f"  Errors: {total_errors}")
    logger.info(f"  Warnings: {total_warnings}")

    if total_errors > 0:
        logger.error("검증 실패 - 위 오류를 수정하세요.")
        sys.exit(1)
    elif total_warnings > 0:
        logger.warning("검증 통과 (경고 있음)")
        sys.exit(0)
    else:
        logger.info("검증 통과")
        sys.exit(0)


def main():
    """메인 진입점."""
    parser = argparse.ArgumentParser(
        prog="kicad_auto_builder",
        description=f"KiCad 자동 회로 생성기 v{__version__} - YAML 파일로 회로도 자동 생성",
    )

    subparsers = parser.add_subparsers(dest="command", help="명령어")

    # build 명령어
    build_parser = subparsers.add_parser("build", help="프로젝트 빌드")
    build_parser.add_argument("config", help="YAML 설정 파일 경로")
    build_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="파일 생성 없이 어떤 작업을 할지만 출력",
    )
    build_parser.add_argument(
        "--cache-dir",
        help="easyeda2kicad 캐시 디렉토리 (기본: cache)",
    )
    build_parser.add_argument(
        "--output", "-o",
        help="출력 디렉토리",
    )
    build_parser.add_argument(
        "--prefer-kicad-lib",
        action="store_true",
        help="KiCad 기본 라이브러리 우선 사용",
    )
    build_parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="상세 로그 출력",
    )
    build_parser.add_argument(
        "--log",
        action="store_true",
        help="빌드 로그를 파일로 저장 (out/build.log)",
    )

    # validate 명령어 (v1.3)
    validate_parser = subparsers.add_parser("validate", help="설정 파일 검증 (파일 생성 없음)")
    validate_parser.add_argument("config", help="YAML 설정 파일 경로")
    validate_parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="상세 로그 출력",
    )

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(0)

    # 상세 로그 모드
    if hasattr(args, 'verbose') and args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    if args.command == "build":
        build_command(args)
    elif args.command == "validate":
        validate_command(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
