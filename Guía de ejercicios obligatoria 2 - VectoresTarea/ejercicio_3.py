vec_decimal = [0.0] * 6
decimal = 0.0
suma_decimales = 0.0

for i in range(len(vec_decimal)):
    vec_decimal[i] = float(input("Ingrese un numero decimal: "))

for i in range(len(vec_decimal)):
    suma_decimales += vec_decimal[i]

promedio_decimales = suma_decimales / len(vec_decimal)
print(f"El promedio es: {promedio_decimales}")