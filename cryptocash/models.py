import sqlite3
import requests



                ########################## DATABASE ################################

def view_all():
    con = sqlite3.connect("data/movimientos.sqlite") 
    cur = con.cursor() 

    res = cur.execute("select * from tabla;") 
    filas = res.fetchall() 
    columnas = res.description 

    #lista de diccionario con filas y columnas
    lista_diccionario = []
    
    for f in filas:
        diccionario = {}
        posicion = 0
        for c in columnas:
            diccionario[c[0]]= f[posicion]
            posicion += 1
        lista_diccionario.append(diccionario)

    con.close() 
    return lista_diccionario

def insert(datosForm):
    con = sqlite3.connect("data/movimientos.sqlite")
    cur = con.cursor()
    res = cur.execute("INSERT INTO tabla(date,time,moneda_from,cantidad_from,moneda_to,cantidad_to) VALUES(?,?,?,?,?,?)", datosForm)
    
    con.commit()
    con.close() 

def coinsFrom(): #monedas from
    con = sqlite3.connect("data/movimientos.sqlite")
    con.row_factory = lambda cursor, row: row[0]
    cur = con.cursor()
    res = cur.execute("SELECT DISTINCT moneda_from from tabla") 
    datos = res.fetchall()
    con.close()
    return datos

def sumFrom(moneda): #suma de la moneda que le indiques en from
    con = sqlite3.connect("data/movimientos.sqlite")
    con.row_factory = lambda cursor, row: row[0]
    cur = con.cursor()
    res = cur.execute(f"SELECT sum (cantidad_from) from tabla where moneda_from='{moneda}'")
    resultado = res.fetchall()
    con.close()
    if resultado[0] == None:
        return 0
    return float(resultado[0])

def sumTo(moneda): #suma de la moneda que le indiques en to
    con = sqlite3.connect("data/movimientos.sqlite")
    con.row_factory = lambda cursor, row: row[0]
    cur = con.cursor()
    res = cur.execute(f"SELECT sum (cantidad_to) from tabla where moneda_to='{moneda}'")
    resultado = res.fetchall()
    con.close()
    if resultado[0] == None:
        return 0
    return float(resultado[0])

def sumFromCryptos(): #suma de cryptos en from
    con = sqlite3.connect("data/movimientos.sqlite")
    con.row_factory = lambda cursor, row: row[0]
    cur = con.cursor()
    res = cur.execute("SELECT sum (cantidad_from) from tabla where moneda_from != 'EUR'")
    resultado = res.fetchall()
    con.close()
    return float(resultado[0])

def sumToCryptos(): #suma de cryptos en to
    con = sqlite3.connect("data/movimientos.sqlite")
    con.row_factory = lambda cursor, row: row[0]
    cur = con.cursor()
    res = cur.execute("SELECT sum (cantidad_to) from tabla where moneda_to != {'EUR'}")
    resultado = res.fetchall()
    con.close()
    return float(resultado[0])

def cryptoFrom(): #moneda crypto en from
    con = sqlite3.connect("data/movimientos.sqlite")
    con.row_factory = lambda cursor, row: row[0]
    cur = con.cursor()
    res = cur.execute("SELECT moneda_from from tabla where moneda_from != 'EUR'")
    resultado = res.fetchall()
    con.close()
    return resultado



                ############################## API REST #################################


def getAllRates(apikey,moneda=""): # todos los rates de esta moneda
    r = requests.get(f"https://rest.coinapi.io/v1/exchanrate/{moneda}?apikey={apikey}") 
    datos = r.json()
    return datos

def getExchangeEur(apikey, crypto): #valor de una cripto en EUR
    r = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{crypto}/EUR?apikey={apikey}")
    datos = r.json()
    rate = datos['rate']
    return float(rate)

def getExchange(apikey,crypto,crypto2): #valor de una cripto o moneda en otra cripto o moneda
    r = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{crypto}/{crypto2}?apikey={apikey}")
    datos = r.json()
    rate = datos['rate']
    return rate

def purchaseCrypto(eur,crypto): #cuanto valor se puede comprar de esa cripto con 'X' EUR.
    rate = getExchange(crypto)
    total = eur / rate
    return total
    
def changeCrypto(apikey,q,crypto1, crypto2): # Funcion docu API, cambiar valor de una cripto comprada por el de otra cripto
    r = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{crypto1}/{crypto2}?apikey={apikey}")
    datos = r.json()
    rate = datos['rate']
    cambio = float(rate)* q
    return cambio

