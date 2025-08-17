from colorama import Fore, Style
from sys import argv, exit
from pathlib import Path

#function of visualisation path directory
def path_tree(path:Path,lvl:int = 0) -> None:
    """
    Function of visualisation path directory
    Input:
    path: Path - the directory path to visualize
    lvl: int - the current level of depth in the directory tree
    Return: None    
    """
    tab_symbol = "   "
    print(Fore.BLUE + tab_symbol*lvl + path.name + '\\' +Style.RESET_ALL)
    
    if path.exists:
        for item in path.iterdir():
            if item.is_dir():
                path_tree(item, lvl + 1)
            else:
                print(Fore.GREEN +tab_symbol*(lvl+1) + item.name + Style.RESET_ALL)


def main():
    if len(argv) != 2:
        print("Usage: python main.py <path_to_directory>")
        return
    
    path = argv[1]
    folder_path = Path(path)
 
    if folder_path.exists() and folder_path.is_dir():
        try:
            path_tree(folder_path)
        except PermissionError:
            print(f'Permission denied while accessing {folder_path}')
        except Exception as e:
            print(f'Error occurred while accessing {folder_path}: {e}')
        finally:
            return
    else:
        print(f'Invalid directory: {folder_path}')
        return


if __name__ == "__main__":
    main()