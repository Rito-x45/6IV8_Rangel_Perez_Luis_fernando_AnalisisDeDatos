import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos = pd.read_csv("./ElementosBasicoEstadistica/housing.csv")

columnas = ["median_house_value", "total_bedrooms", "population"]
estadisticas = {}

for col in columnas:
    valores = datos[col].dropna()
    promedio = valores.mean()
    mediana = valores.median()
    moda = valores.mode().iloc[0] if not valores.mode().empty else np.nan
    rango_val = valores.max() - valores.min()
    varianza = valores.var()
    desviacion_estandar = valores.std()
    estadisticas[col] = {
        "Media": promedio,
        "Mediana": mediana,
        "Moda": moda,
        "Rango": rango_val,
        "Varianza": varianza,
        "Desviación Estándar": desviacion_estandar
    }

tabla_estadisticas = pd.DataFrame(estadisticas)
tabla_estadisticas.reset_index(inplace=True)
tabla_estadisticas.rename(columns={"index": "Estadística"}, inplace=True)

print("\nTabla de Estadísticas Descriptivas:")
print(tabla_estadisticas)

tablas_frecuencias = {}

intervalos_valor_casa = np.linspace(1700, 3600, 11)
frecuencias_valor_casa = pd.cut(datos["median_house_value"], bins=intervalos_valor_casa, include_lowest=True).value_counts().sort_index()
tablas_frecuencias["median_house_value"] = frecuencias_valor_casa

for col in ["total_bedrooms", "population"]:
    valores = datos[col].dropna()
    intervalos = np.linspace(valores.min(), valores.max(), 11)
    tabla_frecuencias = pd.cut(valores, bins=intervalos, include_lowest=True).value_counts().sort_index()
    tablas_frecuencias[col] = tabla_frecuencias

for col, tabla in tablas_frecuencias.items():
    print(f"\nTabla de Frecuencias para {col}:")
    print(tabla)

fig, ejes = plt.subplots(1, 3, figsize=(18, 5))

datos_valor_casa = datos["median_house_value"].dropna()
ejes[0].hist(datos_valor_casa, bins=30, edgecolor='black')
ejes[0].axvline(estadisticas["median_house_value"]["Media"], color='red', linestyle='dashed', linewidth=1, label=f"Media: {estadisticas['median_house_value']['Media']:.2f}")
ejes[0].set_title("Histograma de median_house_value")
ejes[0].set_xlabel("median_house_value")
ejes[0].set_ylabel("Frecuencia")
ejes[0].set_xlim(1700, 3600)
ejes[0].legend()

datos_cuartos = datos["total_bedrooms"].dropna()
ejes[1].hist(datos_cuartos, bins=30, edgecolor='black')
ejes[1].set_title("Histograma de total_bedrooms")
ejes[1].set_xlabel("total_bedrooms")
ejes[1].set_ylabel("Frecuencia")

datos_populacion = datos["population"].dropna()
ejes[2].hist(datos_populacion, bins=30, edgecolor='black')
ejes[2].set_title("Histograma de population")
ejes[2].set_xlabel("population")
ejes[2].set_ylabel("Frecuencia")

plt.tight_layout()
plt.show()
