"""
import pandas as pd

dato = pd.read_csv('techogar.csv', header=0, encoding='latin-1', on_bad_lines='skip')
# agregue latin porque sino no abre
# agregue skip pandas.errors.ParserError: Error tokenizing data. C error: Expected 1 fields in line 15, saw 3

print(dato)

print(dato[Computadora])  # KeyError: 'Computadora'



Abre el archivo 

;Anio ;Computadoras; Internet  ;Television ;Cable ;Telefono
0   0;2001;117772;62212087;91897078;13529983;40331515         
1   1;2002;15207573;7455098;93592413;15375804;4535...  

pero manda 
KeyError: 'Computadoras'


-*- coding: utf-8 -*-

import pandas as pd

dato = pd.read_csv('techogar.csv', header=0)
print(dato.sort_values(by="Telefono"))
print(dato.sort_values(by="Telefono", ascending=False))

KeyError: 'Telefono'


# -------------------------------------------------------------------------------------

import pandas as pd

clientes = {
    'nombre': ['Javier', 'Rita', 'Alicia'],
    'edad': [34, 30, 16],
    'lugar': ['Nata', 'David', 'Capira']
}
dfObj = pd.DataFrame.from_dict(clientes, orient='index')
dfObj = dfObj.transpose()
print(dfObj)
dfObj.to_excel('clientes.xlsx')

# Corre bien
# ---------------------------------------------------------------------

import pandas as pd
data = {'nombre': ['Sigrid', 'Joe', 'Theodoric', 'Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
 'apellido': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
 'edad': [27, 31, 36, 53, 48, 36, 40, 34],
 'pago_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
 'pago_2': [8.06, "?", 5.90, "?", "?", 7.48, 4.37, "?"]}

df = pd.DataFrame(data, columns=['nombre', 'apellido', 'edad', 'pago_1', 'pago_2'])

print(df)

df.to_excel('PagosClientes.xlsx', sheet_name='Pagos')

#  Corre bien

# ---------------------------------------------------------------------

import pandas as pd
df = pd.DataFrame([[11, 21, 31], [12, 22, 32], [31, 32, 33]],
 index=[1, 2, 3], columns=['Norte', 'Sur', 'Este'])

print(df)
df.to_excel('clientesNuevos.xlsx')

#  Corre bien

# ---------------------------------------------------------------------


import pandas as pd
nombres = ['Katie', 'Nik', 'James', 'Evan']
edad = [32, 32, 36, 31]
sucursal = ['London', 'Toronto', 'Atlanta', 'Madrid']
zipped = list(zip(nombres, edad, sucursal))
df = pd.DataFrame(zipped, columns=['Nombre', 'Edad', 'Sucursal'])
print(df)
df.to_excel('ClientesExterior.xlsx', sheet_name='Clientes')

#  Corre bien

# ---------------------------------------------------------------------

"""

import pandas as pd

diccionario = {
    'Nombre': ['Bill', 'Peter', 'Julie', 'David'],
    'Edad': [26, 50, 25, 45],
    'Sucursal': ['Miami', 'Los Angeles', 'New York', 'Orlando']
}
df = pd.DataFrame(diccionario)

print(df)

df.to_excel('ClientesVIP.xlsx', sheet_name='VIP')

# Corre bien
