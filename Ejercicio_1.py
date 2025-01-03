# Pedimos al usuario que ingrese la edad de Juan
# Este es el valor que usaremos para calcular las edades de los demás
edad_juan = int(input("Ingrese la edad de Juan: "))
# Calculamos la edad de Alberto
# Según el enunciado, Alberto tiene 2/3 de la edad de Juan
edad_alberto = (2 / 3) * edad_juan
# Calculamos la edad de Ana
# Según el enunciado, Ana tiene 4/3 de la edad de Juan
edad_ana = (4 / 3) * edad_juan
# Calculamos la edad de la mamá
# La edad de la mamá es la suma de las edades de Juan, Alberto y Ana
edad_mama = edad_juan + edad_alberto + edad_ana
# Utilizamos :.0f para mostrar los números sin decimales, como enteros
print("Las edades son:")
print(f"Alberto: {edad_alberto:.0f}")
print(f"Juan: {edad_juan}")
print(f"Ana: {edad_ana:.0f}")
print(f"Mamá: {edad_mama:.0f}")
