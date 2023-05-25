from cryptocash import app
from flask import render_template,request, redirect
from cryptocash.models import *
from cryptocash.config import APIKEY
from cryptocash.models import *
from cryptocash.forms import MovementsForm
from datetime import datetime
now=datetime.now()


@app.route("/")
def index():
    
    datos = view_all()
    registros = len(datos)

    
    

    return render_template("index.html", data=datos, page="/",registros = registros)

@app.route("/purchase", methods=['GET','POST'])
def compra():
    
    date = now.date()
    hour = now.time()
    cryptos=["EUR","ETH","BNB","ADA","DOT","BTC","USDT","XRP","SOL","MATIC"]
    coins = coinsFrom()
    

    if request.method == "GET":
  
        return render_template("purchase.html",monedas = coins, criptos=cryptos,pu = 0, page="/purchase")

    if request.method == "POST":

        if request.form['action'] == 'Calcular':
            
            coinfrom = request.form.get("coinFrom")           
            cointo = request.form.get("coinTo")
            rate = getExchangeEur(APIKEY,cointo)           
            fromq = request.form.get("fromQ")
            fromq = float(fromq)
            unitprice = rate   #precio unitario de la crypto ( si se divide el Qfrom / rate , da lo mismo que Qto)           
            change = changeCrypto(APIKEY,fromq,coinfrom,cointo)
            
            return render_template("purchase.html",monedas = coins, criptos=cryptos, pu=unitprice, qto=change, page="/purchase")
        else:
            
            return "Aqui hago registro en base datos"


        '''
        print(request.form)
        coinfrom = request.form.get("coinFrom")
        cointo = request.form.get("coinTo")
        print(f"Coin from {coinfrom} coin to {cointo}")
        rate = getExchangeEur(APIKEY,coinfrom)
        print(f"The exchange is: {rate}")
        cambio = changeCrypto(APIKEY,fromq,coinfrom,cointo)
        fromq = request.form.get("fromQ")
        fromq = float(fromq)
        print(f"el valor introducido en fromQ es: {fromq}")
        fromto = request.form.get("fromTo")
        print(f"el valor introducido en formTo es: {fromto}")
        unitprice = (fromq / cambio)
        hora = now.time()
        fecha = now.date()
        print(hora)
        print(fecha)
        '''

@app.route("/status")
def estado():

    suma = sumFrom("EUR")   
    rec = sumTo("EUR")  
    valor = sumFrom("EUR") - sumTo("EUR")

    '''
    valores = []
    criptos = cryptoFrom()
    for i in criptos:  
        value = getExchangeEur(APIKEY,i)
        valores.append(value)
    '''
    


    return render_template("status.html",invertido=suma,recuperado = rec, valorcompra = valor, page = "/status")