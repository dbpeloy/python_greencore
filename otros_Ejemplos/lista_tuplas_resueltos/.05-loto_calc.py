# Generación de 10 números aleatorios entre 1 y 100 sin repetición   
import random  
#creamos una lista con un primer número aleatorio  
lista=[random.randrange(100)+1] #el primer número nunca se repite  
n=1 #n indica la cantidad de números en la lista  
while n<6:  
 x=random.randrange(100)+1  
 norepe=True #suponemos inicialmente que el número generado no está repetido  
 while norepe:  
  for j in range(len(lista)):  
   if x==lista[j]:  
    norepe=False #aquí hemos detectado que el número si esta repetido  
  if norepe:  
   lista.append(x)  
   n+=1  
print(lista)  
