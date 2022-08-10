from tkinter import *
from tkinter import ttk
from cargar_archivo import CargarArchivo

class Menu():
  def __init__(self):
    self.ventana = Tk()
    self.ventana.title("Menú Principal")
    self.ventana.iconbitmap("Extras/logo.ico")
    self.ventana.resizable(0,0)
    self.ventana.config(bg = "#BB0D6A")
    self.ventana.config(relief = "flat")
    self.ventana.config(bd = 16)
    self.centrar(self.ventana, 600, 350)
    self.ventana.geometry("600x350")
    self.ventana_frame()

  def centrar(self, ventana, ancho, alto):
    altura_pantalla = ventana.winfo_screenheight()
    ancho_pantalla = ventana.winfo_screenwidth()
    x = (ancho_pantalla//2) - (ancho//2)
    y = (altura_pantalla//2) - (alto//2)
    ventana.geometry(f"+{x}+{y}")

  def ventana_frame(self):
    self.frame = Frame()
    self.frame.pack()
    self.frame.config(bg = "#F9E1BE")
    self.frame.config(width = "580", height = "330")
    self.frame.config(relief = "ridge")
    self.frame.config(bd = 12)

    # Labels
    nombre_curso = Label(self.frame, text = "Lenguajes Formales y de Programación", bg = "#F9E1BE", font = ("Comic Sans MS", 17))
    nombre_curso.place(x = 72, y = 20)

    nombre_estudiante = Label(self.frame, text = "Harry Aaron Gómez Sanic", bg = "#F9E1BE", bd = 0, font = ("Arial", 12))
    nombre_estudiante.place(x = 80, y = 100)

    carnet_estudiante = Label(self.frame, text = "carnet: 202103718", bg = "#F9E1BE", bd = 0, font = ("Arial", 12))
    carnet_estudiante.place(x = 80, y = 140)

    #BOTONES

    btn_CargarArchivo = Button(self.frame, text = "Cargar Archivos",command = self.ir_pantalla, width = 19, height = 2, font = ("Arial", 9), bg = "#D5A273")
    btn_CargarArchivo.place(x = 335, y = 80)

    btn_GestionarCursos = Button(self.frame, text = "Gestionar Archivos", width = 19, height = 2, font = ("Arial", 9), bg = "#D5A273")
    btn_GestionarCursos.place(x = 335, y = 155)

    btn_ConteoCreditos = Button(self.frame, text = "Conteo de Créditos", width = 19, height = 2, font = ("Arial", 9), bg = "#D5A273")
    btn_ConteoCreditos.place(x = 335, y = 230)

    btn_Salir = Button(self.frame, text = "Salir", width = 11, height = 2, font = ("Arial", 10), bg = "#E7C09C")
    btn_Salir.place(x = 115, y = 215)

    self.frame.mainloop()  

  def ir_pantalla(self):
    self.ventana.destroy()
    CargarArchivo()

Menu()