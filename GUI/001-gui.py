import tkinter as tk

# Creamos la ventana
ventana = tk.Tk()

# Añadimos un título a la ventana
ventana.title("Ejemplo de ventana con botón")

# Creamos un botón
boton = tk.Button(ventana, text="Haz clic aquí")

# Colocamos el botón en la ventana
boton.pack()

# Iniciamos el loop principal de la aplicación
ventana.mainloop()

