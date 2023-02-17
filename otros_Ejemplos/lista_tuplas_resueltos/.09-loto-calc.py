# Este código utiliza un bucle for para solicitar al usuario que proporcione 6 números de 2 cifras válidos como base para los números aleatorios. Si el usuario introduce un número inválido, el programa le pedirá que lo vuelva a intentar hasta que proporcione un número válido. Cada número base se agrega a una lista llamada numeros_base.

# Una vez que se han establecido los números base, el código utiliza otro bucle for para generar un número aleatorio de 2 cifras para cada número base. El número aleatorio generado no será igual al número base correspondiente. Cada número aleatorio se agrega a una lista llamada numeros_aleatorios.

# Finalmente, el programa muestra los números aleatorios generados en pantalla.


import random

# Pide al usuario que introduzca 6 números de 2 cifras como base.
numeros_base = []
for i in range(6):
    while True:
        base = input(f"Introduce el número {i+1} de dos cifras entre 00 y 99: ")
        if len(base) == 2 and base.isdigit() and 0 <= int(base) <= 99:
            base = int(base)
            numeros_base.append(base)
            break
        else:
            print("El número introducido no es válido.")

# Genera 6 números aleatorios de 2 cifras basados en la lista de números base.
numeros_aleatorios = []
for base in numeros_base:
    num = random.randint(0, 99)
    while num == base:
        num = random.randint(0, 99)
    numeros_aleatorios.append(num)

# Muestra los números aleatorios generados.
print("Los números aleatorios generados son:", numeros_aleatorios)

