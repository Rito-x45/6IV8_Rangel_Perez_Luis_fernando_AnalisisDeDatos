import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los archivos Excel
datos = pd.read_excel("Ejercicios/proyecto1.xlsx")

#sumatotal
ventast = datos["ventas_tot"].sum()
print(ventast)

#Clientes con adeudo y sin adeudo
adeudoYsnAdeudo = datos["B_adeudo"].value_counts()
print("adeudoYsnAdeudo")

clientesT = datos["no_clientes"]
