def compara_clave(real, intento):
    if real == intento:
        return True
    else:
        return False

clave_secreta = 'mi clave segura'

intento_clave = input("Escriba su clave secreta: ")

if compara_clave(clave_secreta, intento_clave):
    print("Acceso permitido")
else:
    print("Acceso denegado")
