from flask import Flask,request,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

usuarios =[]

@app.route('/usuario', methods = ['POST'])
def incluir_usuario():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Dados inválidos!'}), 204
    usuarios.append(data)
    return jsonify({'message':'Usuario com sucesso !!'}),200

@app.route('/usuario', methods = ['PUT'])
def atualizar_usuario():
    data = request.get_json()
    for usuario in usuarios:
        if usuario['nome'] == data['nome']:
            usuario.update(data)
            return jsonify({'message':'Usuario atualizado com sucesso!'})
    return jsonify({'message':'Usuario não encontrado!'}),204

@app.route('/usuario',methods=['DELETE'])
def deletar_usuario():
    data = request.get_json()
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario['nome'] != data['nome'] ]
    return jsonify({'message':'Usuario deletado com sucesso !!!'})

@app.route('/usuario',methods = ['GET'])
def verificar_usuario():
    nome = request.args.get('nome')
    for usuario in usuarios:
        if usuario['nome'] == nome:
            return jsonify(usuario)
    return jsonify({'message':'Usuario não encontrado!'}),404


if __name__ == '__main__':
    app.run(debug=True)