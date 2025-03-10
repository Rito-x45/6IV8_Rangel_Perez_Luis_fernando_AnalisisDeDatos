import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./ElementosBasicoEstadistica/housing.csv")

#Mostrar las priemeras 5 filas
print(df.head())

#Mostrar las ultimas 5 filas
print(df.tail())

#Mostrar fila en especifico
print(df.iloc[7])

#Mostrar fila en especifico
print(df.iloc[7 - 10])

#Mostrar fila en especifico
print(df.iloc[7: 10])

#Mostar la columna
print(df["ocean_proximity"])

#Medi de la columna total_bedrooms
mediadecuartos = df["total_bedrooms"].mean()
print("La media de cuartos es: " + str(mediadecuartos))

#Mediana
medianacuarto = df["median_house_value"].median()
print("La media de la casa es : " + str(medianacuarto))

#Suma de popular
sumatotal = df["population"].sum
print("La sumatoria total es: ", sumatotal)

#Filtrar
vomoshacerfiltros = df[df["ocean_proximity"] == "ISLAND"]
print(vomoshacerfiltros)


#Vamos a hacer un grafico de dispersion
plt.scatter(df["ocean_proximity"][:10], df["median_house_value"][:10])
#nombrar ejes
plt.xlabel("Proximidad")
plt.ylabel("Precio")
#Titulo
plt.title("Grafico de dispersion de la proximidad al oceano precio")
plt.show()