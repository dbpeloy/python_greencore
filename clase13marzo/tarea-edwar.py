# Ciclo para contar del 1 al 100
# Ejercicio de mate
# Imprima los números del 1 al 100, agregando un caracter especial si el número es divisible entre 2, 3 o 5.

# Ciclo para contar del 1 al 100


# Funcion para imprimir listas de divisibles en columnas

#def divisibles(lista_numeros, lista_divisores) :
 #   for num in range(1, 101):
        # Verificando si el número es divisible por 2, 3 y 5
  #      if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
   #         print('{:>6}'.format(num),"*", end="")
    #    else:
     #       print('{:>6}'.format(num), end="  ")
      #  if num % 10 == 0 :
       #     print("")
#num=1
#lista[]
#while num!=0 :
 #   num=(int(input("[ Agregue numero a la lista |  0 para Terminar]")))
  #  if num == 0 :
   #     break
    #lista.append(num)
    #print(lista)

#divisibles(lista, None)

# Intentando 

# Pedir al usuario el número inicial y final de la lista
inicio = int(input("Ingrese el número inicial de la lista: "))
fin = int(input("Ingrese el número final de la lista: "))

# Pedir al usuario los tres números divisores
divisor1 = int(input("Ingrese el primer número divisor: "))
divisor2 = int(input("Ingrese el segundo número divisor: "))
divisor3 = int(input("Ingrese el tercer número divisor: "))

# Crear la lista de números
numeros = list(range(inicio, fin+1))

# Crear una nueva lista con los números divisibles por los tres divisores
divisibles = [num for num in numeros if num % divisor1 == 0 and num % divisor2 == 0 and num % divisor3 == 0]

# Imprimir los números divisibles encontrados
print("Los números divisibles por", divisor1, divisor2, "y", divisor3, "son:", divisibles)

