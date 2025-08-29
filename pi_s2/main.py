from gestion_parque.parque import *

nombre = input("Por favor, ingrese su nombre: ")


edad = input("Ingrese su edad: ")


mostrar_atracciones()
entrada = 0
atraccion_elegida = ""
contador_montaña = 0
contador_terror = 0
contador_carrusel = 0 
contador_atracciones = 0

while True:
    atraccion = int(input("¿A cuál de las siguientes atracciones le gustaría entrar? (1-Montaña rusa ; 2-Casa del terror ; 3-Carrusel) "))
    if atraccion not in [1, 2, 3]:
        print("Error, no es una atracción válida.")
        continue
    if not puede_subir(edad, atraccion):
        if edad < 6:
            print("Lo siento, solo puede ingresar al Carrusel.")
        elif edad <= 12:
            print("Usted solo puede pasar al Carrusel y Casa del Terror.")
        continue
    print("Pase por favor.")
    precio = calcular_precio(atraccion)
    entrada += precio
    if atraccion == 1:
        atraccion_elegida += "Montaña rusa "
        contador_montaña += 1
        contador_atracciones += 1
    elif atraccion == 2:
        atraccion_elegida += "Casa del terror "
        contador_terror += 1    
        contador_atracciones += 1
    else:         
        atraccion_elegida += "Carrusel "
        contador_carrusel += 1  
        contador_atracciones += 1    
    repetir = input("Espero que lo haya disfrutado!! ¿Le gustaría ir a otra atracción? (s/n) ")
    while repetir not in ["s", "n"]:
        print("Error, opción no válida. Responda con 's' o 'n'.")
        repetir = input("¿Le gustaría ir a otra atracción? (s/n) ")   
    if repetir == "n":
        break   
if contador_atracciones >= 3:
    print("¡Se aplica un descuento del 10% por subir a 3 o más atracciones!")
    entrada *= 0.90

mostrar_resumen(nombre, edad, contador_montaña, contador_terror, contador_carrusel)
print(f"Total a pagar: {entrada}")
if contador_montaña == 0:
    print("No subió a la Montaña rusa ")        
if contador_terror == 0:
    print("No entró a la Casa del Terror ")       
if contador_carrusel == 0:
    print("No subió al Carrusel ")