def convertir_minutos(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes 
min= int(input("Ingrese la cantidad de minutos: "))
ho, mi= convertir_minutos(min)
print(f"{min} minutos son {ho} horas y {mi} minutos.")