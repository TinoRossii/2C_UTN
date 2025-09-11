vec_numero = [0] * 8
i = 0
contador_cien = 0

for i in range(len(vec_numero)):
    vec_numero[i] = int(input("Ingrese numero: "))

for i in range(len(vec_numero)):
    if vec_numero[i] > 100:
        contador_cien += 1
print(f"La cantidad de numeros mayores a 100 es: {contador_cien}")