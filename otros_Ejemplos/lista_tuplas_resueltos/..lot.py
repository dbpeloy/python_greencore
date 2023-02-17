

import random

# Pedimos al usuario cuántas veces quiere correr el programa
num_corridas = int(input("Ingrese el número de veces que desea correr el programa (máximo 10): "))

# Verificamos que el número de corridas sea válido
if num_corridas <= 0 or num_corridas > 10:
    print("Número de corridas no válido.")
else:
    # Creamos una lista vacía para guardar los números bases
    nums_bases = []

    # Pedimos al usuario los números bases y los guardamos en la lista nums_bases
    for i in range(5):
        num_base = input("Ingrese el número base de dos cifras: ")
        while len(num_base) != 2 or not num_base.isdigit():
            num_base = input("Número no válido. Ingrese el número base de dos cifras: ")
        nums_bases.append(num_base)

    # Repetimos el proceso num_corridas veces
    for i in range(num_corridas):
        # Creamos una lista vacía para guardar los números aleatorios
        nums_aleatorios = []

        # Generamos los números aleatorios
        for j in range(5):
            num_aleatorio = str(random.randint(0, 99)).zfill(2)
            nums_aleatorios.append(num_aleatorio)

        # Mostramos los números bases y los números aleatorios generados en esta corrida
        print(f"\nResultados del ciclo {i+1}")
        for k in range(5):
            print(f"Número base: {nums_bases[k]} - Número aleatorio: {nums_aleatorios[k]}")

