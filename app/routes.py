from flask import render_template
from app import app

# Rota da página inicial
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Exemplo de Usuário'}  # Simule um usuário (isso pode vir de um banco de dados)
    return render_template('index.html', title='Página Inicial', user=user)

# Rota da página de exemplo
@app.route('/exemplo')
def exemplo():
    return 'Esta é uma página de exemplo'