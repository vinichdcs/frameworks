from flask import Flask, render_template, request
from markupsafe import escape
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cad/cadastro")
def cadastro():
    return render_template('cadastro.html')

@app.route("/cad/caduser", methods=['POST'])
def caduser():
    return request.form

@app.route("/cad/categoria")
def categoria():
    return render_template('categoria.html')

@app.route("/anuncios/vendas")
def vendas():
    return render_template('vendas.html')

@app.route("/anuncios/compras")
def compras():
    print("anuncio comprado")
    return ""
