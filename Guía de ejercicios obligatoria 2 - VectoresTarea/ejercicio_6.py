vec_numeros = [0] * 7
i = 0

for i in range(len(vec_numeros)):
    vec_numeros[i] = int(input("Ingrese numero: "))

max_num = vec_numeros[0]
posicion = 0

for i in range(len(vec_numeros)):
    if vec_numeros[i] > max_num:
        max_num = vec_numeros[i]
        posicion = i
print(f"El numero mayor es: {max_num} y está en la posicion {posicion+1}")