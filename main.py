from flask import Flask, request

from repositorio_proprietarioPet import delete, getProprietarioPetId, getDados, insert

app = Flask(__name__)


@app.route("/")
def main():
    return "Minha API REST em Flask!"

@app.route("/proprietarioPet", methods=['GET'])
def proprietarioPet():
    return  getDados(),200

@app.route("/cadastrar", methods=['POST'])
def cadastrar():
    req_data = request.get_json()
    insert(req_data['matricula'], req_data['nome'], req_data['cpf'], req_data['telefone'])
    return  '',201


@app.route("/Proprietariopet/<id>", methods=['DELETE'])
def remover(id):
    proprietarioPet = getProprietarioPetId(id)
    if proprietarioPet.id > 0:
        delete(id)
        return  'Proprietariopet removido',200
    elif proprietarioPet.id == 0:
        return  'Proprietariopet não encontrado',200
    
if __name__ == "__main__":
    app.run(debug=True, port= "8082")