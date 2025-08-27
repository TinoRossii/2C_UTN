def ordenar_mayor_a_menor(numero1, numero2, numero3):
    return sorted([numero1, numero2, numero3], reverse=True)

primero = int(input("Ingrese el primer numero: "))
segundo = int(input("Ingrese el segundo numero: "))
tercero = int(input("Ingrese el tercer numero: "))
print(f"Números ordenados del mayor al menor: {ordenar_mayor_a_menor(primero, segundo, tercero)}")