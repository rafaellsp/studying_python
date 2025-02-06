import os
import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Caminho para o arquivo JSON
basedir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(basedir, 'database/usuarios.json')

# Função para carregar os dados do arquivo JSON
def carregar_usuarios():
    if os.path.exists(database_path):
        with open(database_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# Função para salvar os dados no arquivo JSON
def salvar_usuarios(usuarios):
    with open(database_path, 'w', encoding='utf-8') as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        opcao = request.form.get('opcao')
        
        if nome and opcao:
            # Carregar os usuários existentes
            usuarios = carregar_usuarios()
            
            # Adicionar o novo usuário e voto
            usuarios.append({'nome': nome, 'voto': opcao})
            
            # Salvar os usuários no arquivo JSON
            salvar_usuarios(usuarios)
            
            return redirect(url_for('resultado'))
    
    return render_template('cadastro.html')

@app.route('/resultado')
def resultado():
    # Carregar os usuários do arquivo JSON
    usuarios = carregar_usuarios()
    return render_template('result.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)
