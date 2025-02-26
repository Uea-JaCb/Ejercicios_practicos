def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambiar elementos

# Establecer los valores de la matriz 3x3
matriz_ordenacion = [
    [3, 9, 6],
    [12, 18, 15],
    [27, 21, 24]
]

# Presentar los datos de la matriz original
print("Matriz original:")
for fila in matriz_ordenacion:
    print(fila)

# Seleccionar la fila a ordenar
fila_a_ordenar = 0
bubble_sort(matriz_ordenacion[fila_a_ordenar])

# Presentar la matriz luego de la ordenación
print("\nMatriz después de ordenar la fila 2:")
for fila in matriz_ordenacion:
    print(fila)