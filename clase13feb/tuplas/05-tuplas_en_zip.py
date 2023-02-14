#Zipping Tuples
#El método zip() toma varios objetos de secuencia y devuelve un objeto iterable haciendo coincidir sus elementos. Para obtener más información sobre cómo comprimir tuplas, considere el siguiente ejemplo.
#Supongamos que tenemos tres tuplas diferentes que contienen los datos personales de cuatro clientes. Queremos crear una sola tupla que contenga los datos correspondientes para cada cliente, incluido su nombre, apellido y edad, en forma de tuplas separadas:

first_names = ('Simon', 'Sarah', 'Mehdi', 'Fatime')
last_names = ('Sinek', 'Smith', 'Lotfinejad', 'Lopes')
ages = (49, 55, 39, 33)
zipped = zip(first_names, last_names,ages)
print(zipped)



customers = tuple(zipped)
print(customers)
