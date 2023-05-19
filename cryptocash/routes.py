from cryptocash import app
from flask import render_template,request
from cryptocash.models import *
from cryptocash.config import APIKEY
from cryptocash.models import *


@app.route("/")
def index():
    datos = view_all()
    #cripto = getAllRates(APIKEY,moneda="BTC")
    #cripto = getExchange(APIKEY,crypto="ETH")

    return render_template("index.html", data=datos)

@app.route("/purchase", methods=['GET','POST'])
def compra():

    cryptos=["EUR","ETH","BNB","ADA","DOT","BTC","USDT","XRP","SOL","MATIC"]
    coins = coinsFrom()
    cointo2 = "Hola"
    if request.method == "GET":
        pass

    if request.method == "POST":
        print(request.form)
        coinfrom = request.form["coinFrom"]
        cointo = request.form["coinTo"]
        print(f"Coin from {coinfrom} coin to {cointo}")
        rate = getExchange(APIKEY,coinfrom,cointo)
        print(f"The exchange is: {rate}")
        cointo2 = "Adios"
    
    return render_template("purchase.html",monedas=coins, criptos=cryptos,resultado=cointo2)

@app.route("/status")
def estado():
    return render_template("/status.html")