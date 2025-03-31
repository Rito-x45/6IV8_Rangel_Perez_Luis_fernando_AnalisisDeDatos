import pandas as pd
import numpy as np
from scipy.spatial import distance

#Definir cordenadas de las tiendas
tiendas = {
    'Tienda A': (1,1),
    'Tienda B': (1,5),
    'Tienda C': (7,1),
    'Tienda D': (3,3),
    'Tienda E': (4,8)
}

#Convertir cordenadas a un dataframe
df_tiendas = pd.DataFrame(tiendas).T
df_tiendas.columns = ['X', 'Y']
print("Cordenadas de las tiendas:")
print(df_tiendas)

#Iniciamos una forma para almacenar distancia
distancia_eu = pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)
distancia_mh = pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)
distancia_ch = pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)

#Calcular distancia
for i in df_tiendas.index:
    for j in df_tiendas.index:

        #Distancias Euclideanas
        distancia_eu.loc[i,j] = distance.euclidean(df_tiendas.loc[i], df_tiendas.loc[j])

        #Distancias Manhattan
        distancia_mh.loc[i,j] = distance.cityblock(df_tiendas.loc[i], df_tiendas.loc[j])
        
        #Distancia Chebyshev
        distancia_ch.loc[i,j] = distance.chebyshev(df_tiendas.loc[i], df_tiendas.loc[j])

#Mostrar resultados
print("\nDistancia Euclideana entre las tiendas:\n")
print(distancia_eu)

print("\nDistancia Manhattan entre las tiendas:\n")
print(distancia_mh)

print("\nDistancia Chebyshev entre las tiendas:\n")
print(distancia_ch)