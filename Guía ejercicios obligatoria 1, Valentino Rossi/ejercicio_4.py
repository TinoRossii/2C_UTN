def ordenar_mayor_a_menor(numero1, numero2, numero3):
    if numero1 >= numero2 and numero1 >= numero3:
        if numero2 >= numero3:
            return numero1, numero2, numero3
        else:
            return numero1, numero3, numero2
    elif numero2 >= numero1 and numero2 >= numero3:
        if numero1 >= numero3:
            return numero2, numero1, numero3
        else:
            return numero2, numero3, numero1
    else:
        if numero1 >= numero2:
            return numero3, numero1, numero2
        else:
            return numero3, numero2, numero1


primero = int(input("Ingrese el primer numero: "))
segundo = int(input("Ingrese el segundo numero: "))
tercero = int(input("Ingrese el tercer numero: "))

print("Números ordenados del mayor al menor:", ordenar_mayor_a_menor(primero, segundo, tercero))