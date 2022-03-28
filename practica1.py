"""19/03/2020"""

a = 5
b = 0
try:
    c = a/b
except ZeroDivisionError:
    print("No se puede realizar la división")

# ----------------------------------------------------

try:
    d = 2 + "Bienvenidos "
except TypeError:
    print("Problema de tipos!")

# ----------------------------------------------------
""" -----------------------------------Comentando para poder probar los otros ejemplos
while True:
    try:
        x = int(input("Por favor ingrese un número: "))
        break
    except ValueError:
        print("Oops! No es válido. Intente nuevamente...")

# ------------------------------------------------------
"""


try:
    # Se fuerza excepción
    x = 2/0
except:
    print("Entra en except, ha ocurrido una excepción")
else:
    print("Entra en el else, no ha ocurrido ninguna excepción")
finally:
    print("Entra en finally, se ejecuta el bloque finally")

# -----------------------------------------------------------------
""" -----------------------------------Comentando para poder probar los otros ejemplos

mi_lista = ["Python", "C", "C++", "JavaScript"]
buscar_ind = int(input("Ingrese el indice a buscar:"))
try:
    print(mi_lista[buscar_ind])
except IndexError:
    print("Lo siento, el indice esta fuera de rango")
"""
# -------------------------------------------------------------
""" ------------------------------------Comentado para probar el siguiente problema
mi_lista = ["Python", "C", "C++", "JavaScript"]
while True:
    try:
        buscar_ind = int(input("Ingrese el indice a buscar:"))
        break
    except ValueError:
        print("Valor Invalido...Intente nuevamente")
    except IndexError:
        print("Lo siento, el indice esta fuera de rango")
print(mi_lista[buscar_ind]"""

# ----------------------------------------------

mi_dict = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}
buscar_clave = input("Ingrese la clave a buscar:")
try:
    print(mi_dict[buscar_clave])
except KeyError:
    print(f"¡Lo siento, no es una clave valida!")
