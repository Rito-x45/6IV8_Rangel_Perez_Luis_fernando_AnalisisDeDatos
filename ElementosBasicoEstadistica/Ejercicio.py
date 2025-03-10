import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("./ElementosBasicoEstadistica/housing.csv")
columnas = ["median_house_value", "total_bedrooms", "population"]

estadisticas = {}

for i in columnas:
    estadisticas[i] = {
        "Media": np.mean(df[i]),
        "Mediana": np.median(df[i]),
        "Moda": df[i].mode()[0],
        "Rango": df[i].max() - df[i].min(),
        "Varianza": np.var(df[i], ddof=1),  
        "Desviación Estándar": np.std(df[i], ddof=1)
    }

df_estadisticas = pd.DataFrame(estadisticas)
print("\nEstadísticas Descriptivas:\n", df_estadisticas)

tabla_frecuencia = df["median_house_value"].value_counts().reset_index()
tabla_frecuencia.columns = ["Valor", "Frecuencia"]

print("\nTabla de Frecuencia - median_house_value\n", tabla_frecuencia.head(10))

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

axs[0].hist(df["median_house_value"], bins=30, alpha=0.7, color="blue", range=(500, 756))
axs[0].set_title("Histograma de median_house_value")
axs[0].set_xlabel("Valor")
axs[0].set_ylabel("Frecuencia")

axs[1].hist(df["total_bedrooms"], bins=30, alpha=0.7, color="green", range=(500, 756))
axs[1].set_title("Histograma de total_bedrooms")
axs[1].set_xlabel("Valor")
axs[1].set_ylabel("Frecuencia")

axs[2].hist(df["population"], bins=30, alpha=0.7, color="red", range=(500, 756))
axs[2].set_title("Histograma de population")
axs[2].set_xlabel("Valor")
axs[2].set_ylabel("Frecuencia")

plt.tight_layout()
plt.show()
