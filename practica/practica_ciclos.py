print(f"Bienvenido a Pythonland!")
nombre=input("Por favor, ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))
print(f"Perfecto, los precios de nuestras atraccionnes son: Montania rusa= 1500, Casa del terror = 1200, Carrusel = 800")
entrada=0
atraccion_elegida=""
contador_montania=0
contador_terror=0
contador_carrusel=0

while True:
    atraccion = int(input("¿A cuál de las siguientes atracciones le gustaría entrar? (1-Montania rusa ; 2-Casa del terror ; 3-Carrusel) "))
    if atraccion!=1 and atraccion!=2 and atraccion!=3:
        print(f"Error, no es una atraccion valida")
        atraccion=int(input("A cual de las siguientes atracciones le gustaria entrar? (1-Montania rusa ; 2-Casa del terror ; 3-Carrusel) "))
    if atraccion not in [1, 2, 3]:
        print("Error, no es una atracción válida.")
        continue

    if edad < 6:
        if atraccion != 3:
            print("Lo siento, solo puede ingresar al Carrusel.")
            continue
    elif edad <= 12:
        if atraccion == 1:
            print("Error, usted solo puede pasar al Carrusel y Casa del Terror.")
            continue
    else:
        print("Pase por favor.")
    if atraccion == 1:
        entrada += 1500
        atraccion_elegida += "Montania rusa "
        contador_montania += 1
    elif atraccion == 2:
        entrada += 1200
        atraccion_elegida += "Casa del terror "
        contador_terror += 1
    else:
        entrada += 800
        atraccion_elegida += "Carrusel "
        contador_carrusel += 1
    repetir = input("Espero que lo haya disfrutado!! ¿Le gustaría ir a otra atracción? (si/no) ")
    while repetir not in ["si", "no"]:
        print("Error, opción no válida. Responda con 'si' o 'no'.")
        repetir = input("¿Le gustaría ir a otra atracción? (si/no) ")
    if repetir == "no":
        break
    else:
        atraccion=int(input("A cual de las siguientes atracciones le gustaria entrar? (1-Montania rusa ; 2-Casa del terror ; 3-Carrusel) "))
    while atraccion!=1 and atraccion!=2 and atraccion!=3:
                print(f"Error, no es una atraccion valida")
                atraccion=int(input("A cual de las siguientes atracciones le gustaria entrar? (1-Montania rusa ; 2-Casa del terror ; 3-Carrusel) "))
print(f"Gracias por su visita {nombre}")
print(f"Nombre: ",nombre)
print(f"Edad: ", edad)
print(f"Cantidad de veces subido al carrusel: ", contador_carrusel)
print(f"Cantidad de veces que entró a la Casa del Terror: ", contador_terror)
print(f"Cantidad de veces que subió a la Montaña Rusa: ", contador_montania)
if contador_montania==0:
    print("No subió a la Montaña rusa ")
if contador_terror==0:
    print("No entró a la Casa del Terror ")
print(f"Este es el total a pagar: ", entrada)