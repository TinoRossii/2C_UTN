total_ventas = 0
cantidad_ventas = 0
venta_mayor = None
venta_menor = None

while True:
    venta = float(input("Importe de venta, (para finalizar ingrese 0): "))

    if venta == 0:
        break

    total_ventas += venta
    cantidad_ventas += 1

    if cantidad_ventas == 1:
        venta_mayor = venta
        venta_menor = venta
    else:
        if venta > venta_mayor:
            venta_mayor = venta
        if venta < venta_menor:
            venta_menor = venta

if cantidad_ventas == 0:
    print("No se registraron ventas")
else:
    print(f"Venta mayor: ${venta_mayor}")
    print(f"Venta menor: ${venta_menor}")
    print(f"Cantidad ventas: {cantidad_ventas}")
    print(f"Total de ventas: ${total_ventas}")
    print(f"Promedio de ventas: ${total_ventas / cantidad_ventas}")
