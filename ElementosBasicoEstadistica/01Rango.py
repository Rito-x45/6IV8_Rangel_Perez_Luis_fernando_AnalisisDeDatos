import pandas as pd

#Escribir un programa que pregunte al usuario por la venta de rango en años y muestre en la pantalla una serie de datos de ventas indexadas por los años antes y despues de aplicar los con descuento

inicio = int(input("Introduce el año de ventas inicial: "))
fin = int(input("Introduce el año final de ventas: "))

ventas = {}

for i in range(inicio, fin + 1):
    ventas[i] = float(input("Introcude las ventas de este año " + str(i) + ": "))
    

ventas = pd.Series(ventas)
print("Ventas \n", ventas)
print("Ventas por descuento\n", ventas*0.9)