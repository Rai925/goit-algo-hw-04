import sys
from pathlib import Path
from colorama import Fore, Style

def display_directory_structure(directory_path, indent=0):
    path = Path(directory_path)

    if not path.exists() or not path.is_dir():
        print(f"{Fore.RED}Помилка: Директорія не існує або не є директорією.{Style.RESET_ALL}")
        return

    for item in path.iterdir():
        if item.is_dir():
            print(Fore.BLUE + "  " * indent + f"📂 {item.name}" + Style.RESET_ALL)
            display_directory_structure(item, indent + 1)
        elif item.is_file():
            print(Fore.GREEN + "  " * indent + f"📜 {item.name}" + Style.RESET_ALL)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <absolute_directory_path>")
    else:
        directory_path = sys.argv[1]
        display_directory_structure(directory_path)
