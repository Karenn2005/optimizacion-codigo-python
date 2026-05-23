import time

def es_primo(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


inicio = time.time()

primos = []

for numero in range(1, 100001):
    if es_primo(numero):
        primos.append(numero)

fin = time.time()

print("Cantidad de números primos encontrados:", len(primos))
print("Tiempo de ejecución del código original:", fin - inicio, "segundos")