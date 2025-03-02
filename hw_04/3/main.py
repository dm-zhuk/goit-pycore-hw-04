import sys
from pathlib import Path
from colorize import dir_tree
from colorama import Fore


def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage example: 'python3 main.py ..'" + Fore.RESET)
    else:
        dir_path = Path(sys.argv[1])
        dir_tree(dir_path)


if __name__ == "__main__":
    main()
