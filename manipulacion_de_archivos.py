# Creamos el archivo y escribimos en el
with open("my_notes.txt", "w") as archivo:
    # Escribimos cualquier texto en el archivo
    archivo.write("Esta es la primera vez que trabajo con archivos en Python.\n")
    archivo.write("Aprendí que es importante cerrar los archivos luego de usarlos.\n")
    archivo.write("Existen varios modos de apertura de archivos ('r', 'w', 'a').\n")
    archivo.write("Con tan pocas linea de código podemos crear excelentes programas.\n")
    archivo.close()  # Cerramos el archivo luego de escribir

# Abrimos el archivo para lectura
archivo = open("my_notes.txt", "r")
# Leemos línea por línea usando readline() y un bucle while
linea = archivo.readline()
while linea:
    print(linea.strip())  # Mostramos cada línea sin el salto de línea extra
    linea = archivo.readline()
archivo.close()  # Cerramos el archivo luego de leer