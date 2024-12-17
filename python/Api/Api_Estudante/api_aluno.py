from  flask import Flask,request,jsonify
from data.banco_de_dados import Db_lite
import pandas as pd 

app = Flask(__name__)
db_lite = Db_lite('RegistroDeAlunos.db')



@app.route('/aluno',methods = ['GET'])
def alunos_cadastrados():
    df_alunos = db_lite.ler_tabela('RegistroDeAlunos.db')
    json_alunos = df_alunos.to_json() 
    return json_alunos
    


@app.route('/aluno',methods = ['PUT'])
def atualizar_aluno():
    data = request.get_json()
    print(data)
    # recolher informações necessarias para efetuar 
    # a atualizção do aluno 
    pass

@app.route('/aluno',methods = ['DELET'])
def deletar_registro():
    #info para deletar aluno 
    pass


@app.route('/aluno',methods = ['POST'])
def cadastrar_aluno():
    data = request.get_json()
    print(data)
    #cadastrar aluno
    pass


