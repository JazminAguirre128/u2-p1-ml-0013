import numpy as np 

print("-------- Llenar matriz de ceros --------")

matriz = np.zeros([3,5]) # 3 Filas con 5 columnas
print(matriz)

print("-------- Llenar matriz de unos --------")
matriz = np.ones([3,5])
print(matriz)

print("-------- Llenar matriz de vacios --------")
matriz = np.empty([3,5])
print(matriz)

print("-------- Llenar matriz con rangos --------")
# El primer parametro es el valor inicial
# El segundo parametro es el valor final
# El tercer parametro es el incremento
list = np.arange(0, 10, 2)
print(list)
print("-------- Llenar arreglo con rango no.2 --------")
list = np.arange(0, 10, 1)
print(list)