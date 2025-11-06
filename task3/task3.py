import sys
from pathlib import Path
from colorama import Fore

def print_directory_structure(filepath: Path, separator: str=""):
    """
    Print files from directory by path. If filepath is dir - run itself recursive.

    Args:
        path - path to the file.
        separator - symbol before file name

    """
    for item in filepath.iterdir():
        if item.is_dir():
            print(f"{separator}{Fore.BLUE}{item.name}/")
            print_directory_structure(item, separator + "   ")
        else:
            print(f"{separator}{Fore.GREEN}{item.name}")


def get_files_from_directory():
    """"
    Checks if directory exist and it is directory. Prints file structure by directory. 

    Args:
        path - get path to folder as script start parameter.

    Raises:
        if path/data wrong returns an empty array.
    """
    if len(sys.argv) < 2:
        print(f"{Fore.RED} Error. Please add path to the directory.")
        print(f"{Fore.YELLOW} Example: python task3.py C:/Users/Admin/Pictures")
        sys.exit(1)

    directory = Path(sys.argv[1])

    if not directory.exists():
        print(f"{Fore.RED}Error '{directory}' not exist.")
        sys.exit(1)

    if not directory.is_dir():
        print(f"{Fore.RED}Error: '{directory}' is not directory.")
        sys.exit(1)

    # Print root directory
    print(f"{Fore.CYAN}{directory.name}/")
    print_directory_structure(directory, separator="    ")

if __name__ == "__main__":
    get_files_from_directory()
