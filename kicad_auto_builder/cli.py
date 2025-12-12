"""
CLI - 커맨드라인 인터페이스

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

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S',
)
logger = logging.getLogger(__name__)


def build_command(args):
    """build 명령어 실행."""
    config_path = Path(args.config)

    logger.info("=" * 60)
    logger.info(f"KiCad Auto Builder v{__version__}")
    logger.info("=" * 60)

    # 1. 설정 파일 로드
    logger.info(f"설정 파일 로드: {config_path}")
    try:
        config = load_config(config_path)
    except Exception as e:
        logger.error(f"설정 파일 로드 실패: {e}")
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
    except Exception as e:
        logger.error(f"빌드 실패: {e}")
        import traceback
        traceback.print_exc()
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
