# Definir la función para calcular el descuento

def calcular_descuento(valor_total, porcentaje_descuento=10): # Descuento por defecto del 10%
    descuento = (porcentaje_descuento / 100) * valor_total
    return descuento

if __name__ == '__main__':
    valor1 = 120
    descuento1 = calcular_descuento(valor1)
    valor_final1 = valor1 - descuento1
    print(f"Para un valor de ${valor1}:")
    print(f"Descuento (10% por defecto): ${descuento1}")
    print(f"Valor final a pagar: ${valor_final1}")

    valor2 = 180
    descuento2 = calcular_descuento(valor2, 20) # Descuento del 20%
    valor_final2 = valor2 - descuento2
    print(f"Para un valor de ${valor2} con {20}% de descuento:")
    print(f"Descuento: ${descuento2}")
    print(f"Valor final a pagar: ${valor_final2}")