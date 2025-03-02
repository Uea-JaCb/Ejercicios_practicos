#Programa 1: Búsqueda en Arreglo Multidimensional
#Instrucciones
#Crea un nuevo proyecto en PyCharm y un archivo Python para este programa.
#Escribe un programa que incluya una matriz bidimensional (puede ser una matriz pequeña de 3x3) con valores numéricos.
#Implementa una función que realice una búsqueda en la matriz para encontrar un valor específico que definas.
#Muestra un mensaje que indique si el valor se encontró o no, y muestra su posición en la matriz si se encontró.

# Establecer la matriz de búsqueda 3x3
matriz_busqueda = [
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
]

def busqueda (matriz_busqueda, valor):
    for i in range(len(matriz_busqueda)):
        for j in range(len(matriz_busqueda[i])):
            if matriz_busqueda[i][j] == valor:
                return i, j  # Retorna la posición (fila, columna)
    return None

# valor que se buscará en la matriz
valor_a_buscar = int(input("Digite el valor que desea buscar: "))

# Proceso de búsqueda en la matriz
resultado_obtenido = busqueda(matriz_busqueda, valor_a_buscar)

# Presenta el resultado de la búsqueda
if resultado_obtenido:
    print(f"El valor {valor_a_buscar} fue hallado en la posición {resultado_obtenido}")
else:
    print(f"El valor {valor_a_buscar} no se halló en la matriz de búsqueda.")