from tkinter import *

class gestion_cursos():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Gestionar Curso")
        self.ventana.iconbitmap("Extras/logo.ico")
        self.ventana.resizable(0,0)
        self.ventana.config(bg = "#BB0D6A", relief = "flat", bd = 16)
        self.centrar(self.ventana, 350, 320)
        self.ventana.geometry("350x320")
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
        self.frame.config(bg = "#F9E1BE", width = "330", height = "300", relief = "ridge", bd = 12)

        # BUTTON------
        self.btn_Lista_cursos = Button(self.frame, text = "Listar Cursos",width = 14, height = 1, font = ("Arial", 9), bg = "#E7C09C")
        self.btn_Lista_cursos.place(x = 90, y = 24)

        self.btn_Agregar_curso = Button(self.frame, text = "Agregar Curso", width = 14, height = 1, font = ("Arial", 9), bg = "#E7C09C")
        self.btn_Agregar_curso.place(x = 90, y = 69)

        self.btn_Editar_curso = Button(self.frame, text = "Editar Curso", width = 14, height = 1, font = ("Arial", 9), bg = "#E7C09C")
        self.btn_Editar_curso.place(x = 90, y = 117)

        self.btn_Eliminar_curso = Button(self.frame, text = "Eliminar Curso", width = 14, height = 1, font = ("Arial", 9), bg = "#E7C09C")
        self.btn_Eliminar_curso.place(x = 90, y = 165)  

        self.btn_Regresar = Button(self.frame, text = "Regresar", width = 10, height = 1, font = ("Arial", 9), bg = "#E7C09C")
        self.btn_Regresar.place(x = 103, y = 214)      

        self.frame.mainloop() 

    #def imprimir_nombre(self, curso):
        #print("--------")
        #hola = curso.getNombre()
        #print(hola)


DB = gestion_cursos()