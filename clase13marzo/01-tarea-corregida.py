# Ciclo para contar del 1 al 100
# Ejercicio de mate
# Imprima los números del 1 al 100, agregando un caracter especial si el número es divisible entre 2, 3 o 5.

# Ciclo para contar del 1 al 100
for num in range(1, 101):
    # Verificando si el número es divisible por 2, 3 y 5
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        print('{:>5}'.format(num),"*", end="")
    else:
        print('{:>5}'.format(num), end="  ")
    if num % 10 == 0 :
        print("")
