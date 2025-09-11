vec_numero = [0] * 10
i = 0

for i in range(len(vec_numero)):
    vec_numero[i] = int(input("Ingrese numero: "))

suma_numeros = 0

for i in range(len(vec_numero)):
    suma_numeros += vec_numero[i]
print(f"La suma es: {suma_numeros+1}")