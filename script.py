from os import walk,path
from shutil import move
import pandas as pd
from typer import Typer,Argument,Option
from pathlib import Path
from utils import read_list

app = Typer()

@app.command(help='Walk a directory and rename all files on a list')
def rename_files(folder_path: Path = Argument(
    default='.',
    exists=True,
    file_okay=True,
    dir_okay=True,
    readable=True,
    resolve_path=True
),list_path: Path = Argument(
    default='list.csv',
    exists=True,
    file_okay=True,
    dir_okay=True,
    readable=True,
    resolve_path=True
),
):
    list = read_list(list_path)
    
    for cp,dir,files in walk(folder_path):
        for file in files:
            if file in list:
                move(path.join(cp,file), path.join(cp, list[file]))

if __name__ == '__main__':
    app()
