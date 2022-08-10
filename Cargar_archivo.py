from curso_model import Curso
from gestionar_curso import DB
from tkinter import *
from tkinter import ttk

class CargarArchivo():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Cargar Archivos")
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

    def ir_pantalla(self):
        self.ventana.destroy()
        Menu()

    def ventana_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE")
        self.frame.config(width = "580", height = "330")
        self.frame.config(relief = "ridge")
        self.frame.config(bd = 12)
        nombre_curso = Label(self.frame, text = "2da ventana", bg = "#F9E1BE", font = ("Comic Sans MS", 17))
        nombre_curso.place(x = 72, y = 20)

        btn_Salir = Button(self.frame, text = "Salir", width = 11,command = self.ir_pantalla, height = 2, font = ("Arial", 10), bg = "#E7C09C")
        btn_Salir.place(x = 115, y = 215)

        self.frame.mainloop() 

        

    almacen_cursos = [] #[['017', 'Social Humanística 1', '7', '8', '1', '4', '0\n'], ...,  [...]]

    with open("entrada.LFP", "r") as archivo:
        lista_cursos = archivo.readlines()

    # Almacenar cada linea en otra lista individual
    for linea_curso in lista_cursos:
        #print(linea.rstrip())
        almacen_cursos.append(linea_curso.split(","))

    #---------------------------------------------------------------------

    print("---------------------CAMBIO-----------------------------")
    for curso in almacen_cursos:
        indice_curso = almacen_cursos.index(curso)
        print(indice_curso)
        print(almacen_cursos[indice_curso])
        print("atributos: ")

        for atributos in (almacen_cursos[indice_curso]):
            indice_atributos = (almacen_cursos[indice_curso]).index(atributos)
            print(atributos)

            print("puntos: ","[",indice_curso,"]","[",indice_atributos,"]")

            nombre = almacen_cursos[indice_curso][indice_atributos]
        
        print("..............................................")
    
    #curso = Curso()