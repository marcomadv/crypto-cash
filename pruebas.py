from cryptocash.models import *
from cryptocash.config import APIKEY
from datetime import datetime

now = datetime.now()
'''
suma = sumFrom("EUR")
print(f"la suma de EUR es; {suma}")


resultado = balanceCrypto("EUR")
print(f"el resultado de euros disponibles es; {resultado}")

crypto = cryptoFrom()
valor = getExchangeEur(APIKEY,crypto)
print(valor)


valores = []
criptos = cryptoFrom()

for i in criptos:  
    valor = getExchangeEur(APIKEY,i)
    valores.append(valor)

for i in criptos:
    crypto1 = sumFrom(i)
    crypto2 = sumTo(i)
    print(crypto1)
    print(crypto2)
print(criptos)
'''
#prueba = changeCrypto(APIKEY,30000,'EUR','BTC')
#print(prueba)

'''  ****forma de pasar datos para el insert de la base datos****
date="2023-05-25"
time = "13:22:43"
coinfrom = "EUR"
fromq= 2000
cointo = "ETH"
fromto = 1.20

datos=[date,time,coinfrom,fromq,cointo,fromto]

insert(datos)
'''

valores = []
criptos = cryptoFrom()
valores.append(criptos)
'''
for i in criptos:  
    value = getExchangeEur(APIKEY,i)
    valores.append(value)
'''
print(valores)
print(valores[0][0])
    
    

