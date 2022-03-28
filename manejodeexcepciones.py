"""Manejo de Excepciones
19/03/2022"""

while True:
 try:
    n = int(input('Cantidad de datos: '))
 except ValueError:
    print('Cantidad incorrecta')
    continue
 break
s = 0
i = 0
while True:
 try:
    x = int(input('Ingrese dato: '))
 except ValueError:
    print('Dato incorrecto')
    continue
 i=i+1
 s=s+x
 if i==n:
    break
print('Suma: ',s)
