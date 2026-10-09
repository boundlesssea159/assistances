import json
import sys
from pathlib import Path


def count_python_files(root: Path) -> dict:
    """统计目录下 Python 文件数量和代码行数。"""

    total_files = 0
    total_lines = 0

    # 忽略常见的虚拟环境和 Git 目录
    ignored_dirs = {
        ".git",
        ".venv",
        "venv",
        "__pycache__",
        "node_modules",
    }

    for path in root.rglob("*.py"):
        if any(part in ignored_dirs for part in path.parts):
            continue

        try:
            lines = len(
                path.read_text(encoding="utf-8").splitlines()
            )
        except (UnicodeDecodeError, OSError):
            continue

        total_files += 1
        total_lines += lines

    return {
        "directory": str(root.resolve()),
        "python_files": total_files,
        "total_lines": total_lines,
    }


if __name__ == "__main__":
    directory = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()

    if not directory.is_dir():
        print(f"Error: {directory} is not a directory", file=sys.stderr)
        sys.exit(1)

    result = count_python_files(directory)
    print(json.dumps(result, ensure_ascii=False, indent=2))