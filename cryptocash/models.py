import sqlite3
import requests


    ############################################ DATABASE ##################################################


def view_all(): #todos los datos registrados
    con = sqlite3.connect("data/movimientos.sqlite") 
    cur = con.cursor() 

    res = cur.execute("SELECT * from tabla ORDER by date DESC, time DESC") 
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


def coinsTo(): #cryptos en to
    con = sqlite3.connect("data/movimientos.sqlite")
    con.row_factory = lambda cursor, row: row[0]
    cur = con.cursor()
    res = cur.execute("SELECT DISTINCT moneda_to from tabla where moneda_to != 'EUR'") 
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


def cryptoValues(): #moneda crypto mas cantidad que poseemos
    con = sqlite3.connect("data/movimientos.sqlite")
    cur = con.cursor()
    res = cur.execute("""
        select moneda, sum (cantidad ) from (
            select moneda_from moneda, sum (cantidad_from*-1) cantidad  from tabla GROUP by moneda_from
            UNION ALL
            select moneda_to moneda, sum (cantidad_to) cantidad  from tabla GROUP by moneda_to
        )WHERE moneda != "EUR"
        group by moneda 
    """)
    resultado = res.fetchall()
    return resultado


def quantityForCrypto(crypto): #cantidad que poseemos de una crypto concreta
    con = sqlite3.connect("data/movimientos.sqlite")
    con.row_factory = lambda cursor, row: row[0]
    cur = con.cursor()
    res = cur.execute(f"""
        select sum (cantidad ) from (
            select moneda_from moneda, sum (cantidad_from*-1) cantidad  from tabla GROUP by moneda_from
            UNION ALL
            select moneda_to moneda, sum (cantidad_to) cantidad  from tabla GROUP by moneda_to
        )WHERE moneda == "{crypto}"
        group by moneda 
    """)
    resultado = res.fetchall()
    return resultado



    ################################################ API REST ###################################################


def getExchangeEur(apikey, crypto): #valor de una cripto en EUR
    r = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{crypto}/EUR?apikey={apikey}")
    datos = r.json()
    rate = datos['rate']
    return float(rate)


def changeCrypto(apikey,q,crypto1, crypto2): # Funcion docu API, cambiar valor de una cripto comprada por el de otra cripto
    r = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{crypto1}/{crypto2}?apikey={apikey}")
    datos = r.json()
    rate = datos['rate']
    cambio = float(rate)* q
    return cambio

