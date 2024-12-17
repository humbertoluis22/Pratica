import sqlite3
import pandas as pd
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from decorators.decoradores import *


class Db_lite:
    def __init__(self, nome_banco, path="c:\\DataPy") -> None:
        try:
            os.makedirs(path)
        except:
            pass
        caminho_completo = os.path.join(path, nome_banco)
        conn = sqlite3.connect(caminho_completo)
        self._conn = conn
        self._cursor = conn.cursor()


    @commit_e_close
    def escrever_tabela(self, nome_tabela, dataframe: pd.DataFrame, if_exists="append"):
        dataframe.to_sql(nome_tabela, self._conn, if_exists=if_exists, index=False)


    def ler_tabela(self, nome_tabela):
        try:
            df = pd.read_sql(f"SELECT * FROM  {nome_tabela}", self._conn)
        except Exception;
            df = pd.DataFrame() 
        return df
    

    @commit_e_close
    def update(
        self, nome_tabela: str, colunas: list, valores: list, col_condi: str, cond: str
    ):
        if len(colunas) != len(valores):
            print(
                "Necessario que colunas e valores tenham o mesmo tamanho para montar script"
            )
            return
        colunas_valores = zip(colunas,valores)
        script_inicial = f'UPDATE {nome_tabela} SET '
        parte_final = f' WHERE {col_condi} = "{cond}"'
        script_cols = []
        for col , val in colunas_valores:
            script_col = f' {col} = "{val}"'
            script_cols.append(script_col)

        script_col = ','.join(script_cols)
        script_final = script_inicial + script_col + parte_final
        self._conn.executescript(script_final)


    @commit_e_close
    def excluir_registro(
        self, nome_tabela: str, coluna_chave: list = [], valor: list = []
    ):

        if len(coluna_chave) != len(valor):
            print("As duas listas precisam ter o mesmo tamanho para montar o script")
            return

        if len(coluna_chave) == 1:
            query = f'DELETE FROM {nome_tabela} WHERE {coluna_chave[0]} = "{valor[0]}"'
            self._conn.executescript(query)
            return
        else:
            chave_valor = zip(coluna_chave, valor)
            ultima_parte_script = []
            script_inicial = f"DELETE FROM {nome_tabela} WHERE "
            for chave, valor in chave_valor:
                script = f' {chave} = "{valor}" '
                ultima_parte_script.append(script)
            ultima_parte_script = " and ".join(ultima_parte_script)
            script_inicial += ultima_parte_script
            script_final = script_inicial
            print(script_final)
            self._conn.executescript(script_final)

    @commit_e_close
    def execute_query(self, query):
        self._conn.executescript(query)

    @commit_e_close
    def drop_table(self, tb_name):
        """Deleta a tabela do banco de dados."""
        self.run_query(f"DROP TABLE {tb_name}")


if __name__ == "__main__":
    # criar_pasta  primeiro teste
    db_lite = Db_lite(nome_banco="Casa.db")

    dict = {
        "Nome": ["maria", "guilherme", "humberto", "isabela", "teste"],
        "idade": [40, 47, 23, 20, 00000000],
    }
    df = pd.DataFrame(dict)
    print(df)
    db_lite.escrever_tabela(nome_tabela='validando',dataframe=df,if_exists='replace')
    # db_lite.excluir_registro('validando',['Nome','idade'],['humberto',23])
    # db_lite.excluir_registro('validando',['Nome'],['maria'])
    # df_validando = db_lite.ler_tabela('validando')
    # script = 'Delete from validando where Nome = "guilherme"'
    # db_lite.execute_query(query=script)
    print("***********************")
    # print(df_validando)
    pass
