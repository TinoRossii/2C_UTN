def area_triangulo(base, altura):
    return (base * altura) / 2

b= float(input("Ingrese la base del triángulo: "))  
a= float(input("Ingrese la altura del triángulo: "))  
print(f"El área del triángulo es: {area_triangulo(b, a)}")