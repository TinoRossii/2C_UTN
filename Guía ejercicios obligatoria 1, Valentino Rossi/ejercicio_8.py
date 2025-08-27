def calcular_edad(año_nacimiento):
    año_actual = 2025
    return año_actual - año_nacimiento
año_naci = int(input("Ingrese su año de nacimiento: "))
edad = calcular_edad(año_naci)
print(f"Tenes {edad} años.")  