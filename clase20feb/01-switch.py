def switch(value):
    if value == 1:
        return "uno"
    if value == 2:
        return "dos"
    if value == 42:
        return "La respuesta a la vida, el universo y todo lo demás."
    raise Exception("¡No se encontró valor!")
