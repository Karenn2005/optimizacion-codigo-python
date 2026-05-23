import matplotlib.pyplot as plt

codigos = ["Original", "Optimizado"]
tiempos = [45.17, 0.22]

plt.bar(codigos, tiempos)
plt.title("Comparación de tiempos de ejecución")
plt.xlabel("Tipo de código")
plt.ylabel("Tiempo en segundos")

plt.savefig("comparacion_tiempos.png")
plt.show()