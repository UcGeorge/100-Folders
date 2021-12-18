import os
import re
from tqdm import tqdm


parent_dir = input("Enter start location: ").replace('\\', '/').rstrip('/')
level = input(
    "Enter the maximun level (Note that the number of terminal folders = 2^level): ")
key = input(
    f"Enter a secret number between 0 and {(2**int(level)) - 1} (The binary equivalent will become your secret folder address): ")

key_bin = format(int(key), "b").zfill(10)


def _100Folders(path: str, _level: int):

    try:
        os.mkdir(path)
    except OSError as error:
        if('[WinError 183]' in str(error)):
            pass
        else:
            print(f'[FATAL] {error}')
            exit()

    if _level < int(level):
        __level = int(_level)+1
        for i in range(2):
            _100Folders(os.path.join(path, str(i)), __level)
    else:
        print('.', end='')


if(not re.search(r'[a-zA-Z]:/.*', parent_dir)):
    print('You entered an invalid file parh')
else:
    _100Folders(parent_dir, 0)
    secret_location = parent_dir + '/' + '/'.join([s for s in key_bin])
    print(f"\n\nYour secret location: {secret_location}\n")
