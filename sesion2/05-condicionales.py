# condicional IF ELSE
edad=20
edad_minima=18
print(edad>=edad_minima)

if edad>= edad_minima:
    # TODO: implementar accion cuando sea mayor de edad
    print('Eres mayor de edad, puedes ingresar')
elif edad > 15:
    print('Puedes ingresar sólo a los quinceañeros')
elif edad > 10:
    print('Puedes ingresar al zoo gratis')
else:
    print('Eres menor de edad, no puedes hacer nada')

print('Yo siempre me ejecuto')

# operador ternario
# es para devolver un valor y almacenarlo en una variable y en una sola linea de codigo
resultado = 'eres mayor de edad' if edad>=edad_minima else 'Eres menor de edad'
print(resultado)

# tengo el siguiente numero
numero = 11
# como saber si es par o impar
if numero % 2 == 0:
    print('El numero es par')
else:
    print('El numero es impar')

# luego de haber terminado con el if hacer uso del operador ternario

resultado = 'el numero es par' if numero % 2 == 0 else 'El numero es impar'
print(resultado)

persona = {
    'nombre': 'Raul',
    'nacionalidad': 'Boliviana',
    'sexo': 'M'
}

if (persona['nombre']=='Raul' and persona['nacionalidad']=='Boliviana'):
    print('Sí, Se llama ',persona['nombre'],' y su nacionalidad es peruano',persona['nacionalidad'],)
else:
    print('No, la persona es ',persona['nombre'],'y su nacionalidad es ',persona['nacionalidad'],)

# for

meses = ['Enero','Febrero','Marzo','Abril']

for mes in meses:
    if mes =='Enero':
        print('Vamos a la playa')
    print(mes)

for numero in range(5,10,12):
    print(numero)

print(int(10.6))
for numero in range(int(len(meses)/2),len(meses)):
    print(numero)


# Ejercicio
# Cuantas personas tienen más de 20 años
# qué personas tienen menos de 20 personas: Nicolas y Guillermo

personas = [
    {
    'nombre': 'Adriana',
    'edad': 25
    },
    {
    'nombre': 'Nicolas',
    'edad': 15
    },
    {
    'nombre': 'Maria',
    'edad': 23
    },
    {
    'nombre': 'Guillermo',
    'edad': 10
    }
]
# 1. Cuantas personas tienen mas de 20 años  > 2
# 2. Que personas son las que tienen menos de 20 años > Las personas son Nicolas, Guillermo
# HINT: crear una lista donde se almacenen los nombres de las personas que tienen menos de 20, un contador para contar a las personas de mas de 20


contador = 0
listaMenores = []

for persona in personas:
    if persona['edad']>=20:
        contador += 1
    else:
        listaMenores.append(persona['nombre'])

print('Hay ',contador,'mayores de 20 años')
print(listaMenores,' son las personas menores de 20 años')
