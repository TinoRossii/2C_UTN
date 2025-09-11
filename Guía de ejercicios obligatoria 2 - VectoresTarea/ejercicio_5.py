vec_numeros = [0] * 10
i = 0

for i in range(len(vec_numeros)):
    vec_numeros[i] = int(input("Ingrese numero: "))

buscar = int(input("Ingrese numero entero a buscar: "))
encontrado = False
for i in vec_numeros:
    if i == buscar:
        encontrado = True
        print(f"El numero {buscar} está en la lista")
        break
if not encontrado:
    print("El numero no está en la lista")