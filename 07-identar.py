# Asignacion de variables

A=1
B=1

# Condicion

if (A>B) : 
     #Esto se ejecuta solamente si A es mayor que B
     print("A es mayor que B")
     A=A+1
else :
    if  (A<B) :
        print("A es menor que B")
        A=A/B
    else : 
        print("A y B son iguales!")

# Imprimir resultados
print("A vale", A," y B vale", B)
