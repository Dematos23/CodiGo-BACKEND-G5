# variable numerica
numero =10
numero2 = 10.5



nombre ="Diego"
apellido = 'Matos'

html='''<html>
<P>
<P>
'''

fecha = 0

print('holaaa :)')
print(type(nombre))
print(type(numero))

soltero=True
calor=False
print(type(soltero))

# Variables que tienen varios valores
# arreglos 
edades = [10, 12, 40, 60, 'Eduardo', 14,5, False, [1,2]]

# JSON
curso = {
    'nombre': 'Backend',
    'dificultad': 'Dificil',
    'skills': [
        {
            'nombre':'Base de datos',
            'nivel': 'Intermedio'
        },
        {
            'nombre': 'ORM',
            'nivel': 'Avanzado'
        }
    ]
}

print(edades[2:-1])

print(curso['skills'][1]['nombre'])

personas = [{
    'nombre': 'Eduardo',
    'nacionalidad': 'peruano',
    'hobbies':[
        {
            'nombre': 'Volar drones',
            'experiencia': '2 años'
        },{
            'nombre':'Programar',
            'experiencia': '1 mes'
        }
    ]
},{
    'nombre': 'Juliana',
    'nacionalidad': 'colombiana',
    'hobbies':[
        {
            'nombre': 'Montar bici',
            'experiencia': '4 años'
        },{
            'nombre':'Bases de datos',
            'experiencia': '8 mes'
        }
    ]
}]

print(personas[0]['nacionalidad'])
print(personas[1]['hobbies'])
print(personas[0]['hobbies'][1]['experiencia'])