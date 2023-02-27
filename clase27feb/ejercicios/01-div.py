# Ver si el numero dado es divisible entre 2,3 y 5

num = 1
while num <= 100:
    # Verificar aqui si el número es divisible por 2, 3 y 5
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        print(num,"*", end="")
        num += 1
    else:
        print(num, end="")
    # Agrega una coma y un espacio después de cada número
    print(", ", end="")
    num += 1
