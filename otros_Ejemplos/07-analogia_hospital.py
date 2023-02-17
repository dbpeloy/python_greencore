# Imagina que administras un hospital que trata a pacientes con una sola enfermedad. Tienes:
# Un plan de tratamiento: [3] Cada paciente recibe 3 unidades de la cura en su primer día.
# Una lista de pacientes: [1 2 3 4 5] Su número de pacientes para la semana (1 persona el lunes, 2 personas el martes, etc.).
# Pregunta: ¿Cuánto medicamento usa cada día?
#  Bueno, eso es solo una multiplicación rápida:

# Plan  *  Patients       = Daily Usage
# [3]   *  [1 2 3 4 5]    = [3 6 9 12 15]

# Codigo

plan = 3
pacientes = [1,2,3,4,5]
#uso_diario = plan * pacientes
#print(uso_diario)


for i in [pacientes]:
    try:
        print('Dia1',pacientes * (plan)(i))
        i = i +1
    except ValueError as err:
        print('Error computing factorial({}): {}'.format(i, err))
