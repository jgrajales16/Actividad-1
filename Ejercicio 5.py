import math
# Pedimos al usuario que ingrese el radio del círculo
radio = float(input("Ingrese el radio del círculo: "))
# Calculamos el área del círculo usando la fórmula: área = pi * radioˆ2
area = math.pi * radio ** 2
# Calculamos la longitud de la circunferencia usando la fórmula: longitud = 2 * pi * radio
longitud = 2 * math.pi * radio
# Mostramos los resultados
print("El área del círculo es:", area)
print("La longitud de la circunferencia es:", longitud)
