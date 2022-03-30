"""
mensaje = input('Frase que desea escribir en el archivo:')
try:
    archivo = open('C:\\Users\\User\\PycharmProjects\\Intermedio\\Practicas\\Clase2\\ejemploarchivo.txt','w',encoding='utf8')
    
    archivo.write(mensaje)

    archivo.write('\nAdios')

except Exception as e:
    print(e)

finally:
    archivo.close()
"""


"""
try:
    archivo = open('C:\\Users\\User\\PycharmProjects\\Intermedio\\Practicas\\Clase2\\ejemploarchivo.txt', 'r')
    print(archivo.read(5))
    print(archivo.read(3))
    
except Exception as e:
    print(e)
    
finally:
    archivo.close()
"""

"""try:
    
    archivo = open('C:\\Users\\User\\PycharmProjects\\Intermedio\\Practicas\\Clase2\\ejemploarchivo.txt', 'r')
    
    for linea in archivo:
        print(linea)

except Exception as e:
    
    print(e)

finally:
    
    archivo.close()"""


try:

    archivo = open('C:\\Users\\User\\PycharmProjects\\Intermedio\\Practicas\\Clase2\\ejemploarchivo.txt', 'r')

    print(archivo.readlines()[0])

except Exception as e:

    print(e)

finally:

    archivo.close()

