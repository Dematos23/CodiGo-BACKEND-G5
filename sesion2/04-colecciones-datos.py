# Listas
dias=['Lunes', 'Martes','Miercoles']

# metodo para agregar un nuevo valor
dias.append('Jueves')

print(dias)
# metodo para eliminar un valor de la lista
dias.remove('Martes')
print(dias)

# dias.clear()
print(dias)

otrosDias= ['Sabado','Domingo']

diasSemana = dias + otrosDias
print(diasSemana)
# variables mutables / inmutables
lista1 = [1,2,3,4,5]

lista2 = lista1
lista3 = lista1[:]
lista1[0]=50
print(id(lista1))
print(id(lista2))
print(id(lista3))
print('La lista 1 es;',lista1)
print('La lista 2 es;',lista2)
print('La lista 3 es;',lista3)

# las variables inmutables son las variables de tipo primitivo como los INT, STR, FLOAT, BOOLEAN, DATE

CONFIGURACION = ({
        'Nombre':'API_KEY'
        'Valor':'XXXXXX.XXXX.XXXX'},
    {
        'Nombre':'Sendgrid'
        'Valor':'asdasdasdasdasdasda'
    })

CONFIGURACION = ('asdasdasdasdasdasd', 'asdasdgsfdgsdfg','123154352wcasda78sd8a')


print(CONFIGURACION[0])

print(CONFIGURACION)

persona= {
    'nombre':'Diego'
    'correo':'dematos23@gmail.com'
    'direcciones':[º1-0]

}