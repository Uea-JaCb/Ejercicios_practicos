#Crear una matriz 3D para temperaturas
#Calcular promedios por ciudad y semana
#Mostrar los resultados en pantalla

# Lista de ciudades para el ejercicio práctico
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

# Iterar sobre las ciudades y sus datos usando índices
for i in range(len(ciudades)):
    ciudad = ciudades[i]
    datos_ciudad = temperaturas[i]
    print(f"\nPromedios de temperaturas en la ciudad de {ciudad}:")
    for j in range(len(datos_ciudad)):
        datos_semana = datos_ciudad[j]
        promedio = sum(datos_semana) / 7 #Suma los valores de las temperaturas de los días de la semana en cada ciudad y los dívide para el número total de días
        print(f"  Semana {j + 1}: {promedio:.2f}°C") #Muestra el promedio de la temperatura semanal solo con dos decimales)