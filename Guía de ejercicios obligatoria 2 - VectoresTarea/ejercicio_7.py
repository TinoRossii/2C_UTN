vec_numeros = [0] * 6
i = 0

for i in range(len(vec_numeros)):
    vec_numeros[i] = int(input("Ingrese numero: "))

print("Numeros invertidos:", vec_numeros[::-1])