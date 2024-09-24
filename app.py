
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Lista de nomes e sobrenomes
nomes = ["João", "Maria", "Pedro", "Ana", "Carlos", "Paula"]
sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Ferreira", "Costa"]

# Lista de domínios aleatórios para os e-mails
dominios = ["uol.com", "gmail.com", "hotmail.com"]

# Rota principal para exibir o formulário
@app.route('/')
def index():
    return render_template('index.html')

# Rota para gerar os fake users
@app.route('/gerar_usuarios', methods=['POST'])
def gerar_usuarios():
    quantidade = int(request.form['quantidade'])  # Quantidade de usuários que o usuário quer
    usuarios = []

    for _ in range(quantidade):
        nome = random.choice(nomes)
        sobrenome = random.choice(sobrenomes)
        dominio = random.choice(dominios)
        email = f"{nome.lower()}.{sobrenome.lower()}@{dominio}"
        usuarios.append({"nome": nome, "sobrenome": sobrenome, "email": email})

    return jsonify(usuarios)  # Devolve a lista em formato JSON

if __name__ == '__main__':
    app.run(debug=True)
