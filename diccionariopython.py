# 1. Crear un diccionario con información personal ficticia

informacion_personal = {
    "nombre": "Johao Caicedo",
    "edad": 30,
    "ciudad": "Esmeralda",
    "profesion": "Estudiante universitario",
}

# 2. Acceder y modificar el valor de "ciudad" se mostramos primero la ciudad original
print("Ciudad original:", informacion_personal["ciudad"])

# Cambia el valor de "ciudad" a Guayaquil
informacion_personal["ciudad"] = "Guayaquil"

# 3. Agregar una nueva clave-valor, agregaré "peso"
informacion_personal["peso"] = '73 kg'

# 4. Verifica si existe la clave "estatura" y la agrega si no existe
if "estatura" not in informacion_personal:
    informacion_personal["estatura"] = 1.68
    print("Estatura añadida al diccionario")
else:
    print("La estatura ya existía")

# 5. Eliminar la clave "profesión" del diccionario
del informacion_personal["profesion"]
print("Profesión eliminada del diccionario")

# 6. Imprimir el diccionario final
print("\nDiccionario final:")
print(informacion_personal)