MAX = 20

def cargar_libros(titulos, ejemplares, cantidad):
    disponibles = MAX - cantidad
    n = int(input(f"¿Cuántos libros desea cargar? (máx {disponibles}): "))
    if n > disponibles: 
        n = disponibles
    for i in range(cantidad, cantidad + n):
        titulos[i] = input(f"Título {(i-cantidad) + 1}: ")
        ejemplares[i] = int(input(f"Ejemplares de '{titulos[i]}': "))
    return cantidad + n  

def mostrar_catalogo(titulos, ejemplares, cantidad):
    print("--- Catálogo ---")
    if cantidad == 0:
        print("Catálogo vacío.")
    for i in range(cantidad):
        print(f"{titulos[i]} -> {ejemplares[i]} copias")

def consultar_disponibilidad(titulos, ejemplares, cantidad):
    libro = input("Título a consultar: ").lower()
    for i in range(cantidad):
        if titulos[i].lower() == libro:
            print(f"'{titulos[i]}' tiene {ejemplares[i]} copias.")
            return
    print("El libro no está en el catálogo.")

def listar_agotados(titulos, ejemplares, cantidad):
    print("--- Agotados ---")
    hay = False
    for i in range(cantidad):
        if ejemplares[i] == 0:
            print(titulos[i])
            hay = True
    if not hay:
        print("No hay libros agotados.")

def agregar_libro(titulos, ejemplares, cantidad):
    if cantidad >= MAX:
        print("Catálogo completo (20/20).")
        return cantidad
    titulo = input("Nuevo título: ")
    copias = int(input("Cantidad de ejemplares: "))
    titulos[cantidad] = titulo
    ejemplares[cantidad] = copias
    print("Libro agregado.")
    return cantidad + 1

def actualizar_ejemplares(titulos, ejemplares, cantidad):
    libro = input("Título a actualizar: ").lower()
    for i in range(cantidad):
        if titulos[i].lower() == libro:
            nuevo = int(input(f"Nueva cantidad para '{titulos[i]}': "))
            ejemplares[i] = nuevo
            print("Actualizado.")
            return
    print("El libro no está en el catálogo.")

def menu():
    titulos = [""] * MAX
    ejemplares = [0] * MAX
    cantidad = 0

    while True:
        print("--- Sistema de Catálogo de Biblioteca ---")
        print("1. Cargar títulos y ejemplares")
        print("2. Mostrar catálogo completo")
        print("3. Consultar disponibilidad")
        print("4. Listar títulos agotados")
        print("5. Agregar un nuevo título")
        print("6. Actualizar ejemplares (préstamo/devolución)")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                cantidad = cargar_libros(titulos, ejemplares, cantidad)
            case "2":
                mostrar_catalogo(titulos, ejemplares, cantidad)
            case "3":
                consultar_disponibilidad(titulos, ejemplares, cantidad)
            case "4":
                listar_agotados(titulos, ejemplares, cantidad)
            case "5":
                cantidad = agregar_libro(titulos, ejemplares, cantidad)
            case "6":
                actualizar_ejemplares(titulos, ejemplares, cantidad)
            case "7":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida.")

menu()