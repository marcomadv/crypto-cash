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
    coins = coinsFrom()
    

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
            change = changeCrypto(APIKEY,fromq1,coinfrom,cointo)

            preview={
                "coinfrom" : request.form["coinFrom"],        
                "cointo" : request.form["coinTo"],          
                "fromq" : fromq1,
                "unitprice" : rate,           
                "change" : change
            }

            return render_template("purchase.html",coinfrom =request.form["coinFrom"],cointo=request.form["coinTo"],fromq=fromq1,pu=unitprice,change=change, page="/purchase")
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

            '''
            coinfrom = request.form.get("coinFrom")        
            cointo = request.form.get("coinTo")
            rate = getExchangeEur(APIKEY,cointo)          
            fromq = request.form.get("fromQ")
            fromq = float(fromq)
            unitprice = rate   #precio unitario de la crypto ( si se divide el Qfrom / rate , da lo mismo que Qto)           
            change = changeCrypto(APIKEY,fromq,coinfrom,cointo)
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