# OPTIMIZACION DE CODIGOS Y MEDICION DE TIEMPOS

# INTRODUCCION

El presente trabajo tiene como objetivo aplicar técnicas de optimización y buenas prácticas de programación en Python para mejorar el rendimiento de un código encargado de buscar números primos en un rango de 1 a 100000.

Inicialmente se trabajó con un código sin optimización, el cual presentaba tiempos de ejecución elevados debido al uso de bucles ineficientes y múltiples iteraciones innecesarias.

Posteriormente se aplicaron diferentes técnicas de optimización para reducir el tiempo de ejecución y mejorar la eficiencia del programa.

# CODIGO ORIGINAL

El código original realizaba la búsqueda de números primos recorriendo todos los números desde 2 hasta n para verificar si un número era primo.

El tiempo de ejecución obtenido fue de aproximadamente:

- 45.17 segundos

Esto evidenció un bajo rendimiento computacional.

# TEGNICAS DE OPERACION APLICADAS

Se aplicaron las siguientes técnicas de optimización:

# 1: REDUCCION DEL RANGO DEL BUCLE

Se optimizó la verificación de números primos utilizando únicamente iteraciones hasta la raíz cuadrada de n, reduciendo significativamente el número de operaciones.

# 2. USO DE LIST COMPREHENSIONS

Se reemplazó el uso de ciclos tradicionales y append() por list comprehensions para mejorar la eficiencia en la creación de listas.

# 3. USO DE NUMPY

Se utilizaron arrays de NumPy mediante np.arange() para optimizar el manejo de datos numéricos.

# RESULTADOS

Después de aplicar las optimizaciones, el tiempo de ejecución del programa se redujo considerablemente.

# TIEMPO DEL CODIGO OPTIMIZADO 

- 0.22 segundos aproximadamente.

La comparación demuestra una mejora significativa en el rendimiento del programa.

Además, mediante cProfile se identificó que la función que más tiempo consumía era:

- es_primo_optimizado()

También se verificó el uso de la función math.sqrt() como parte de la optimización.

# ANALISIS

La optimización permitió disminuir drásticamente el tiempo de ejecución del programa. La reducción del rango de iteraciones fue la técnica que mayor impacto tuvo en el rendimiento.

El uso de list comprehensions permitió simplificar el código y hacerlo más eficiente, mientras que NumPy ayudó en el manejo optimizado de arrays numéricos.

El profiling realizado con cProfile permitió identificar las funciones críticas del programa y analizar el comportamiento del código durante su ejecución.

# CONCLUSIONES

La aplicación de buenas prácticas de programación y técnicas de optimización permitió mejorar significativamente el rendimiento del programa en Python.

El uso adecuado de estructuras optimizadas, reducción de iteraciones innecesarias y herramientas de análisis como cProfile contribuyen a desarrollar programas más eficientes y escalables.

Finalmente, este trabajo permitió comprender la importancia de medir y analizar el rendimiento del código durante el desarrollo de proyectos de Ciencia de Datos.