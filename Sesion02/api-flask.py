from logging import debug
from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def inicio():
    
    print(request.method)
    if request.method == 'POST':
        
        print(request.get_json())
        data = request.get_json()
        if(data.get('nombre')):
            nombre = data['nombre']
            return 'Hola, {}!'.format(nombre)
        else:
            return 'Necesito la informacion', 400
    elif request.method == 'GET':
        return 'Bienvenido a mi API de Productos', 200

if __name__ == '__main__':
    app.run(debug=True)

