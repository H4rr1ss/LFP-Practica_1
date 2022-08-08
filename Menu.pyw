from tkinter import *

# Creación de ventana
ventana = Tk()

# --------------------------------------------DISEÑO--------------------------------------------
ventana.title("Menú Principal")
ventana.iconbitmap("Extras/logo.ico")
ventana.resizable(0,0)
ventana.config(bg = "#BB0D6A")
ventana.config(relief = "flat")
ventana.config(bd = 16)

frame = Frame()
frame.pack()
frame.config(bg = "#F9E1BE")
frame.config(width = "580", height = "330")
frame.config(relief = "ridge")
frame.config(bd = 12)

# Labels
nombre_curso = Label(frame, text = "Lenguajes Formales y de Programación", bg = "#F9E1BE", font = ("Comic Sans MS", 17))
nombre_curso.place(x = 72, y = 20)

nombre_estudiante = Label(frame, text = "Harry Aaron Gómez Sanic", bg = "#F9E1BE", bd = 0, font = ("Arial", 12))
nombre_estudiante.place(x = 80, y = 100)

carnet_estudiante = Label(frame, text = "carnet: 202103718", bg = "#F9E1BE", bd = 0, font = ("Arial", 12))
carnet_estudiante.place(x = 80, y = 140)

# Botones
def v_Carga():
    print("hola")

#def v_Gestionar():
  #  print("hola")

#def v_Conteo():
   # print("hola")

btn_CargarArchivo = Button(frame, text = "Cargar Archivos", command = v_Carga, width = 19, height = 2, font = ("Arial", 9), bg = "#D5A273")
btn_CargarArchivo.place(x = 335, y = 80)

btn_GestionarCursos = Button(frame, text = "Gestionar Archivos", width = 19, height = 2, font = ("Arial", 9), bg = "#D5A273")
btn_GestionarCursos.place(x = 335, y = 155)

btn_ConteoCreditos = Button(frame, text = "Conteo de Créditos", width = 19, height = 2, font = ("Arial", 9), bg = "#D5A273")
btn_ConteoCreditos.place(x = 335, y = 230)

btn_Salir = Button(frame, text = "Salir", width = 11, height = 2, font = ("Arial", 10), bg = "#E7C09C")
btn_Salir.place(x = 115, y = 215)

ventana.mainloop()