def buscar_numero(array, numero):
    for i in range(len(array)):
        if array[i] == numero:
            return i + 1
    return -1

numeros = [int(input(f"Ingrese número {i+1}: ")) for i in range(10)]
numero_a_buscar = int(input("Ingrese un número a buscar: "))

posicion = buscar_numero(numeros, numero_a_buscar)
print(posicion) 