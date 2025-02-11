from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint("cliente", __name__)

@cliente_route.route("/")
def lista_clientes():
    return render_template("lista_clientes.html", clientes=CLIENTES)

@cliente_route.route("/cadastro", methods=["GET", "POST"])
def cadastro_clientes():
    if request.method == "GET":
        return render_template("cadastro_clientes.html")
    else:
        nome = request.form.get("nome")
        email = request.form.get("email")
        return render_template("<p>teste</p>")
