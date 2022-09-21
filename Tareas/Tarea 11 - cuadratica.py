import cmath as m
from math import sqrt
def formula_general(a,b,c):
    determinante = (b**2)-4*a*c
    if determinante < 0:
        x1=(-b+m.sqrt(b**2-(4*a*c)))/(2*a)
        x2=(-b-m.sqrt(b**2-(4*a*c)))/(2*a)
        print("La solución es compleja")
    else:
        x1=(-b+sqrt(b**2-(4*a*c)))/(2*a)
        x2=(-b-sqrt(b**2-(4*a*c)))/(2*a)
    print("El valor de x1: {0}\nEl valor de x2:{1}".format(x1,x2))

formula_general(10,23,45)
formula_general(10,23,-45)