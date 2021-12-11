numero1=10
numero2=30

resultado = numero1 + numero2

print(resultado)
print('El resultado es:', resultado)
print('El resultado es: ',resultado,)
print(f'El resultado es: {resultado}')

print('El resultado es {} y nada más' .format(resultado))

resultado = numero1 - numero2
resultado = numero1 * numero2
resultado = numero1 / numero2

print('{:.3f}'.format(resultado))
print(f'{resultado:.1f}')

# modulo
resultado = numero1 % numero2
print('El modulo es:', resultado)

# el cociente
resultado = numero1 // numero2
print('el cociente es: ',resultado)