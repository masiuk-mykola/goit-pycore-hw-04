import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)


def print_directory_tree(path: Path, prefix=""):
    print(f"{prefix}{Fore.BLUE}{path.name}/")
    indent = " " * 4
    try:
        for item in sorted(path.iterdir()):
            if item.is_dir():
                print_directory_tree(item, indent)
            elif item.is_file():
                print(f"{prefix}{indent}{Fore.GREEN}{item.name}")
    except Exception as e:
        print(f"{prefix}{indent}{Fore.RED}[Error accessing {path}]: {e}")


def main():
    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(f"{Fore.RED} The path does not exist: {dir_path}")
        sys.exit(1)

    if not dir_path.is_dir():
        print(f"{Fore.RED} This is not a directory: {dir_path}")
        sys.exit(1)

    print_directory_tree(dir_path)


if __name__ == "__main__":
    main()
