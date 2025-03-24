import numpy as np
import matplotlib.pyplot as plt

#Crear una semilla randompra reproductubidad
np.random.seed(0)

#Crear parametros para una distribucion
#Media
media = 0

#desviacion estandar
sigma1 = 1
sigma2 = 2
sigma3 = 3

#el numero muestra para el analisis
n_muestra = 1000

#datos de la distribucion normales
datos1 = np.random.normal(media, sigma1, n_muestra)
datos2 = np.random.normal(media, sigma2, n_muestra)
datos3 = np.random.normal(media, sigma3, n_muestra)

#configurar la grafica
plt.figure(figsize=(10,6))
plt.hist(datos1, bins=30, color= "blue", density= True, label = "Desviacion Estandar (1)", alpha=0.5)
plt.hist(datos2, bins=30, color= "red", density= True, label = "Desviacion Estandar (2)", alpha=0.5)
plt.hist(datos3, bins=30, color= "green", density= True, label = "Desviacion Estandar (3)", alpha=0.5)

#a graficar
plt.title("conparacion de distribucion normales con una semilla random")
plt.ylabel("valor")
plt.xlabel("densidad")
plt.axhline(0, color = "black", linewidth = 0.5, ls = "--")
plt.axvline(0, color = "black", linewidth = 0.5, ls = "--")
plt.legend()
plt.grid()
plt.show()