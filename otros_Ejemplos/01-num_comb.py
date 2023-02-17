# En este ejemplo, la variable numeros contiene 
# los cuatro números enteros que deseas combinar. 
# La función itertools.combinations genera todas 
# las combinaciones posibles de 4 elementos a partir 
# de esta lista. Luego, el bucle for imprime cada 
# combinación en una línea separada.


import itertools

# Define una lista con los números que quieres combinar
numeros = [1, 2, 3, 4]

# Genera todas las combinaciones de 4 elementos
combinaciones = itertools.combinations(numeros, 4)

# Imprime cada combinación en una línea separada
for combinacion in combinaciones:
    print(combinacion)

