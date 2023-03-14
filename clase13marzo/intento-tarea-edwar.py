# Ciclo para contar del 1 al 100
# Ejercicio de mate
# Imprima los números del 1 al 100, agregando un caracter especial si el número es divisible entre 2, 3 o 5.

# Ciclo para contar del 1 al 100

# Intentando resolver
 
# Pedir número inicial y final de la lista que se va a crear
inicio = int(input("Ingrese el número inicial de la lista......: "))
fin = int(input("Ingrese el número final de la lista........: "))

# Pedir los tres números divisores
divisor1 = int(input("Ingrese el primer número divisor...: "))
divisor2 = int(input("Ingrese el segundo número divisor..: "))
divisor3 = int(input("Ingrese el tercer número divisor...: "))

# Crear la lista de números
numeros = list(range(inicio, fin+1))

# Crear una nueva lista con los números divisibles por los tres divisores pero solo me saca los divisibles exactos
# por ejemplo haciendo una lista de 0 a 100 me dice que los números divisibles por 2 3 y 5 son: [30, 60, 90]
# aqui ==> de nuevo el AND y el OR me vacilaron ****
# divisibles = [num for num in numeros if num % divisor1 == 0 and num % divisor2 == 0 and num % divisor3 == 0]

# corregido a OR
divisibles = [num for num in numeros if num % divisor1 == 0 or num % divisor2 == 0 or num % divisor3 == 0]

# Imprimir los números divisibles encontrados
print("Los números divisibles por", divisor1, divisor2, "y", divisor3, "son:", divisibles)

# Falta 0 para Terminar

