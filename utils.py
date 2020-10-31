from pathlib import Path
import pandas as pd
from typer import secho
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
    
    else:
        secho('El formato de la lista no es soportado')
    
read_list('./list.csv')