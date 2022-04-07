"""class Aritmetica:
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB


try:
    num1 = int(input('Introducir el primer número:'))
    try:
        num2 = int(input('Introducir el segundo número:'))
        aritmetica1 = Aritmetica(num1, num2)
        print(f'Suma: {aritmetica1.sumar()}')
    except:
        print('Introducir un valor entero')
except:
    print('Introducir un valor entero')

# Introducir el primer número:20
# Introducir el segundo número:21
# Suma: 41


# ----------------------------------------------------------------------
# Clase Imc para calcular el Indice de Masa Corporal


class Imc:
    def __init__(self, pes, est):
        self.peso = pes
        self.estatura = est

    def calculaIndice(self):

        return self.peso / (self.estatura ** 2)


try:
    peso = float(input('Introducir el peso en kilogramos:'))

    try:
        estatura = float(input('Introducir la estatura en metros:'))
        imc1 = Imc(peso, estatura)
        print(f'IMC: %.2f' % imc1.calculaIndice())

    except:
        print('Introducir un valor flotante')

except:
    print('Introducir un valor flotante')

# Introducir el peso en kilogramos:60
# Introducir la estatura en metros:1.77
# IMC: 19.15



# ----------------------------------------------------------------------

import os


# Clase Empleado para consultar las generales y modificar el cargo

class Empleado():
    def __init__(self, edad, nombre, profesion):
         self.edad = edad
         self.nombre = nombre
         self.profesion = profesion
         self.posicion = "Desempleado"

    def consultargenerales(self):
        print("******CONSULTA GENERALES DEL EMPLEADO******")
        print("Nombre:",self.nombre)
        print("Edad:", self.edad)
        print("Profesion:", self.profesion)
        print("Cargo:",self.posicion)
        print("")

    def actualizacargo(self, posicion):
         self.posicion = posicion
         self.consultargenerales()


nombre = input("Ingresa el nombre del empleado:")
edad = int(input("Ingrese la edad del empleado:"))
profesion = input("Ingrese la profesion del empleado:")

emp = Empleado(edad, nombre, profesion)  # Instancia

# Llamamos al método

emp.consultargenerales()

print("******ACTUALIZACION DEL CARGO******")
posicion = input("Ingrese el cargo a desempeñar en la empresa:")
print("")
emp.actualizacargo(posicion)
os.system("pause")

#Ingresa el nombre del empleado:Lala Gomez
#Ingrese la edad del empleado:56
#Ingrese la profesion del empleado:Ing Industrial
#******CONSULTA GENERALES DEL EMPLEADO******
#Nombre: Lala Gomez
#Edad: 56
#Profesion: Ing Industrial
#Cargo: Desempleado

#******ACTUALIZACION DEL CARGO******
#Ingrese el cargo a desempeñar en la empresa:Supervisor de Planta

#******CONSULTA GENERALES DEL EMPLEADO******
#Nombre: Lala Gomez
#Edad: 56
#Profesion: Ing Industrial
#Cargo: Supervisor de Planta

#Presione una tecla para continuar . . . d



# ----------------------------------------------------------------------

# En la Librería Parra las personas que van a pagar
# una caja un número que les indicará el valor
# del descuento que tendrán sobre el total de su compra.
# Tomar en cuenta lo siguiente:
# 1: 20%
# 2: 15%
# 3: 18%


# Clase Libreria para el calculo de descuento por compra

class Libreria:

    def __init__(self, compra, numero):
        self.compra = compra
        self.numero = numero

    def calculatotal(self):
        match numero:
            case 1:
                descuento = self.compra * 0.20
                total = self.compra - descuento
            case 2:
                descuento = self.compra * 0.15
                total = self.compra - descuento
            case 3:
                descuento = self.compra * 0.18
                total = self.compra - descuento

        return total, descuento


compra = float(input('Introducir el total de la compra:'))

numero = int(input('Introducir el numero sacado:'))

lib = Libreria(compra, numero)

tot, descu = lib.calculatotal()

print("Monto de la Compra: %.2f" % compra)
print("Desc según Número (1)-20% (2)-15% (3)-18%:", numero)
print("Descuento Aplicado: %.2f" % descu)
print(f'El total a pagar es: %.2f' % tot)

# Introducir el total de la compra:100
# Introducir el numero sacado:1
# Monto de la Compra: 100.00
# Desc según Número (1)-20% (2)-15% (3)-18%: 1
# Descuento Aplicado: 20.00
# El total a pagar es: 80.00

"""


# ----------------------------------------------------------------------

# El sistema de vigilancia del transporte público entrega
# una lista de longitud n con el código de placa de los
# vehículos que invaden el carril exclusivo de este sistema
# de transporte de pasajeros. La lista puede contener códigos
# repetidos que corresponden a vehículos que cometieron esta
# infracción más de una vez. La multa por una infracción es $100,
# por dos infracciones el valor se duplica, por tres se triplica, etc.
# Escriba un programa que lea la lista de códigos y muestre para cada uno,
# la cantidad de infracciones cometidas y el total de la multa a pagar.


#  Clase Infraccion para calcular el monto de la multa a pagar

class Infraccion:

    def __init__(self, infra):
        self.infraccion = infra

    def ingresadatos(self):
        resp = 's'
        while resp.lower() == 's':
            infraccion.append(input("Ingrese la placa del vehiculo:"))
            resp = input("Desea registrar otra placa s/n:")
        return infraccion

    def calculaInfraccion(self):
        for i in infraccion:
            if i not in multadas:
                cuenta = infraccion.count(i)
                multadas.append(i)
                cmultadas.append(cuenta)
        return multadas, cmultadas


infraccion = []

multadas = []

cmultadas = []

infra = Infraccion(infraccion)

infra.ingresadatos()

multadas, cmultadas = infra.calculaInfraccion()

print("Placa\t\t Cantidad\t\t Multa ")

for i in range(len(multadas)):
    print(f"{multadas[i]}\t\t {cmultadas[i]}\t\t\t\t {cmultadas[i] * 100}")
