import pandas as pd

#Escribir una funcion que reciva un diccionario con las notas de los estudiantes del curso 
# y devuelve una serie con un minimo, maximo, media y desviacion tipica

def estadistica_notas(notas):
    notas = pd.Series(notas)
    etadistica = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index = ["minimo", "Max", "Media", "Desviacion Estandar"])
    return etadistica

notas = {"Juan": 9, "Juana": 10, "Pepe": 9.6, "Pedro": 7, "Fabian":6, "Maximiliano":8, "Sandra": 11, "Rosario": 6}

print(estadistica_notas(notas))