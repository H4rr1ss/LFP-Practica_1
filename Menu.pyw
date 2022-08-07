from tkinter import *

# Creación de ventana
ventana = Tk()

# Diseño
ventana.title("Menú Principal")
ventana.iconbitmap("logo.ico")
ventana.resizable(0,0)
#ventana.geometry("580x340")
ventana.config(bg = "#BB0D6A")
ventana.config(relief = "flat")
ventana.config(bd = 16)

frame = Frame()
frame.pack()
frame.config(bg = "#F9E1BE")
frame.config(width = "580", height = "340")
frame.config(relief = "ridge")
frame.config(bd = 12)

ventana.mainloop()