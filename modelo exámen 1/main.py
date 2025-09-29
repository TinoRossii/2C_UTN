from constantes import MAX
from funciones import (
    cargar_participantes,
    mostrar_participantes_y_promedio,
    bubble_sort_paralelo_por_puntuacion,
    mostrar_listado,)

def menu():
    nombres = [""] * MAX
    puntajes = [0] * MAX
    comentarios = [""] * MAX
    cantidad = 0

    while True:
        print("\n--- Menú Encuesta de Satisfacción ---")
        print("1. Ingresar participantes")
        print("2. Mostrar participantes y promedio")
        print("3. Ordenar participantes por puntuación (Bubble Sort)")
        print("4. Salir")
        seleccion = input("Seleccione una opción (1-4): ").strip()

        match seleccion:
            case "1":
                cantidad = cargar_participantes(nombres, puntajes, comentarios, cantidad)
            case "2":
                mostrar_participantes_y_promedio(nombres, puntajes, comentarios, cantidad)
            case "3":
                if cantidad == 0:
                    print("No hay participantes para ordenar.")
                else:
                    bubble_sort_paralelo_por_puntuacion(nombres, puntajes, comentarios, cantidad)
                    mostrar_listado(nombres, puntajes, comentarios, cantidad)
            case "4":
                print("Programa finalizado. ¡Éxitos!")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()