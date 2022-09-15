
#actividad 9

maximo = None
minimo = None

diccionario = {"Juan":36, "Pedro":25, "José":108, "Matias":32, "Jonathan":51, 
                "Jorge":12,"Nicolas":23, "Martha":8, "David":25}

for k,v in diccionario.items():
    print("El compañero: ",k," Mencionó el valor: ",v )
    if maximo == None:
        maximo = v
    elif v >= maximo:
        maximo = v

    if minimo == None:
        minimo = v    
    elif v <= minimo:
        minimo = v
print("El valor máximo es: ",maximo," y el mínimo es: ", minimo) 