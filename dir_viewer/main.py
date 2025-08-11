from colorama import Fore, Style
from sys import argv
from pathlib import Path

def path_tree(path:Path,lvl:int = 0):
    tab_symbol = "   "
    print(Fore.BLUE + tab_symbol*lvl + path.name + '\\' +Style.RESET_ALL)
    
    if path.exists:
        for item in path.iterdir():
            if item.is_dir():
                path_tree(item, lvl + 1)
            else:
                print(Fore.GREEN +tab_symbol*(lvl+1) + item.name + Style.RESET_ALL)


def main():
    folder_path = Path(argv[1])
    # print(folder_path.iterdir())
    # for item in folder_path.iterdir():
    #     if item.is_dir():
    #         # folder_string = 
    #         print(item)
    path_tree(folder_path)

if __name__ == "__main__":
    main()