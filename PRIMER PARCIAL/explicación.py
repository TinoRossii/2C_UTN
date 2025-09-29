MAX = 10  # Capacidad máxima de registros para las listas estáticas

def cargar(alumnos, libros, comentarios, cant):
    # Si ya llegamos al máximo, no cargamos más y devolvemos la cantidad actual
    if cant >= MAX:
        print("Registro completo (10/10)")
        return cant

    i = cant  # Índice de escritura: próxima posición libre
    while i < MAX:  # Bucle de carga mientras quede espacio
        print("Carga", i + 1,)  # Muestra el número de carga (la coma extra no afecta)

        nombre = input("Nombre completo: ")  # Lee el nombre
        # Valida que no sea vacío ni solo espacios
        if nombre.strip() == "":
            print("Nombre no puede estar vacío")
            continue  # Vuelve a pedir esta misma carga (sin avanzar i)

        # Lee la cantidad de libros y convierte a int
        # OJO: si el usuario ingresa texto no numérico, lanzará ValueError (no se maneja acá)
        cant_libros = int(input("Libros leídos (1..20): "))
        # Valida el rango permitido [1..20]
        if 1 <= cant_libros <= 20:
            pass  # Todo OK, seguimos
        else:
            print("Cantidad de libros inválida")
            continue  # Reintenta esta carga

        comentario = input("Comentario: ")  # Lee comentario
        # Valida que no sea vacío ni solo espacios
        if comentario.strip() == "":
            print("Comentario no puede estar vacío")
            continue  # Reintenta esta carga

        # Guarda los tres campos en el mismo índice (listas paralelas)
        alumnos[i] = nombre
        libros[i] = cant_libros
        comentarios[i] = comentario
        i += 1  # Avanza a la próxima posición libre

        if i < MAX:  # Si aún hay lugar, pregunta si seguir cargando
            seguir = input("¿Cargar otro? (s/n): ").lower()  # Normaliza a minúsculas
            # Repite hasta que la respuesta sea 's' o 'n'
            while seguir not in ("s", "n"):
                print("Respuesta inválida. Use 's' o 'n'.")
                seguir = input("¿Cargar otro? (s/n): ").lower()
            if seguir == "n":  # Si no quiere seguir, sale del bucle de carga
                break
        else:
            print("Se alcanzó el máximo de 10")  # Justo se llenó

    return i  # Devuelve la nueva cantidad cargada

def mostrar_y_promedio(alumnos, libros, comentarios, cant):
    print(" Hábitos de lectura ")  # Encabezado
    if cant == 0:  # Si no hay datos, informa y termina
        print("No hay alumnos cargados")
        return

    suma = 0  # Acumulador de libros
    # Recorre solo los registros efectivamente cargados [0..cant-1]
    for idx in range(cant):
        print(f"{idx+1}. {alumnos[idx]} | Libros: {libros[idx]} | Comentario: {comentarios[idx]}")
        suma += libros[idx]  # Suma la cantidad de libros para el promedio

    promedio = suma / cant  # Calcula promedio (float)
    print(f"Promedio de libros leídos: {promedio}")  # Muestra el promedio (sin formato fijo de decimales)

def ordenar_bubble_desc(alumnos, libros, comentarios, cant):
    # Si hay 0 o 1 elemento, no hay nada que ordenar
    if cant <= 1:
        print("No hay suficientes datos para ordenar")
        return

    # Bubble Sort clásico con límite decreciente; criterio descendente por 'libros'
    for pasada in range(cant - 1):  # Cant-1 pasadas como máximo
        for j in range(cant - 1 - pasada):  # Compara pares contiguos hasta el límite
            if libros[j] < libros[j + 1]:  # Descendente: si izq < der, intercambia
                # Intercambia en 'libros'
                aux = libros[j]; libros[j] = libros[j+1]; libros[j+1] = aux
                # Intercambia en 'alumnos' (mantener correspondencia)
                aux = alumnos[j]; alumnos[j] = alumnos[j+1]; alumnos[j+1] = aux
                # Intercambia en 'comentarios' (mantener correspondencia)
                aux = comentarios[j]; comentarios[j] = comentarios[j+1]; comentarios[j+1] = aux

    print(" Ordenado por libros (desc) ")  # Encabezado del listado ordenado
    # Muestra el resultado en el nuevo orden
    for idx in range(cant):
        print(f"{idx+1}. {alumnos[idx]} | Libros: {libros[idx]} | Comentario: {comentarios[idx]}")

def menu():
    # Crea listas estáticas de tamaño MAX
    alumnos = [""] * MAX
    libros = [0] * MAX
    comentarios = [""] * MAX
    cant = 0  # Cantidad real cargada al inicio

    while True:  # Bucle principal del menú
        print("1) Ingresar alumnos")
        print("2) Mostrar y promedio")
        print("3) Ordenar por libros (Bubble desc)")
        print("4) Salir")
        op = input("Opción (1-4): ").lower()  # Lee opción y la pone en minúsculas
        # Valida que la opción sea una de las permitidas
        while op not in ("1","2","3","4"):
            print("Opción inválida.")
            op = input("Opción (1-4): ").lower()

        # Despacha según la opción (requiere Python 3.10+)
        match op:
            case "1":
                # Llama a 'cargar' y actualiza la cantidad real de registros
                cant = cargar(alumnos, libros, comentarios, cant)
            case "2":
                # Muestra todos los registros y el promedio de libros
                mostrar_y_promedio(alumnos, libros, comentarios, cant)
            case "3":
                # Ordena por cantidad de libros (descendente) y muestra el listado ordenado
                ordenar_bubble_desc(alumnos, libros, comentarios, cant)
            case "4":
                print("Fin del programa")  # Sale del menú/bucle
                break
            case _:
                # Por la validación previa no debería ocurrir, pero se deja por seguridad
                print("Opción inválida")

menu()  # Punto de entrada: ejecuta el menú principal
