#!/usr/bin/env python
# coding: utf-8

cadena = input("Ingrese una cadena de texto: ")
while True :
    if cadena.isalpha():
        print("La cadena contiene solo letras")
        break
    else:
        print("La cadena no contiene solo letras")
        break
