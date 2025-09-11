import practica.funciones as funciones

print("Bienvenidos al programa")
nombre = input("Ingrese su nombre: ")

funciones.saludar(nombre)

numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
numero3 = int(input("Numero 3: "))

resultado_promedio = funciones.promedio(numero1, numero2, numero3)

print(f"El promedio es: {resultado_promedio}")

resultado_suma, resultado_resta, resultado_multiplicación = funciones.operar(numero1, numero2)

funciones.dividir(numero1, numero2)