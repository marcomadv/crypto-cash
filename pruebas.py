from cryptocash.models import *
from cryptocash.config import APIKEY

'''
suma = sumFrom("EUR")
print(f"la suma de EUR es; {suma}")


resultado = balanceCrypto("EUR")
print(f"el resultado de euros disponibles es; {resultado}")

crypto = cryptoFrom()
valor = getExchangeEur(APIKEY,crypto)
print(valor)

'''
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



