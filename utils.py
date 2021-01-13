from pathlib import Path
import pandas as pd
from typer import secho
import os
from shutil import move
# from os import path

def read_list(list_path:Path):
    
    if str(list_path).endswith('.csv'):
        list = pd.read_csv(list_path, sep=';')
        from_col = []
        to_col = []
        for i in list['from']:
            from_col.append(i)
        for i in list['to']:
            to_col.append(i)
        
        list = {}
        
        for i in range(len(from_col)):
            list[from_col[i]] = to_col[i]
        return list
    
    if str(list_path).endswith('.txt'):
        
        f = open(list_path, encoding="utf-8")
        list = {}
        
        for i in f.readlines():
            pair = i.split(';')
            list[pair[0]] = pair[1]
        
        return list
    
    else:
        secho('El formato de la lista no es soportado')

def move_files(path:Path):
    for dir,cp,files in os.walk(path):
        for file in files:
            # print(dir)
            folder_name = str(file[:str(file).rfind('.')])
            # print(folder_name)
            os.makedirs(os.path.join(dir,folder_name), exist_ok=True)
            move(os.path.join(dir,file),os.path.join(dir,folder_name)) 
            
# read_list('./list.csv')