
totalCobro = 0.0
totalProductos = 0
monto = -1

while monto != 0:
    monto = float(input("[Para terminar ingrese 0]\nIngrese el monto del producto {0}: ".format(totalProductos+1)))
    if monto < 0:
        print("Los valores negativos no son aceptado")
        continue
    elif monto == 0:
        break
    else:
        totalProductos = totalProductos + 1
        totalCobro += monto

if totalCobro>1000:
    totalCobro = totalCobro - (totalCobro * 0.10)
    print("Su compra tiene el 10% de descuento \nEl total a pagar de sus {0} productos es: {1}".format(totalProductos, totalCobro))
else:
    print("El total a pagar de sus {0} productos es: {1}".format(totalProductos, totalCobro))
