# Ir trabajando poco a poco en un calculadora


# Aqui trabajamos el Menu en un ciclo `while`

from tkinter import *  
  
top = Tk()  
  
def hello():  
    print("Hola Fabi !")  
  
# create a toplevel menu  
menubar = Menu()  
menubar.add_command(label=" Hola! ", command=hello)  
menubar.add_command(label=" Salir! ", command=top.quit)  
  
# display the menu  
top.config(menu=menubar)  
  
top.mainloop()  
