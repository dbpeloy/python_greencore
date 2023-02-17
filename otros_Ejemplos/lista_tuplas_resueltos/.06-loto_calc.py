# Este código utiliza el módulo random para generar un número aleatorio de dos cifras, utilizando como base 6 números aleatorios previamente generados. Para crear un número aleatorio de dos cifras, se selecciona un número aleatorio entre 0 y 99, y se le agregan 4 dígitos aleatorios adicionales para formar un número de 6 cifras. Luego, se imprime el número resultante.

#Ten en cuenta que, para garantizar que los números generados sean realmente aleatorios, se recomienda inicializar la semilla del generador de números aleatorios usando random.seed() antes de generar cada número aleatorio.


import random

# Genera 6 números aleatorios de 2 cifras cada uno
for i in range(6):
    # Genera un número aleatorio de 2 cifras usando como base 6 números aleatorios previamente generados
    random.seed() # Inicializa la semilla del generador de números aleatorios
    num = random.choice(range(100)) # Selecciona un número aleatorio entre 0 y 99
    for j in range(5):
        num = (num * 10) + random.choice(range(10)) # Agrega un dígito aleatorio para obtener un número de 2 cifras
    print(num)

