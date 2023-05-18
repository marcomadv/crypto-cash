from cryptocash import app
from flask import render_template,request
from cryptocash.models import *
from cryptocash.config import APIKEY
from cryptocash.models import *


@app.route("/")
def index():
    datos = view_all()
    #cripto = getAllRates(APIKEY,moneda="BTC")
    cripto = getExchange(APIKEY,cripto="ETH")

    return render_template("index.html", data=datos, crypto=cripto)

@app.route("/purchase", methods=['GET','POST'])
def compra():
    if request.method == "GET":
        pass

    if request.method == "POST":
        pass

    return render_template("purchase.html")

@app.route("/status")
def estado():
    return render_template("/status.html")