class Persona:
    nombre = ''
    edad=0
    estatura=0.0

    def saludar(self):
        print('Hola!',self.nombre)

    def __init__(self, nombre,edad,estatura,sexo='NS/NO'):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        self.sexo = sexo

eduardo = Persona(nombre='Eduardo', edad=20, estatura=1.89)
print(eduardo.nombre)