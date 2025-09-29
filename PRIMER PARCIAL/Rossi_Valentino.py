MAX = 10

def cargar(alumnos, libros, comentarios, cant):
    if cant >= MAX:
        print("Registro completo (10/10)")
        return cant

    i = cant
    while i < MAX:
        print("Carga", i + 1,)
        nombre = input("Nombre completo: ")
        if nombre.strip() == "":
            print("Nombre no puede estar vacío")
            continue
        cant_libros = int(input("Libros leídos (1..20): "))
        if 1 <= cant_libros <= 20:
            pass
        else:
            print("Cantidad de libros inválida")
            continue
        comentario = input("Comentario: ")
        if comentario.strip() == "":
            print("Comentario no puede estar vacío")
            continue

        alumnos[i] = nombre
        libros[i] = cant_libros
        comentarios[i] = comentario
        i += 1

        if i < MAX:
            seguir = input("¿Cargar otro? (s/n): ").lower()
            while seguir not in ("s", "n"):
                print("Respuesta inválida. Use 's' o 'n'.")
                seguir = input("¿Cargar otro? (s/n): ").lower()
            if seguir == "n":
                break
        else:
            print("Se alcanzó el máximo de 10")
    return i

def mostrar_y_promedio(alumnos, libros, comentarios, cant):
    print(" Hábitos de lectura ")
    if cant == 0:
        print("No hay alumnos cargados")
        return
    suma = 0
    for idx in range(cant):
        print(f"{idx+1}. {alumnos[idx]} | Libros: {libros[idx]} | Comentario: {comentarios[idx]}")
        suma += libros[idx]
    promedio = suma / cant
    print(f"Promedio de libros leídos: {promedio}")

def ordenar_bubble_desc(alumnos, libros, comentarios, cant):
    if cant <= 1:
        print("No hay suficientes datos para ordenar")
        return

    for pasada in range(cant - 1):
        for j in range(cant - 1 - pasada):
            if libros[j] < libros[j + 1]:
                aux = libros[j]; libros[j] = libros[j+1]; libros[j+1] = aux
                aux = alumnos[j]; alumnos[j] = alumnos[j+1]; alumnos[j+1] = aux
                aux = comentarios[j]; comentarios[j] = comentarios[j+1]; comentarios[j+1] = aux
    print(" Ordenado por libros (desc) ")
    for idx in range(cant):
        print(f"{idx+1}. {alumnos[idx]} | Libros: {libros[idx]} | Comentario: {comentarios[idx]}")

def menu():
    alumnos = [""] * MAX
    libros = [0] * MAX
    comentarios = [""] * MAX
    cant = 0

    while True:
        print("1) Ingresar alumnos")
        print("2) Mostrar y promedio")
        print("3) Ordenar por libros (Bubble desc)")
        print("4) Salir")
        op = input("Opción (1-4): ").lower()
        while op not in ("1","2","3","4"):
            print("Opción inválida.")
            op = input("Opción (1-4): ").lower()

        match op:
            case "1":
                cant = cargar(alumnos, libros, comentarios, cant)
            case "2":
                mostrar_y_promedio(alumnos, libros, comentarios, cant)
            case "3":
                ordenar_bubble_desc(alumnos, libros, comentarios, cant)
            case "4":
                print("Fin del programa")
                break
            case _:
                print("Opción inválida")

menu()