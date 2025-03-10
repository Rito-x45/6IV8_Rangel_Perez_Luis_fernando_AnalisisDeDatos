import pandas as pd

#Escribir una funcion que reciva un diccionario con las notas de los estudiantes del curso 
# y devuelve una serie con un minimo, maximo, media y desviacion tipica

def estadistica_notas(notas):
    notas = pd.Series(notas)
    etadistica = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index = ["minimo", "Max", "Media", "Desviacion Estandar"])
    return etadistica

def aprobados(notas):
    notas = pd.Series(notas)
    return notas[notas >= 6].sort_values(ascending=False)

notas = {"Juan": 9, "Juana": 10, "Pepe": 4.6, "Pedro": 0, "Fabian":4, "Maximiliano":8, "Sandra": 1, "Rosario": 6}

print(estadistica_notas(notas))
print(aprobados(notas))