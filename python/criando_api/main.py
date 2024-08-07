import pandas as pd 
from flask import Flask,render_template,jsonify

app = Flask(__name__)

@app.route('/teste')
def homepage():
    return 'essa é a homepage do site'

@app.route('/vendas')
def total_vendas():
    arquivo = pd.read_csv('12-18 - Criando API no Python.csv')
    total_vendas = arquivo['Vendas'].sum()
    resposta = {
        'Total de vendas': total_vendas
    }
    return jsonify(resposta)



app.run(host= '0.0.0.0')