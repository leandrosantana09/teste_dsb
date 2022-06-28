import pandas as pd
import os


def get_df(pasta):
    
    lista_item = []
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            lista_item.append(os.path.join(diretorio, arquivo))

    data = pd.concat([pd.read_csv(arquivos) for arquivos in lista_item], 
                axis=0)

    return data        