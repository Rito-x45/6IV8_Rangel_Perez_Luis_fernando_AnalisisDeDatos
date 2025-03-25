import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# cargar archivo de Excel
datos = pd.read_excel("Ejercicios/proyecto1.xlsx")

# sumar todas las ventas
ventas_totales = datos["ventas_tot"].sum()
print("Ventas totales:", ventas_totales)

# contar clientes con y sin adeudo
con_adeudo = datos[datos["B_adeudo"] == "Con adeudo"].shape[0]
sin_adeudo = datos[datos["B_adeudo"] == "Sin adeudo"].shape[0]
total_clientes = con_adeudo + sin_adeudo

# sacar porcentajes
porc_adeudo = (con_adeudo / total_clientes) * 100
porc_sin_adeudo = (sin_adeudo / total_clientes) * 100

print(f"Porcentaje de clientes con adeudo: {porc_adeudo:.2f}%")
print(f"Porcentaje de clientes sin adeudo: {porc_sin_adeudo:.2f}%")

# agrupar ventas por mes y graficar
ventas_por_fecha = datos.groupby("B_mes")["ventas_tot"].sum().reset_index()

plt.bar(ventas_por_fecha["B_mes"].dt.strftime("%Y-%m-%d"), ventas_por_fecha["ventas_tot"])
plt.title("Ventas por fecha")
plt.xlabel("Fecha")
plt.ylabel("Ventas totales")
plt.show()

# desviación estándar de los pagos por mes
pagos_std = datos.groupby("B_mes")["pagos_tot"].std().reset_index()

plt.bar(pagos_std["B_mes"].dt.strftime("%Y-%m-%d"), pagos_std["pagos_tot"])
plt.title("Desviación estandar de pagos")
plt.xlabel("Fecha")
plt.ylabel("Desviación estandar")
plt.show()

# sumar todas las deudas
deuda_total = datos["adeudo_actual"].sum()
print("Deuda total de los clientes:", deuda_total)

# sacar porcentaje de utilidad
utilidad = ((ventas_totales - deuda_total) / ventas_totales) * 100
print(f"Porcentaje de utilidad del comercio: {utilidad:.2f}%")

# gráfica circular de ventas por sucursal
ventas_sucursal = datos.groupby("suc")["ventas_tot"].sum()
colores = plt.cm.tab20.colors[:len(ventas_sucursal)]

plt.pie(ventas_sucursal,
        labels=ventas_sucursal.index,
        autopct="%1.1f%%",
        startangle=140,
        colors=colores)
plt.title("Ventas por sucursal")
plt.show()

# gráfica de barras con deuda y utilidad por sucursal
deuda_sucursal = datos.groupby("suc")["adeudo_actual"].sum()
ventas_sucursal = datos.groupby("suc")["ventas_tot"].sum()
utilidad_sucursal = ((ventas_sucursal - deuda_sucursal) / ventas_sucursal)

sucursales = deuda_sucursal.index
x = np.arange(len(sucursales))
ancho = 0.35

fig, ax1 = plt.subplots(figsize=(10,6))
ax1.bar(x - ancho/2, deuda_sucursal, ancho, label="Deuda Total")
ax1.set_ylabel("Deuda Total")
ax2 = ax1.twinx()
ax2.bar(x + ancho/2, utilidad_sucursal, ancho, label="Utilidad", color="red")
ax2.set_ylabel("Margen de Utilidad")

plt.title("Deuda Total y Margen de Utilidad por Sucursal")
fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
plt.show()
