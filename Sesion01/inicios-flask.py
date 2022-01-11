from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'Bienvenido a mi API'

@app.route('/bienvenida')
def bienvenida():
        return 'Te doy la bienvenida a mi API'

if __name__ == '__main__':
    app.run(debug=True, port=3000)