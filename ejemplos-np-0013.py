import numpy as np

califas = np.array([60, 70, 90])
print("--------- Ejemplo 1: Imprimir Califas ---------")
print(califas) # Imprime la lista de califas 
print(type(califas)) # Muestra el tipo de arreglo
print("--------- Ejemplo 0: Dimensiones de un Array ---------")
califas = np.array(60)
print(califas)
print("Dimensión :", califas.ndim)
print("--------- Ejemplo 1: Dimensiones de un Array ---------")
califas = np.array([60, 70, 90])
print(califas)
print("Dimensión :", califas.ndim)
print("--------- Ejemplo 2: Dimensiones de un Array ---------")
califas = np.array([
    [
    [60, 70, 90],
    [50,80,98]
    ]
    ])# Un arreglo de 2 dimensiones es como una tabla en Excel
print(califas)
print("Dimensión :", califas.ndim)
print("--------- Ejemplo 3: Dimensiones de un Array ---------")
califas = np.array([
    [
    [60, 70, 90],
    [50,80,98]
    ],
    [
    [60, 70, 90],
    [50,80,98]
    ]
    ])# Un arreglo de 2 dimensiones es como una tabla en Excel
print(califas)
print("Dimensión :", califas.ndim)