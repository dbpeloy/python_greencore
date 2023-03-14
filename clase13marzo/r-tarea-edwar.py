#!/usr/bin/env python
# coding: utf-8

# Solución basada en la respuesta de Edwar, disponible en:
# https://github.com/dbpeloy/python_greencore/blob/main/clase13marzo/intento-tarea-edwar.py
#

'''
Ciclo para contar del 1 al 100
Ejercicio de mate
Imprima los números del 1 al 100, agregando un caracter especial si el número es divisible entre 2, 3 o 5.

Ciclo para contar del 1 al 100

Intentando resolver
'''

def pedir_numero(titulo):
    numero=input(titulo)
    if numero.isnumeric() :
        return int(numero)
    else :
        print("Error. Por favor ingrese un número entero.")
        return pedir_numero(titulo)

 
# Pedir número inicial y final de la lista que se va a recorrer
inicio = pedir_numero("Ingrese el número inicial de la lista......: ")
fin = pedir_numero("Ingrese el número final de la lista........: ")

# Pedir los divisores
divisores=[]
while True :
    divactual=pedir_numero("Divisores actuales.......: "+str(divisores)+"\nIngrese el siguiente divisor | Digite 0 para terminar...:")
    if divactual == 0 :
        if len(divisores) > 0 :
            break
        else :
            print("Error. Divisores esta vac¡o. Debe ingresar un numero!!")
    else :
        divisores.append(divactual)
for i in range(inicio, fin+1) :
    print("El número actual es",i)
    for d in divisores :
        if i % d == 0 :
            print("{} es divisible por {}.".format(i,d))

# Falta 0 para Terminar
