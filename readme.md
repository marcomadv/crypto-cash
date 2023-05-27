# Aplicación Web Tradeo con criptomonedas

- Programa hecho en python con el framework flask, App web para compra y tradeo de criptomonedas.
- Todos los valores de las monedas introducidas se obtienen directamente de la Api que nos proporciona;

    https://www.coinapi.io


# Instalación
- crear un entorno en python y ejecutar el comando.
- activación del entorno:
```
source "nombre entorno"/bin/activate
```
- instalacion de requerimientos de la App:
```
pip install -r requirements.txt
```
la libreria utilizada en flask https://flask.palletsprojects.com/en/2.2.x/

# Ejecucion del programa
- inicializar el servidor de flask
- en mac: ```export FLASK_APP=main.py```
- en windows: ```set FLASK_APP=main.py```

# Otra opción de ejecucion (recomendada)
- instalar
  ```pip install python-dotenv```
- crear un archivo .env y dentro agregar lo siguiente:
``` FLASK_APP=main.py```
``` FLASK_DEBUG=True ```
- por ultimo para lanzar la App ejecutamos el siguiente comando en el terminal:
``` flask run ```
# Comando para ejecutar el servidor:
```flask --app main run```
# Comando para ejecutar el servidor en otro puerto diferente por default es el 5000
```flask --app main run -p 5002```
# Comando para ejecutar el servidor en modo debug, para realizar cambios en tiempo real
```flask --app main --debug run```

# Consumo de los recursos de la Api

- Para obtener valores reales y que la App web funcione de manera satisfactoria, deberemos crear una Key totalmente gratuita en la web ; https://www.coinapi.io , introduciendo nuestro correo electronico.

- Posterior a la creacion de la api, deberemos agregarla en el fichero ```config.py``` de la App, en el apartado donde se indica, y entre comillas " " .
- Una vez realizado este paso, la App esta lista.

- Como muestra de agradecimiento por el uso de nuestra App web y para que la experiencia de usuario sea mas satisfactoria, le proporcionamos para una primera toma de contacto un ApiKey de muestra totalmente activo y valido;

    ```APIKEY= "E79C8323-4CAF-4623-99CF-09BDA5A514DE"```






*Los movimientos registrados en CryptoCash son totalmente ficticios. En ningun caso tendran repercusión en la vida real.





