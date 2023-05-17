from cryptocash import app
from flask import render_template

@app.route("/")
def index():
    return render_template ("index.html")

@app.route("/purchase")
def compra():
    return render_template("purchase.html")

@app.route("/status")
def estado():
    return render_template("/status.html")