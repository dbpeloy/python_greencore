while True:
    palabra = input("Ingresa una palabra: ")
    if palabra.isalpha():
        break
    else:
        print("Error: Ingresa solo letras.")

