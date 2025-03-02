#Programa 2: Ordenación de Arreglo Multidimensional
#Crea un nuevo proyecto en PyCharm y un archivo Python para este programa.
#Escribe un programa que incluya una matriz bidimensional con valores numéricos (puede ser una matriz pequeña de 3x3).
#Implementa una función que ordene una fila específica de la matriz en orden ascendente utilizando un algoritmo de ordenación de tu elección (por ejemplo, Bubble Sort o QuickSort).
#Muestra la matriz original y la matriz con la fila ordenada.

# Establecer los valores de la matriz 3x3
matriz_ordenacion = [
    [3, 9, 6],
    [12, 18, 15],
    [27, 21, 24]
]

def ordenacion(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambiar elementos


# Presentar los datos de la matriz original
print("Matriz original:")
for fila in matriz_ordenacion:
    print(fila)

# Seleccionar la fila a ordenar
fila_a_ordenar = 0
ordenacion(matriz_ordenacion[fila_a_ordenar])

# Presentar la matriz luego de la ordenación
print("\nMatriz después de ordenar la fila 2:")
for fila in matriz_ordenacion:
    print(fila)