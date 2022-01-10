from datetime import datetime

nombre = input('Ingresa tu nombre')
edad = int(input('Ingresa tu edad'))
time = datetime.now().hour

if edad>=18:
    print('Puedes hacer lo que quieras! :D')
elif time>18:
    print('Debes ir a dormir')
else:
    print('Debes hacer la tarea')
