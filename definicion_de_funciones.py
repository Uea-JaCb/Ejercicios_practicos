# Desarrollar una función en Python que calcule la temperatura promedio de una ciudad durante un período de tiempo.
# La función debe ser capaz de manejar datos de temperaturas de múltiples ciudades y semanas.
# y recibir estos datos como parámetros para calcular la temperatura promedio de cada ciudad.

# Lista de nombres de las ciudades
ciudades = ["Guayaquil", "Manabí", "Esmeraldas"]

# Matriz 3D: [ciudades][semanas][días]
temperaturas = [
    [  # Ciudad de Guayaquil
        [28, 29, 27, 30, 31, 29, 28],  # Semana 1
        [29, 30, 28, 31, 32, 30, 29],  # Semana 2
        [27, 28, 26, 29, 30, 28, 27],  # Semana 3
        [30, 31, 29, 32, 33, 31, 30]   # Semana 4
    ],
    [  # Ciudad de Manabí
        [26, 27, 25, 28, 29, 27, 26],  # Semana 1
        [27, 28, 26, 29, 30, 28, 27],  # Semana 2
        [25, 26, 24, 27, 28, 26, 25],  # Semana 3
        [28, 29, 27, 30, 31, 29, 28]   # Semana 4
    ],
    [  # Ciudad de Esmeraldas
        [24, 25, 23, 26, 27, 25, 24],  # Semana 1
        [25, 26, 24, 27, 28, 26, 25],  # Semana 2
        [23, 24, 22, 25, 26, 24, 23],  # Semana 3
        [26, 27, 25, 28, 29, 27, 26]   # Semana 4
    ]
]

def promedio_ciudad(temperaturas, ciudades): #Calcula y muestra la temperatura promedio de cada ciudad.
    for i in range(len(ciudades)):
        ciudad = ciudades[i]
        datos_ciudad = temperaturas[i]
        # Aplanar la lista de temperaturas para la ciudad usando lista por comprensión
        temperaturas_totales = [dia for semana in datos_ciudad for dia in semana]
        promedio = sum(temperaturas_totales) / len(temperaturas_totales) # Calcular el promedio total de la ciudad
        print(f"La temperatura promedio en la ciudad de {ciudad} durante el mes es: {promedio:.2f}° Celcius") # Mostrar el resultado con dos decimales

# Llamar a la función con los datos proporcionados
promedio_ciudad(temperaturas, ciudades)