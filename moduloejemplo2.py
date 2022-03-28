import misfunciones as funciones

print("Programa de Conversiones")

print("a. Convertir kilometros a milla")

print("b. Convertir metro a centimetros")

op = input("Introducir la opcion: ")

n1 = int(input("Introducir el valor"))

if op == 'a':
    print(funciones.milla(n1))

elif op == 'b':
    print(funciones.cen(n1))

else:
    print("Opcion incorrecta")