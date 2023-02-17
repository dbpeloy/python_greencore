import random

while True:
    base = input("Introduce un número de dos cifras entre 00 y 99: ")
    if len(base) == 2 and base.isdigit() and int(base) >= 0 and int(base) <= 99:
        base = int(base)
        break
    else:
        print("El número introducido no es válido.")

while True:
    num = (base * 100) + random.choice(range(100))
    print("El número aleatorio generado es:", num)

    respuesta = input("¿Desea generar otro número aleatorio? (S/N) ")
    if respuesta.upper() != "S":
        break

