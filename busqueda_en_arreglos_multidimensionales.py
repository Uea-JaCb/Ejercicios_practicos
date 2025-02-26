def busqueda (matriz_busqueda, valor):
    for i in range(len(matriz_busqueda)):
        for j in range(len(matriz_busqueda[i])):
            if matriz_busqueda[i][j] == valor:
                return i, j  # Retorna la posición (fila, columna)
    return None

# Establecer la matriz de búsqueda 3x3
matriz_busqueda = [
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
]

# valor que se buscará en la matriz
valor_a_buscar = int(input("Digite el valor que desea buscar: "))

# Proceso de búsqueda en la matriz
resultado_obtenido = busqueda(matriz_busqueda, valor_a_buscar)

# Presenta el resultado de la búsqueda
if resultado_obtenido:
    print(f"El valor {valor_a_buscar} fue hallado en la posición {resultado_obtenido}")
else:
    print(f"El valor {valor_a_buscar} no se halló en la matriz de búsqueda.")