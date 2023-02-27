# En este código, utilizamos la función zip() para combinar las tres listas lista1, lista2 y lista3 
# en un solo iterador que recorrerá los elementos de cada lista simultáneamente. Luego, utilizamos 
# un solo for loop para recorrer este iterador y desempacar los elementos de cada lista en las variables num, 
# letra y booleano. Finalmente, imprimimos cada variable separada por un espacio.

#Es importante tener en cuenta que la función zip() se detendrá tan pronto como la lista más corta 
# se haya agotado. Es decir, si una de las listas es más corta que las otras, el for loop se 
# detendrá después de haber recorrido todos los elementos de la lista más corta.


lista1 = [1, 2, 3]
lista2 = ["a", "b", "c"]
lista3 = [True, False, True]

# Ciclo para recorrer varias listas simultáneamente
for num, letra, booleano in zip(lista1, lista2, lista3):
    print(num, letra, booleano)

