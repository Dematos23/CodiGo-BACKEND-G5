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

