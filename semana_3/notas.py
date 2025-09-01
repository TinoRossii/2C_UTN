# Realizar un programa que registre las notas de varios alumnos
# La cantidad de almunos la va a definir el usuario
# Cada alumno tendrá cargadas 3 notas
# Al final del programa necesitamos saber el promedio general del curso
# El promedio más alto

acumulación_total_notas = 0
promedio_mayor = None
alumno_mayor = None
cantidad_de_alumnos = int(input("Ingrese la cantidad de alumnos: "))
alumno = 1

while alumno <= cantidad_de_alumnos:
    total_notas = 0
    for examen in range(1, 4):
        nota = int(input("Ingrese la nota: "))
        total_notas += nota
    acumulación_total_notas += total_notas
    promedio_alumno = total_notas / 3
    print(f"El promedio del alumno {alumno} es: {promedio_alumno}")
    if promedio_mayor is None or promedio_alumno > promedio_mayor:
        promedio_mayor = promedio_alumno
        alumno_mayor = alumno
    alumno += 1

promedio_general_curso = acumulación_total_notas / cantidad_de_alumnos
print(f"El promedio general del curso es: {promedio_general_curso}")
print(f"El promedio más alto es: {promedio_mayor}, del alumno {alumno_mayor}")