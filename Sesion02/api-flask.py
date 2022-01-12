from logging import debug
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app=app)

mis_productos = [{
    "nombre":"Paneton con arto bromato",
    "precio": 17.50,
    "disponible": True,
    "fecha_vencimiento": "2022-01-14"
}, {
    "nombre":"Chocolate con arta azucar",
    "precio": 6.90,
    "disponible": False,
    "fecha_vencimiento": "2021-12-30"
}]

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

@app.route('/productos', methods=['POST', 'GET'])
def productos():
    if request.method == 'GET':
        return {
            'data': mis_productos,
            'message': 'Los productos son:',
            'ok': True,
        }
    elif request.method == 'POST':
        data = request.get_json()
        mis_productos.append(data)
        return {
            'data': data,
            'message': 'Producto agregado exitosamente',
            'ok': True
        }, 201

@app.route('/producto/<int:id>', methods=['GET','PUT'])
def producto(id):
    if request.method == 'GET':
        cantidadProductos = len(mis_productos)
        if id < cantidadProductos:
            return {
            'data': mis_productos[id],
            'message': 'El producto es:',
            'ok': True,
        }
        else:
            return {
            'data': None,
            'message': 'El producto no existe',
            'ok': False,
        }, 404

    elif request.method == 'PUT':
        data = request.get_json()
        if(id < len(mis_productos)):
            mis_productos[id] = data
            return {
                'ok': True,
                'data': mis_productos[id],
                'message': 'Producto actualizado exitosamente'
            }, 201
        else:
            return{
                'ok': False,
                'data': None,
                'message': 'El producto con el id {} no existe'.format(id)
            }

if __name__ == '__main__':
    app.run(debug=True)

