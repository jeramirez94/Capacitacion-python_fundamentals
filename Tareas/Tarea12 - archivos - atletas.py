from email import header
import pandas as pd
import numpy as np
import csv
datos = pd.read_csv("C:\\Users\\jeramirez\\Documents\\python_fundamentals\\Tareas\\athlete_events.csv")
datosAgeMedal = datos[datos['Medal'].notna()]
datosAgeMedal = datosAgeMedal[datosAgeMedal['Age'].notna()]

medallistasOro = datosAgeMedal[datosAgeMedal["Medal"]=='Gold']
medallistasPlata = datosAgeMedal[datosAgeMedal["Medal"]=='Silver']
medallistasBronce = datosAgeMedal[datosAgeMedal["Medal"]=='Bronze']
print("============================\nInicio\n============================")
print("============================\nMás Veterano Oro\n============================")
#print(medallistasOro.sort_values(['Age'], ascending=[False]))
print(medallistasOro[medallistasOro["Age"] == medallistasOro["Age"].max()])
print("============================\nMás Veterano Plata\n============================")
print(medallistasPlata[medallistasPlata["Age"] == medallistasPlata["Age"].max()])
print("============================\nMás Veterano Bronce\n============================")
print(medallistasBronce[medallistasBronce["Age"] == medallistasBronce["Age"].max()])
print("============================\nMás joven en ganar oro\n============================")

print(medallistasOro[medallistasOro["Age"] == medallistasOro["Age"].min()])

print("============================\nEl más ganador\n============================")
medallistas = datos[datos["Name"].notna()] #solo registros con nombre
medallistas = medallistas[medallistas["Medal"].notna()] #solo registros con medallas
medallistaMasGanador = medallistas.mode()
print(medallistaMasGanador)
medallistaMasGanador.to_csv("C:\\Users\\jeramirez\\Documents\\python_fundamentals\\Tareas\\elmasganador.csv", header=True,index=True)