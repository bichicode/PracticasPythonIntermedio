"""19/03
Bianca"""

# ------Crear un vector
from numpy import*
vector = array([3, 6, 7, 2, 8])  # ---Creación de un vector fila
print(vector)
print(type(vector))

# ---- Operaciones con Matrices

matriz1 =array([[2,3],[4,5]]) #Arreglo (matriz)
matriz2 =array([[5,2],[1,4]])
print(f"Matrices Originales\n Matriz1 \n {matriz1}\n Matriz2 \n{matriz2}")
suma = matriz1 + matriz2 #Suma de matrices
print("Suma de Matrices")
print(suma)
resta = matriz1 - matriz2 #Resta de matrices
print("Resta de Matrices\n",resta)
mul = matriz1 * matriz2 #Multiplicación (elemento con elemento)
print("Multiplicacion de Matrices \n",mul)


matrizA = array([[4,2,5],[2,8,4],[6,9,5]])
print(f"Matriz A \n {matrizA}")
#Funcion prod()
producto = prod(matrizA)
print(f"La multiplicacion de la matriz es: {producto}")
#Funcion mean()
promedio = mean(matrizA)
print(f"El promedio de la matriz es:{promedio}")
#Funcion median()
mediana = median(matrizA)
print(f"La mediana de la matriz es:{mediana}")
#Funcion sort()
matrizA2 = sort(matrizA)
print(f"Matriz Ordenada es:\n {matrizA2}")
#Funcion cumsum()
sumaacum = cumsum(matrizA)
print(f"La suma acumulada de la Matriz es:{sumaacum}")
#Funcion diagonal()
diag = diagonal(matrizA)
print(f"La diagonal de la Matriz es:{diag}")
