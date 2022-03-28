import convtemp as cte

print("Programa para convertir temperaturas\n a. Convertir Fahrenheit a Celsius \nb. Convertir Celcius a Fahrenheit ")

op = input("Introducir la opcion: ")

n1 = int(input("Introducir la temperatura"))

if op == 'a':
    print(cte.celcius(n1))

elif op == 'b':
    print(cte.fah(n1))

else:
    print("Opcion incorrecta")
