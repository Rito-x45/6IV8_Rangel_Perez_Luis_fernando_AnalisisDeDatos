import pandas as pd

#Escribir una funcion que reciva un diccionario con las notas de los estudiantes del curso y devuelve una serie con un minimo, maximo, media y desviacion tipica

def estadistica_notas(notas):
    nota = pd.Series(notas)
    etadistica = pd.Series(notas.min(), notas.max(), notas.mean(), notas.std())