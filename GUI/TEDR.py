from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(event=None):
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
    window.title(f"Thecleverprogrammer - {filepath}")

def save_file(event=None):
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
    window.title(f"Thecleverprogrammer - {filepath}")

def exit_editor(event=None):
    window.destroy()

window = Tk()
window.title("Thecleverprogrammer")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save As...", command=save_file)

# Add menu and keyboard shortcuts
menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", accelerator="Ctrl+O", command=open_file)
file_menu.add_command(label="Save As...", accelerator="Ctrl+S", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=exit_editor)
menu_bar.add_cascade(label="File", menu=file_menu)
window.config(menu=menu_bar)

# Bind keyboard shortcuts
window.bind("<Control-o>", open_file)
window.bind("<Control-s>", save_file)
window.bind("<Control-q>", exit_editor)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()

