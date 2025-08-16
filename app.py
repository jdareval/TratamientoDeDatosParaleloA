#Archivo con el codigo para la API el cual controlara las consultas que se realicen a la 
#API 
#Importar todas las librerias necesarias  
from flask import Flask, jsonify, request

#Nombre de la app
app = Flask(__name__)

#Declarador de la ruta
@app.route('/')
def home(): #esta sección deo codigo define la casa el home donde se inica la API
    return jsonify ({'message': 'Bienvenido a la API de base - Tratamiento de Datos Paralelo A'})

#esta sección es donde se envia información a la API
@app.route('/api/sumar', methods=['POST']) # NUESTRA API LO QUE HACE ES SUMAS
def sumar():
          data = request.get_json() #RECIBIRLO EN FORMATO JSON
          a =data.get('a')
          b = data.get('b')
          if a is None or b is None: #define si uno de los datos que se han enviado falta
                return jsonify ({'error': 'Parametros a y b requeridos'}), 400 #devuelve un error
          return jsonify ({'resultado': a + b})

#envia información de la API LA VERSION Y DESCRIPCION Y AUTOR 
@app.route('/api/info', methods=['GET'])
def info():
      return jsonify({
            'nombre': 'Microservicio BAse -  Tratamiento de Datos PAralelo A',
            'version': '1.0.0',
            'descripcion': 'Este microservicio realiza operaciones basicas de suma y proporciona información del servicio.',
            'autor': 'Julio Arévalo',
      })

# para correr un programa se necesita un declarador y este seria el declarador de las API
if __name__ == '__main__':
    #Datos de prueba
    app.run(debug=True, host='0.0.0.0', port=5000)