from constantes import MAX

def es_entero_no_negativo(cad: str) -> bool:
    """True si cad representa un entero decimal >= 0 (solo dígitos)."""
    if cad == "":
        return False
    for ch in cad:
        if ch < '0' or ch > '9':
            return False
    return True

def parse_entero(cad: str) -> int:
    """Convierte cad (validada) a entero sin try/except. Asume solo dígitos."""
    valor = 0
    for ch in cad:
        valor = valor * 10 + (ord(ch) - ord('0'))
    return valor

def leer_no_vacio(mensaje: str) -> str:
    """Lee un string no vacío (tras recortar espacios a los costados)."""
    while True:
        s = input(mensaje)
        if s.strip() != "":
            return s
        print("Error: no puede estar en blanco.")

def leer_puntuacion_1_a_10() -> int:
    """Lee una puntuación válida [1..10] sin try/except ni isdigit."""
    while True:
        s = input("Puntuación (1 a 10): ").strip()
        if not es_entero_no_negativo(s):
            print("Error: ingrese un número entero entre 1 y 10.")
            continue
        n = parse_entero(s)
        if 1 <= n <= 10:
            return n
        print("Error: debe estar entre 1 y 10.")

def leer_sn(mensaje: str) -> str:
    """Lee respuesta 's' o 'n'. Permitido usar .lower() para esta validación."""
    while True:
        r = input(mensaje).strip().lower()
        if r == 's' or r == 'n':
            return r
        print("Respuesta inválida. Use 's' o 'n'.")

def cargar_participantes(nombres: list, puntajes: list, comentarios: list, cantidad: int) -> int:
    """Carga iterativa hasta MAX, validando. Devuelve nueva cantidad real cargada."""
    if cantidad >= MAX:
        print("Catálogo completo (10/10). No se pueden ingresar más participantes.")
        return cantidad

    i = cantidad
    while i < MAX:
        print(f"\n--- Ingreso #{i + 1} ---")
        nombre = leer_no_vacio("Nombre y apellido: ")
        puntuacion = leer_puntuacion_1_a_10()
        comentario = leer_no_vacio("Comentario: ")

        nombres[i] = nombre
        puntajes[i] = puntuacion
        comentarios[i] = comentario
        i += 1

        if i < MAX:
            seguir = leer_sn("¿Desea ingresar otro participante? (s/n): ")
            if seguir == 'n':
                break
        else:
            print("Se alcanzó el máximo de 10 participantes.")

    return i

def mostrar_participantes_y_promedio(nombres: list, puntajes: list, comentarios: list, cantidad: int) -> None:
    print("\n--- Participantes cargados ---")
    if cantidad == 0:
        print("No hay participantes cargados.")
        return
    suma = 0
    for i in range(cantidad):
        print(f"{i+1}. {nombres[i]} | Puntuación: {puntajes[i]} | Comentario: {comentarios[i]}")
        suma += puntajes[i]
    promedio = suma / cantidad
    print(f"\nPromedio de puntuaciones: {promedio:.2f}")

def bubble_sort_paralelo_por_puntuacion(nombres: list, puntajes: list, comentarios: list, cantidad: int) -> None:
    """Bubble Sort ascendente por puntaje, manteniendo correspondencia en las 3 listas."""
    if cantidad <= 1:
        return
    hubo_cambio = True
    pasada = 0
    while hubo_cambio:
        hubo_cambio = False
        limite = cantidad - 1 - pasada
        j = 0
        while j < limite:
            if puntajes[j] > puntajes[j + 1]:

                aux_p = puntajes[j]
                puntajes[j] = puntajes[j + 1]
                puntajes[j + 1] = aux_p

                aux_n = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = aux_n

                aux_c = comentarios[j]
                comentarios[j] = comentarios[j + 1]
                comentarios[j + 1] = aux_c
                hubo_cambio = True
            j += 1
        pasada += 1

def mostrar_listado(nombres: list, puntajes: list, comentarios: list, cantidad: int) -> None:
    print("\n--- Lista actual ---")
    if cantidad == 0:
        print("No hay participantes cargados.")
        return
    for i in range(cantidad):
        print(f"{i+1}. {nombres[i]} | Puntuación: {puntajes[i]} | Comentario: {comentarios[i]}")
