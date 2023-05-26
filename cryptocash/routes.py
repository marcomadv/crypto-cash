from cryptocash import app
from flask import render_template,request, redirect, flash
from cryptocash.models import *
from cryptocash.config import APIKEY
from cryptocash.models import *
from cryptocash.forms import MovementsForm
from time import strftime


@app.route("/")
def index():
    
    datos = view_all()
    registros = len(datos)

    
    

    return render_template("index.html", data=datos, page="/",registros = registros)

@app.route("/purchase", methods=['GET','POST'])
def compra():
    
    cryptos=["EUR","ETH","BNB","ADA","DOT","BTC","USDT","XRP","SOL","MATIC"]
    coins = coinsTo()
    coins.append("EUR")
    

    if request.method == "GET":

        datos = view_all()
        registros = len(datos)
  
        return render_template("purchase.html",monedas = coins, criptos=cryptos, registros=registros, page="/purchase")

    if request.method == "POST":

        if request.form['action'] == 'Calcular':
            
            coinfrom = request.form["coinFrom"]       
            cointo = request.form["coinTo"]
            rate = getExchangeEur(APIKEY,cointo)          
            fromq = request.form["fromQ"]
            fromq1 = float(fromq)
            unitprice = rate   #precio unitario de la crypto ( si se divide el Qfrom / rate , da lo mismo que Qto)           
            change = 0
            if coinfrom =="EUR" and cointo !="BTC": 
                flash("Con 'EUR' solo puedes hacer compra de 'BTC'")

            elif cointo =="EUR" and coinfrom !="BTC":    
                flash("Solo se pueden intercambiar por 'EUR' la criptomoneda 'BTC'")

            elif coinfrom !="EUR" and fromq1 > quantityForCrypto(coinfrom)[0]:       
                flash("No hay suficiente cantidad de la moneda seleccionada")

            else:            
                change = changeCrypto(APIKEY,fromq1,coinfrom,cointo)
            
            return render_template("purchase.html",coinfrom =request.form["coinFrom"],cointo=request.form["coinTo"],fromq=fromq1,pu=unitprice,change=change, page="/purchase")
        else:

            if request.form["Qto"] == '':

                fromq = request.form["fromQ"]
                fromq1 = float(fromq)

                flash("Debe calcular los valores antes de registro")
                return render_template("purchase.html",coinfrom =request.form["coinFrom"],cointo=request.form["coinTo"],monedas = coins, criptos=cryptos,fromq=fromq1, page="/purchase")
            else:

                date = strftime("%Y-%m-%d")
                time = strftime("%H:%M:%S")
                
                datosForm=[date,               
                            time,
                            request.form["coinFrom"],
                            request.form["fromQ"],
                            request.form["coinTo"],
                            request.form["Qto"]]

                insert(datosForm)
                
                print(request.form)
                flash("Transaccion registrada correctamente")
                return redirect("/")


@app.route("/status")
def estado():

    suma = sumFrom("EUR")   
    rec = sumTo("EUR")  
    purchaseValue = sumFrom("EUR") - sumTo("EUR")
   


    currentValue = 0
    valorescripto = cryptoValues()

    for valor in valorescripto:
        rate = getExchangeEur(APIKEY,valor[0])
        totalValue = rate * valor[1]
        currentValue += totalValue
    
    balance = currentValue - purchaseValue
    

    return render_template("status.html",invertido=suma,recuperado = rec, valorcompra = purchaseValue, estado=currentValue,balance = balance, page = "/status")