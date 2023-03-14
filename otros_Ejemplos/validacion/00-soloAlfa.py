#!/usr/bin/env python
# coding: utf-8

'''
Validación de entrada de usuario
Es importante siempre validar los datos que se van a leer desde teclado, sea cual sea su tipo. 
Para avisarle al usuario de su error se utilizan las excepciones y es indispensable volver 
a solicitarle la información, por lo que estas siempre van dentro de ciclos que concluyen su 
ejecución hasta que la entrada sea correcta.
'''

# Fuente: https://codingornot.com/08-python-validar-entradas-ejemplos
# En el siguiente script se está validando que el usuario introduzca un entero.

def lee_entero():
   while True:
       entrada = raw_input("Escribe un numero entero: ")
       try:
           entrada = int(entrada)
           return entrada
       except ValueError:
           print ("La entrada es incorrecta: escribe un numero entero")
