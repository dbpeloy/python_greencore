#!/usr/bin/env python
# coding: utf-8
'''
`os` es un módulo incorporado de Python que proporciona una forma de utilizar funcionalidades 
del sistema operativo en el que se está ejecutando Python.

Al importar el módulo os, podemos acceder a una variedad de funciones y constantes que nos 
permiten realizar operaciones en el sistema operativo subyacente, como manipulación de archivos, 
gestión de procesos, variables de entorno, entre otras.

Algunas de las funciones más comunes de os incluyen:

os.getcwd(): Devuelve el directorio de trabajo actual como una cadena.
os.listdir(path): Devuelve una lista de los nombres de archivo en el directorio especificado.
os.path.join(path, *paths): Une uno o más componentes de ruta de manera inteligente.
os.path.exists(path): Devuelve True si la ruta especificada existe, de lo contrario, devuelve False.
Es importante tener en cuenta que las funcionalidades que proporciona el módulo os pueden 
variar según el sistema operativo en el que se está ejecutando Python.
'''
# Pedir 4 numeros de 1 o 2 cifras, que sean mayor que 0 pero menor que 40
# Crear un archivo en el sistema operativo que almecene los numeros
# Hacer validaciones

import os

# Forma de validar que sean 4 numeros enteros de 0 a 40
numeros = []
for i in range(4):
    numero = int(input("Ingrese 4 números [1 o 2 cifras] Mayor que 0 - Menor que 40{}: ".format(i+1)))
    if numero.isdigit():
        while not (0 <= base <= 40):
            print("Error: NumIvalido ")
            numero = int(input("Ingrese número base de 1 o 2 cifras {}: ".format(i+1)))numeros.append(numero)
            # Crear el archivo de salida
            filename = "Num_Data_{}.txt".format(os.popen("date '+%Y%m%d%H%M%S'").read().strip())
            with open(filename, "w") as f:
            # Escribir encabezado con los números bases
            f.write("Los numeros escritos son: {}\n\n".format(numeros))
      else
        print("Ingrese solo números")

