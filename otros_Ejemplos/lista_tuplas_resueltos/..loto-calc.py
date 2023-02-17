# Este código utiliza un bucle while para ejecutar el programa tantas veces como el usuario lo desee. Dentro del bucle, se utiliza el código anterior para solicitar al usuario que proporcione 6 números de 2 cifras válidos como base para los números aleatorios y para generar los números aleatorios basados en los números base proporcionados. Una vez que se han generado los números aleatorios, se muestran en pantalla.

#Después de mostrar los números aleatorios generados, el programa pregunta al usuario si desea continuar. Si el usuario ingresa "n" o "N", el bucle se rompe y el programa termina.


import random

# Función que pide al usuario un número de 2 cifras y lo valida.
def pedir_numero():
    while True:
        num = input("Introduce un número de dos cifras entre 00 y 99: ")
        if len(num) == 2 and num.isdigit() and 0 <= int(num) <= 99:
            return int(num)
        else:
            print("El número introducido no es válido.")

# Bucle principal.
while True:
    # Pide al usuario que introduzca 6 números de 2 cifras como base.
    numeros_base = []
    for i in range(5):
        base = pedir_numero()
        numeros_base.append(base)

    # Genera 6 números aleatorios de 2 cifras basados en la lista de números base.
    numeros_aleatorios = []
    for base in numeros_base:
        num = random.randint(0, 99)
        while num == base:
            num = random.randint(0, 99)
        numeros_aleatorios.append(num)

    # Muestra los números aleatorios generados.
    print("Los números aleatorios generados son:", numeros_aleatorios)

    # Pregunta al usuario si desea continuar.
    continuar = input("¿Desea continuar? (S/N) ").lower()
    if continuar == "n":
        break

