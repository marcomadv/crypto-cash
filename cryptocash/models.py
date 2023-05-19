import sqlite3
import requests


########################## BBDD ################################

def view_all():
    con = sqlite3.connect("data/movimientos.sqlite") # conectar con base de datos
    cur = con.cursor() #cursor para poder ejecutar las querys

    res = cur.execute("select * from tabla;")  #query o peticion a la base de datos

    filas = res.fetchall() #(1,2023-05-05,sueldo,1600)
    columnas = res.description #columnas(id,0,0,0,0,0)

    #objetivo crear una lista de diccionario con filas y columnas
    lista_diccionario = []
    
    for f in filas:
        diccionario = {}
        posicion = 0
        for c in columnas:
            diccionario[c[0]]= f[posicion]
            posicion += 1
        lista_diccionario.append(diccionario)

    con.close() #cerramos la conexion 
    return lista_diccionario

def insert(registroForm):
    con = sqlite3.connect("data/movimientos.sqlite")
    cur = con.cursor()
    res = cur.execute("INSERT INTO tabla(date,time,moneda_from,cantidad_from,moneda_to,cantidad_to) VALUES(?,?,?,?,?,?)", registroForm) #hacer insert en base datos de los datos añadidos en formulario
    
    con.commit() #validacion de registros
    con.close() #cierre de conexion

def coinsFrom(): #monedas from
    con = sqlite3.connect("data/movimientos.sqlite")
    con.row_factory = lambda cursor, row: row[0]
    cur = con.cursor()
    res = cur.execute("SELECT DISTINCT moneda_from from tabla") 
    datos = res.fetchall()
    con.close()
    return datos

def sumFrom(moneda): # suma de monedas from
    con = sqlite3.connect("data/movimientos.sqlite")
    cur = con.cursor()
    res = cur.execute(f"SELECT sum (cantidad_from) from tabla where moneda_from='{moneda}'")
    resultado = res.fetchall()
    con.close()
    return resultado

def sumTo(moneda):
    con = sqlite3.connect("data/movimientos.sqlite")
    cur = con.cursor()
    res = cur.execute(f"SELECT sum (cantidad_to) from tabla where moneda_to='{moneda}'")
    resultado = res.fetchall()
    con.close()
    return resultado

#darle una vuelta a esto, no funciona por que los datos son listas
def balanceCrypto(moneda):
    op1 = sumFrom(moneda)
    op1 = float(op1)
    op2 = sumTo(moneda)
    op2 = float(op2)
    resultado = op1 - op2
    return resultado
    

    



############################## API #########################

def getAllRates(apikey,moneda=""): # todos los rates de esta moneda
    r = requests.get(f"https://rest.coinapi.io/v1/exchanrate/{moneda}?apikey={apikey}") 
    datos = r.json()
    return datos

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
    cambio = int(rate)* q
    return cambio


'''
def getAllCoins(apikey):

    lista_criptos = []
    lista_no_criptos = []

    r = requests.get(f"https://rest.coinapi.io/v1/assets/?apikey={apikey}")

    if r.status_code != 200:
        raise Exception("Error en consulta codigo de error:{}".format(r.status_code))
    
    lista_general = r.json() #16379 registros


    for item in lista_general:
        if item["type_is_crypto"] == 1:
            lista_criptos.append(item["asset_id"])
        else:
            lista_no_criptos.append(item["asset_id"])


class Exchange: 
    def __init__(self, cripto):
        self.moneda_cripto = cripto
        self.rate = None
        self.status_code = None
        self.time = None
    def getExchange(self, apikey):
        r = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{self.moneda_cripto}/EUR?apikey={apikey}")
        respuesta = r.json()
        self.status_code = r.status_code
        if r.status_code == 200:
            self.rate = respuesta['rate']
            self.time = respuesta['time']
        else:
            print(f"status: {r.status_code}, error: {respuesta['error']}")
'''