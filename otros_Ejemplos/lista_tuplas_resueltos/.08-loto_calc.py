# Este código utiliza dos bucles while. El primer bucle solicita al usuario que proporcione un número de 2 cifras válido como base para los números aleatorios. Si el usuario introduce un número inválido, el programa le pedirá que lo vuelva a intentar hasta que proporcione un número válido.

# Una vez que se ha establecido el número base, el segundo bucle generará un número aleatorio de 2 cifras y lo mostrará en pantalla. A diferencia del código anterior, este código genera un número aleatorio de 2 cifras que siempre estará entre 00 y 99, y puede o no puede ser igual al número base introducido por el usuario.

# El programa continuará pidiendo al usuario que genere otro número aleatorio hasta que el usuario indique que ya no desea generar más números.



import random

while True:
    # Pide al usuario que introduzca un número de 2 cifras como base.
    while True:
        base = input("Introduce un número de dos cifras entre 00 y 99: ")
        if len(base) == 2 and base.isdigit() and 0 <= int(base) <= 99:
            base = int(base)
            break
        else:
            print("El número introducido no es válido.")

    # Genera un número aleatorio de 2 cifras.
    num = random.randint(0, 99)

    # Muestra el número generado.
    print("El número aleatorio generado es:", num)

    # Pregunta al usuario si desea generar otro número aleatorio.
    respuesta = input("¿Desea generar otro número aleatorio? (S/N) ")
    if respuesta.upper() != "S":
        break

