# Función para imprimir listas de divisibles en columnas
def divisibles(lista_numeros, lista_divisores) :
    for num in lista_numeros :
        # Verificando si el número es divisible por los divisores de la lista
            divisible=False
            for divisor in lista_divisores :
                if num % divisor == 0 :
                    divisible=True
            if divisible :
                print('{:>5}'.format(num),"*", end="")
            else:
                print('{:>5}'.format(num), end="  ")
            if num % 10 == 0 :
                print("")

num=1
lista=[]
while num!= 0 :
    num=(int(input("Agregue número a la lista, o 0 para terminar: ")))
    if num == 0 :
        break
    lista.append(num)
    print(lista)

divisibles(lista, [2, 3, 5])
print("")
