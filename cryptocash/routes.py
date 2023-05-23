from cryptocash import app
from flask import render_template,request
from cryptocash.models import *
from cryptocash.config import APIKEY
from cryptocash.models import *
from datetime import datetime
now=datetime.now()


@app.route("/")
def index():
    
    datos = view_all()
    registros = len(datos)
    
    #cripto = getAllRates(APIKEY,moneda="BTC")
    #cripto = getExchange(APIKEY,crypto="ETH")

    return render_template("index.html", data=datos, page="/",registros = registros)

@app.route("/purchase", methods=['GET','POST'])
def compra():

   # dataForm=[{}]

    cryptos=["EUR","ETH","BNB","ADA","DOT","BTC","USDT","XRP","SOL","MATIC"]
    coins = coinsFrom()

    if request.method == "GET":
  
        return render_template("purchase.html",monedas = coins, criptos=cryptos,pu = 0, page="/purchase")

    if request.method == "POST":
        print(request.form)
        coinfrom = request.form.get("coinFrom")
        cointo = request.form.get("coinTo")
        print(f"Coin from {coinfrom} coin to {cointo}")
        rate = getExchangeEur(APIKEY,coinfrom)
        print(f"The exchange is: {rate}")
        
        fromq = request.form.get("fromQ")
        fromq = float(fromq)
        print(f"el valor introducido en formQ es: {fromq}")
        fromto = request.form.get("fromTo")
        print(f"el valor introducido en formTo es: {fromto}")
       
        hora = now.time()
        fecha = now.date()
        print(hora)
        print(fecha)
        cambio = changeCrypto(APIKEY,fromq,coinfrom,cointo)

    return render_template("purchase.html",monedas=coins, criptos=cryptos, pu = rate, qto=cambio, page="/purchase")

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
    


    return render_template("status.html",invertido=suma,recuperado = rec, valorcompra = valor, page = "/status")