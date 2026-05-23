import time
import math
import numpy as np

def es_primo_optimizado(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


inicio = time.time()

numeros = np.arange(1, 100001)

primos = [numero for numero in numeros if es_primo_optimizado(numero)]

fin = time.time()

print("Cantidad de números primos encontrados:", len(primos))
print("Tiempo de ejecución del código optimizado:", fin - inicio, "segundos")