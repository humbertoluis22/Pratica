import sqlite3
import pandas as pd
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.banco_de_dados import Db_lite

if __name__ == "__main__":
    # criar_pasta  primeiro teste
    db_lite = Db_lite(nome_banco="Casa.db")

    dict = {
        "Nome": ["maria", "guilherme", "humberto", "isabela", "teste"],
        "idade": [40, 47, 23, 20, 00000000],
    }
    df = pd.DataFrame(dict)
    print(df)
    # db_lite.escrever_tabela(nome_tabela='validando',dataframe=df,if_exists='replace')
    # db_lite.excluir_registro('validando',['Nome','idade'],['humberto',23])
    # db_lite.excluir_registro('validando',['Nome'],['maria'])
    # df_validando = db_lite.ler_tabela('validando')
    # script = 'Delete from validando where Nome = "guilherme"'
    # db_lite.execute_query(query=script)
    db_lite.update('validando',colunas=['Nome','idade'],valores=['isabela','21'],col_condi='Nome',cond='isabela')
    print("***********************")
    # print(df_validando)
    pass
