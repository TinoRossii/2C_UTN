def saludar(nombre:str)->None:
    print(f"Hola, {nombre}.")

def promedio(a:int, b:int, c:int)->float:
    return (a+ b + c) /3

def operar(a:int, b:int)->int:
    suma = a + b
    resta = a - b
    multiplicación = a * b
    return suma, resta, multiplicación

def dividir(a:int, b:int)->None:
    print(f"la división es: {a/b}")