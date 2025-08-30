def registrar_visita():
    nombre = str(input("¿Cual es su nombre?: "))
    while True:
        if nombre.strip() == "":
            print("Error, el nombre no puede estar vacío.")
            nombre = str(input("¿Cual es su nombre?: "))
        elif nombre.isdigit():
            print("Error, el nombre no puede ser un número.")
            nombre = str(input("¿Cual es su nombre?: "))
        else:
            break
    edad = int(input("¿Cuantos años tiene?: "))
    while True:
        if edad <= 0:
            print("Error, la edad debe ser un número positivo.")
            edad = int(input("¿Cuantos años tiene?: "))
        else:
            break
    return nombre, edad

def mostrar_atracciones():
    print("Los precios de nuestras atracciones son:")
    print("1- Montaña rusa = 1500")
    print("2- Casa del terror = 1200")
    print("3- Carrusel = 800")

def puede_subir(edad, atraccion):
    if edad < 6:
        return atraccion == 3
    elif edad <= 12:
        return atraccion == 2 or atraccion == 3
    else:
        return atraccion == 1 or atraccion == 2 or atraccion == 3

def calcular_precio(atraccion):
    if atraccion == 1:
        return 1500
    elif atraccion == 2:
        return 1200
    elif atraccion == 3:
        return 800
    return 0

def mostrar_resumen(entrada, nombre, edad, contador_montaña, contador_terror, contador_carrusel, atraccion_elegida):
    print("Resumen:")
    print(f"¡Gracias por tu visita, {nombre}!")
    print(f"Edad: {edad}")
    print(f"Atracciones escogidas: {atraccion_elegida}")
    print(f"Total: ${entrada}")
    print(f"Cantidad de veces que se subió al Carrusel: {contador_carrusel}")
    print(f"Cantidad de veces que entró a la Casa del Terror: {contador_terror}")
    print(f"Cantidad de veces que se subió a la Montaña Rusa: {contador_montaña}")

def main():
    entrada = 0
    atraccion_elegida = ""
    contador_montaña = 0
    contador_terror = 0
    contador_carrusel = 0 
    contador_atracciones = 0

    nombre, edad = registrar_visita()
    mostrar_atracciones()

    while True:
        atraccion = int(input("¿A cuál atracción quiere ir? (1- Montaña rusa ; 2- Casa del terror ; 3- Carrusel) "))
        
        if atraccion != 1 and atraccion != 2 and atraccion != 3:
            print("Error, no es una opción válida.")
            continue

        if not puede_subir(edad, atraccion):
            if edad < 6:
                print("Solo puede ingresar al Carrusel.")
            elif edad <= 12:
                print("Solo puede pasar al Carrusel y Casa del Terror.")
            continue

        print("¡Puede pasar!")
        precio = calcular_precio(atraccion)
        entrada += precio

        if atraccion == 1:
            atraccion_elegida += "Montaña rusa, "
            contador_montaña += 1
        elif atraccion == 2:
            atraccion_elegida += "Casa del terror, "
            contador_terror += 1    
        elif atraccion == 3:         
            atraccion_elegida += "Carrusel, "
            contador_carrusel += 1  

        contador_atracciones += 1
        while True:
            repetir = input("¿Quiere subir a otra atracción? (si/no): ")
            if repetir == "si" or repetir == "no":
                break
            print("Error, por favor reponda con 'si' o 'no'.")

        if repetir == "no":
            break   

    if contador_atracciones >= 3:
        print("Tiene un descuento del 10% por subir a 3 o más atracciones")
        entrada *= 0.90
    mostrar_resumen(entrada, nombre, edad, contador_montaña, contador_terror, contador_carrusel, atraccion_elegida)

if __name__ == "__main__":
    main()