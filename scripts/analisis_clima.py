
import pandas as pd
import matplotlib.pyplot as plt

#cargamos el dataset climático desde la carpeta datos
df = pd.read_csv("datos/annual.csv")

#tomamos las dos primeras columnas (solo las necesarias)
df = df[["Year", "Mean"]]

#eliminación de valores nulos para garantizar cálculos correctos
df = df.dropna()

#análisis estadístico
promedio = df["Mean"].mean()
maximo = df["Mean"].max()
minimo = df["Mean"].min()

print("==INDICADORES CLIMÁTICOS==")
print(f"Temperatura promedio: {promedio}")
print(f"Temperatura máxima: {maximo}")
print(f"Temperatura mínima: {minimo}")

#gráfico
plt.plot(df["Year"], df["Mean"])
plt.title("Evolución de temperatura")
plt.xlabel("Año")
plt.ylabel("Temperatura media")
plt.grid()

#guardamos el gráfico en resultados
plt.savefig("resultados/grafico_clima.png")
plt.show()
