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

   # dataForm=[{}]

    cryptos=["EUR","ETH","BNB","ADA","DOT","BTC","USDT","XRP","SOL","MATIC"]
    coins = coinsFrom()
    cointo2 = "Hola"

    if request.method == "GET":
  
        return render_template("purchase.html",monedas = coins, criptos=cryptos,resultado=cointo2,pu = 0)

    if request.method == "POST":
        print(request.form)
        coinfrom = request.form["coinFrom"]
        cointo = request.form["coinTo"]
        print(f"Coin from {coinfrom} coin to {cointo}")
        rate = getExchange(APIKEY,coinfrom,cointo)
        print(f"The exchange is: {rate}")
        cointo2 = "Adios"
        fromq = request.form["fromQ"]
        print(f"el valor introducido en formQ es: {fromq}")
        fromto = request.form["fromTo"]
        print(f"el valor introducido en formTo es: {fromto}")

    return render_template("purchase.html",monedas=coins, criptos=cryptos,resultado=cointo2, pu = rate)

@app.route("/status")
def estado():

    suma = sumFrom("EUR")
    rec = sumTo("EUR")
    valor = sumFrom("EUR") - sumTo("EUR")



    valores = []
    criptos = cryptoFrom()
    for i in criptos:  
        value = getExchangeEur(APIKEY,i)
        valores.append(value)
    




    


    return render_template("/status.html",invertido=suma,recuperado = rec, valorcompra = valor)