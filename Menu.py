from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from curso_model import Curso
from database import DB
# -------------------------------------------------------------MENÚ----------------------------------------------------------------------
class Menu():
  def __init__(self):
    self.General_ventana()
    self.ventana.title("Menú Principal")
    self.centrar(self.ventana, 600, 350)
    self.ventana.geometry("600x350")
    self.ventana_frame()

  def General_ventana(self):
    self.ventana = Tk()
    self.ventana.iconbitmap("Extras/logo.ico")
    self.ventana.resizable(0,0)
    self.ventana.config(bg = "#BB0D6A", relief = "flat", bd = 16)

  def centrar(self, ventana, ancho, alto):
    altura_pantalla = ventana.winfo_screenheight()
    ancho_pantalla = ventana.winfo_screenwidth()
    x = (ancho_pantalla//2) - (ancho//2)
    y = (altura_pantalla//2) - (alto//2)
    ventana.geometry(f"+{x}+{y}")
  
  # Cambio de pantallas---------------
  def __ir_pantalla_cargar_curso(self):
    self.ventana.destroy()
    CargarArchivo()

  def __ir_pantalla_gestion_curso(self):
    self.ventana.destroy()
    Gestion_cursos()
  # ----------------------------------
  def ventana_frame(self):
    self.frame = Frame()
    self.frame.pack()
    self.frame.config(bg = "#F9E1BE", width = "580", height = "330", relief = "ridge", bd = 12)

    # LABELS-----
    self.__lbl_Nombre_curso = Label(self.frame, text = "Lenguajes Formales y de Programación", bg = "#F9E1BE", font = ("Comic Sans MS", 17))
    self.__lbl_Nombre_curso.place(x = 72, y = 20)

    self.__lbl_Nombre_estudiante = Label(self.frame, text = "Harry Aaron Gómez Sanic", bg = "#F9E1BE", bd = 0, font = ("Arial", 12))
    self.__lbl_Nombre_estudiante.place(x = 80, y = 100)

    self.__lbl_Carnet_estudiante = Label(self.frame, text = "carnet: 202103718", bg = "#F9E1BE", bd = 0, font = ("Arial", 12))
    self.__lbl_Carnet_estudiante.place(x = 80, y = 140)

    # BUTTON-----
    self.__btn_CargarArchivo = Button(self.frame, text = "Cargar Archivos",command = self.__ir_pantalla_cargar_curso, width = 19, height = 2, font = ("Arial", 9), bg = "#D5A273")
    self.__btn_CargarArchivo.place(x = 335, y = 80)

    self.__btn_GestionarCursos = Button(self.frame, text = "Gestionar Archivos", command = self.__ir_pantalla_gestion_curso, width = 19, height = 2, font = ("Arial", 9), bg = "#D5A273")
    self.__btn_GestionarCursos.place(x = 335, y = 155)

    self.__btn_ConteoCreditos = Button(self.frame, text = "Conteo de Créditos", width = 19, height = 2, font = ("Arial", 9), bg = "#D5A273")
    self.__btn_ConteoCreditos.place(x = 335, y = 230)

    self.__btn_Salir = Button(self.frame, text = "Salir", width = 11, height = 2, font = ("Arial", 10), bg = "#E7C09C")
    self.__btn_Salir.place(x = 115, y = 215)

    self.frame.mainloop()  



# ----------------------------------------------------------CARGAR-ARCHIVOS-------------------------------------------------------------------------
class CargarArchivo(Menu):
  def __init__(self):
    super().General_ventana()
    self.ventana.title("Cargar Archivos")
    super().centrar(self.ventana, 600, 300)
    self.ventana.geometry("600x300")
    self.ventana_frame()

  def __ir_pantalla_menu(self):
    self.ventana.destroy()
    Menu()

  def __Insertar_archivo(self):
    self.almacen_cursos = [] #[['017', 'Social Humanística 1', '7', '8', '1', '4', '0\n'], ...,  [...]]
    ruta = self.__tb_Ruta.get()
    with open("entrada.LFP", "r") as archivo:
      self.lista_cursos = archivo.readlines()

    # Almacenar cada linea en otra lista individual
    for linea_curso in self.lista_cursos:
      self.almacen_cursos.append(linea_curso.split(","))

    for curso in self.almacen_cursos:
      indice_curso = self.almacen_cursos.index(curso)
        
      codigo = self.almacen_cursos[indice_curso][0]
      nombre = self.almacen_cursos[indice_curso][1]
      prerequisito = self.almacen_cursos[indice_curso][2]
      obligatorio = self.almacen_cursos[indice_curso][3]
      semestre = self.almacen_cursos[indice_curso][4]
      creditos = self.almacen_cursos[indice_curso][5]
      estado = self.almacen_cursos[indice_curso][6]

      curso = Curso(codigo, nombre, prerequisito, obligatorio, semestre, creditos, estado)
      DB.Crear_curso(curso)
    tkinter.messagebox.showinfo("Confirmación", "Archivo cargado exitosamente!")

  def ventana_frame(self):
    self.frame = Frame()
    self.frame.pack()
    self.frame.config(bg = "#F9E1BE", width = "580", height = "280", relief = "ridge", bd = 12)

    # LABEL-----
    self.__lbl_Ruta = Label(self.frame, text = "Ruta", bg = "#F9E1BE", font = ("Comic Sans MS", 13))
    self.__lbl_Ruta.place(x = 85, y = 75)

    # TEXFIELD-----
    self.__tb_Ruta = Entry(self.frame, font = "Arial", width = 29, justify = "center")
    self.__tb_Ruta.place(x = 135, y = 78)

    # BUTTON------
    self.__btn_Seleccionar = Button(self.frame, text = "Seleccionar", command = self.__Insertar_archivo, width = 13, height = 2, font = ("Arial", 9), bg = "#E7C09C")
    self.__btn_Seleccionar.place(x = 145, y = 147)

    self.__btn_Regresar = Button(self.frame, text = "Regresar", command = self.__ir_pantalla_menu, width = 13, height = 2, font = ("Arial", 9), bg = "#E7C09C")
    self.__btn_Regresar.place(x = 310, y = 147)

    self.frame.mainloop()



# ---------------------------------------------------------GESTIONAR-ARCHIVOS-------------------------------------------------------------------------
class Gestion_cursos(Menu):
  def __init__(self):
    super().General_ventana()
    self.ventana.title("Gestionar Curso")
    super().centrar(self.ventana, 350, 320)
    self.ventana.geometry("350x320")
    self.ventana_frame()

  def __ir_pantalla_menu(self):
    self.ventana.destroy()
    Menu()

  def __ir_pantalla_listar_curso(self):
    self.ventana.destroy()
    listar_cursos()

  def __ir_pantalla_agregar_curso(self):
    self.ventana.destroy()
    Agregar_curso()

  def __ir_pantalla_editar_curso(self):
    self.ventana.destroy()
    Editar_curso()
    
  def __ir_pantalla_eliminar_curso(self):
    self.ventana.destroy()
    Eliminar_curso()
    
  def ventana_frame(self):
    self.frame = Frame()
    self.frame.pack()
    self.frame.config(bg = "#F9E1BE", width = "330", height = "300", relief = "ridge", bd = 12)

    # BUTTON------
    self.__btn_Lista_cursos = Button(self.frame, text = "Listar Cursos",width = 14, command = self.__ir_pantalla_listar_curso,  height = 1, font = ("Arial", 9), bg = "#E7C09C")
    self.__btn_Lista_cursos.place(x = 90, y = 24)

    self.__btn_Agregar_curso = Button(self.frame, text = "Agregar Curso", width = 14, command = self.__ir_pantalla_agregar_curso, height = 1, font = ("Arial", 9), bg = "#E7C09C")
    self.__btn_Agregar_curso.place(x = 90, y = 69)

    self.__btn_Editar_curso = Button(self.frame, text = "Editar Curso", width = 14, command = self.__ir_pantalla_editar_curso, height = 1, font = ("Arial", 9), bg = "#E7C09C")
    self.__btn_Editar_curso.place(x = 90, y = 117)

    self.__btn_Eliminar_curso = Button(self.frame, text = "Eliminar Curso", width = 14, command = self.__ir_pantalla_eliminar_curso, height = 1, font = ("Arial", 9), bg = "#E7C09C")
    self.__btn_Eliminar_curso.place(x = 90, y = 165)  

    self.__btn_Regresar = Button(self.frame, text = "Regresar", command = self.__ir_pantalla_menu, width = 10, height = 1, font = ("Arial", 9), bg = "#E7C09C")
    self.__btn_Regresar.place(x = 103, y = 214)      

    self.frame.mainloop() 

# ----------------------------------------------------------LISTAR-CURSOS-------------------------------------------------------------------------
class listar_cursos(Menu):
  def __init__(self):
    super().General_ventana()
    self.ventana.title("Listar Cursos")
    super().centrar(self.ventana, 800, 460)
    self.ventana.geometry("800x460")
    self.Ventana_frame()

  def __ir_pantalla_gestion_curso(self):
    self.ventana.destroy()
    Gestion_cursos()

  def __Mostrar_tabla(self):
    self.tabla = ttk.Treeview(self.frame, columns = ("#0", "#1", "#2", "#3", "#4", "#5"), height = 15)
    self.tabla.grid(row = 7, column = 0, columnspan = 2)
    self.tabla.place(x = 22, y = 25)

    self.tabla.column("#0", width = 57)
    self.tabla.column("#1", width = 175, anchor = CENTER)
    self.tabla.column("#2", width = 175, anchor = CENTER)
    self.tabla.column("#3", width = 63, anchor = CENTER)
    self.tabla.column("#4", width = 70, anchor = CENTER)
    self.tabla.column("#5", width = 60, anchor = CENTER)
    self.tabla.column("#6", width = 100, anchor = CENTER)

    self.tabla.heading("#0", text = "Codigo", anchor = CENTER)
    self.tabla.heading("#1", text = "Nombre", anchor = CENTER)
    self.tabla.heading("#2", text = "Pre-requisito", anchor = CENTER)
    self.tabla.heading("#3", text = "Semestre", anchor = CENTER)
    self.tabla.heading("#4", text = "Obligatorio", anchor = CENTER)
    self.tabla.heading("#5", text = "Créditos", anchor = CENTER)
    self.tabla.heading("#6", text = "Estado", anchor = CENTER)
    
    cursos = DB.Recibir_curso()

    for curso in cursos:
      indice_curso = cursos.index(curso)
      
      codigo = cursos[indice_curso].getCodigo()
      nombre = cursos[indice_curso].getNombre()
      prerequisito = cursos[indice_curso].getPrerequisito()
      obligatorio = cursos[indice_curso].getObligatorio()
      semestre = cursos[indice_curso].getSemestre()
      creditos = cursos[indice_curso].getCreditos()
      estado = cursos[indice_curso].getEstado()
      self.tabla.insert("", END, text = codigo, values = (nombre, prerequisito, obligatorio, semestre, creditos, estado))

  def Ventana_frame(self):
    self.frame = Frame()
    self.frame.pack()
    self.frame.config(bg = "#F9E1BE", width = "780", height = "430", relief = "ridge", bd = 12)
    self.__Mostrar_tabla()

    # BUTTON------
    self.__btn_Regresar = Button(self.frame, text = "Regresar", command = self.__ir_pantalla_gestion_curso, width = 14, height = 1, font = ("Arial", 9), bg = "#E7C09C")
    self.__btn_Regresar.place(x = 580, y = 364)
    
    self.frame.mainloop() 



# ---------------------------------------------------------AGREGAR-CURSO-------------------------------------------------------------------------
class Agregar_curso(Menu):
  def __init__(self):
    super().General_ventana()
    self.ventana.title("Agregar Curso")
    super().centrar(self.ventana, 670, 465)
    self.ventana.geometry("670x465")
    self.ventana_frame()

  def __ir_pantalla_gestion_curso(self):
    self.ventana.destroy()
    Gestion_cursos()

  def __btn_Agregar_curso(self):
    
    curso = Curso(self.__tb_Codigo.get(), self.__tb_Nombre.get(), self.__tb_Prerequisito.get(), self.__tb_Obligatorio.get(), self.__tb_Semestre.get(), self.__tb_Creditos.get(), self.__tb_Estado.get())
    DB.Crear_curso(curso)
    tkinter.messagebox.showinfo("Confirmación", "¡Curso agregado exitosamente!")

  def ventana_frame(self):
    self.frame = Frame()
    self.frame.pack()
    self.frame.config(bg = "#F9E1BE", width = "650", height = "435", relief = "ridge", bd = 12)

    # LABELS-----
    self.__lbl_Codigo = Label(self.frame, text = "Código:", bg = "#F9E1BE", font = ("Arial", 12))
    self.__lbl_Codigo.place(x = 45, y = 40)

    self.__lbl_Nombre = Label(self.frame, text = "Nombre:", bg = "#F9E1BE", font = ("Arial", 12))
    self.__lbl_Nombre.place(x = 45, y = 90)
    
    self.__lbl_Prerequisito = Label(self.frame, text = "Pre-requisito:", bg = "#F9E1BE", font = ("Arial", 12))
    self.__lbl_Prerequisito.place(x = 45, y = 140)

    self.__lbl_Semestre = Label(self.frame, text = "Semestre:", bg = "#F9E1BE", font = ("Arial", 12))
    self.__lbl_Semestre.place(x = 45, y = 190)

    self.__lbl_Obligatorio = Label(self.frame, text = "Obligatorio:", bg = "#F9E1BE", font = ("Arial", 12))
    self.__lbl_Obligatorio.place(x = 45, y = 240)

    self.__lbl_Creditos = Label(self.frame, text = "Créditos:", bg = "#F9E1BE", font = ("Arial", 12))
    self.__lbl_Creditos.place(x = 45, y = 290)

    self.__lbl_Estado = Label(self.frame, text = "Estado:", bg = "#F9E1BE", font = ("Arial", 12))
    self.__lbl_Estado.place(x = 45, y = 340)

    # TEXFIELD-----
    self.__tb_Codigo = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.__tb_Codigo.place(x = 160, y = 42)

    self.__tb_Nombre = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.__tb_Nombre.place(x = 160, y = 92)

    self.__tb_Prerequisito = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.__tb_Prerequisito.place(x = 160, y = 142)

    self.__tb_Semestre = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.__tb_Semestre.place(x = 160, y = 192)

    self.__tb_Obligatorio = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.__tb_Obligatorio.place(x = 160, y = 242)

    self.__tb_Creditos = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.__tb_Creditos.place(x = 160, y = 292)

    self.__tb_Estado = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.__tb_Estado.place(x = 160, y = 342)

    # BUTTON-----
    self.__btn_Agregar = Button(self.frame, text = "Agregar", command = self.__btn_Agregar_curso, width = 14, height = 3, font = ("Arial", 9), bg = "#E7C09C")
    self.__btn_Agregar.place(x = 487, y = 130)

    self.__btn_Regresar = Button(self.frame, text = "Regresar", command = self.__ir_pantalla_gestion_curso, width = 14, height = 3, font = ("Arial", 9), bg = "#E7C09C")
    self.__btn_Regresar.place(x = 487, y = 225)

    self.frame.mainloop() 
  


# ---------------------------------------------------------EDITAR-CURSO-------------------------------------------------------------------------
class Editar_curso(Menu):
  def __init__(self):
    super().General_ventana()
    self.ventana.title("Editar Curso")
    super().centrar(self.ventana, 670, 465)
    self.ventana.geometry("670x465")
    self.ventana_frame()

  def __ir_pantalla_gestion_curso(self):
    self.ventana.destroy()
    Gestion_cursos()

  def __Mostrar_curso(self):
    curso = DB.Mostrar_curso(self.__tb_Codigo.get())

    if curso is not None:
      self.__tb_Nombre.insert(0, curso.getNombre())
      self.__tb_Prerequisito.insert(0, curso.getPrerequisito())
      self.__tb_Obligatorio.insert(0, curso.getObligatorio())
      self.__tb_Semestre.insert(0, curso.getSemestre())
      self.__tb_Creditos.insert(0, curso.getCreditos())
      self.__tb_Estado.insert(0, curso.getEstado())
    else:
      tkinter.messagebox.showinfo("Error", "El curso con código: "+ self.__tb_Codigo.get() + ", no existe." )
    
  def __Editar_curso(self):
    DB.Actualizar_curso(self.__tb_Codigo.get(), self.__tb_Nombre.get(), self.__tb_Prerequisito.get(), self.__tb_Semestre.get(), self.__tb_Obligatorio.get(), self.__tb_Creditos.get(), self.__tb_Estado.get())
    tkinter.messagebox.showinfo("Confirmación", "¡Curso Editado exitosamente!")

  def ventana_frame(self):
    self.frame = Frame()
    self.frame.pack()
    self.frame.config(bg = "#F9E1BE", width = "650", height = "435", relief = "ridge", bd = 12)

    # LABELS-----
    self.__lbl_Codigo = Label(self.frame, text = "Código:", bg = "#F9E1BE", font = ("Arial", 12))
    self.__lbl_Codigo.place(x = 45, y = 40)

    self.__lbl_Nombre = Label(self.frame, text = "Nombre:", bg = "#F9E1BE", font = ("Arial", 12))
    self.__lbl_Nombre.place(x = 45, y = 90)
    
    self.__lbl_Prerequisito = Label(self.frame, text = "Pre-requisito:", bg = "#F9E1BE", font = ("Arial", 12))
    self.__lbl_Prerequisito.place(x = 45, y = 140)

    self.__lbl_Semestre = Label(self.frame, text = "Semestre:", bg = "#F9E1BE", font = ("Arial", 12))
    self.__lbl_Semestre.place(x = 45, y = 190)

    self.__lbl_Obligatorio = Label(self.frame, text = "Obligatorio:", bg = "#F9E1BE", font = ("Arial", 12))
    self.__lbl_Obligatorio.place(x = 45, y = 240)

    self.__lbl_Creditos = Label(self.frame, text = "Créditos:", bg = "#F9E1BE", font = ("Arial", 12))
    self.__lbl_Creditos.place(x = 45, y = 290)

    self.__lbl_Estado = Label(self.frame, text = "Estado:", bg = "#F9E1BE", font = ("Arial", 12))
    self.__lbl_Estado.place(x = 45, y = 340)

    # TEXFIELD-----
    self.__tb_Codigo = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.__tb_Codigo.place(x = 160, y = 42)

    self.__tb_Nombre = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.__tb_Nombre.place(x = 160, y = 92)

    self.__tb_Prerequisito = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.__tb_Prerequisito.place(x = 160, y = 142)

    self.__tb_Semestre = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.__tb_Semestre.place(x = 160, y = 192)

    self.__tb_Obligatorio = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.__tb_Obligatorio.place(x = 160, y = 242)

    self.__tb_Creditos = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.__tb_Creditos.place(x = 160, y = 292)

    self.__tb_Estado = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.__tb_Estado.place(x = 160, y = 342)

    # BUTTON-----
    self.__btn_Mostrar = Button(self.frame, text = "Mostrar", command = self.__Mostrar_curso, width = 14, height = 3, font = ("Arial", 9), bg = "#E7C09C")
    self.__btn_Mostrar.place(x = 487, y = 100)
    
    self.__btn_Editar = Button(self.frame, text = "Editar", command = self.__Editar_curso, width = 14, height = 3, font = ("Arial", 9), bg = "#E7C09C")
    self.__btn_Editar.place(x = 487, y = 180)

    self.__btn_Regresar = Button(self.frame, text = "Regresar", command = self.__ir_pantalla_gestion_curso, width = 14, height = 3, font = ("Arial", 9), bg = "#E7C09C")
    self.__btn_Regresar.place(x = 487, y = 260)

    self.frame.mainloop() 



# ---------------------------------------------------------ELIMINAR-CURSO-------------------------------------------------------------------------
class Eliminar_curso(Menu):
  def __init__(self):
    super().General_ventana()
    self.ventana.title("Eliminar Curso")
    super().centrar(self.ventana, 515, 235)
    self.ventana.geometry("515x235")
    self.ventana_frame()

  def __ir_pantalla_gestion_curso(self):
    self.ventana.destroy()
    Gestion_cursos()

  def ventana_frame(self):
    self.frame = Frame()
    self.frame.pack()
    self.frame.config(bg = "#F9E1BE", width = "495", height = "215", relief = "ridge", bd = 12)

    # LABEL-----
    self.__lbl_Codigo_curso = Label(self.frame, text = "Código de curso:", bg = "#F9E1BE", font = ("Comic Sans MS", 13))
    self.__lbl_Codigo_curso.place(x = 63, y = 38)

    # TEXFIELD-----
    self.__tb_Codigo_curso = Entry(self.frame, font = "Arial", width = 16, justify = "center")
    self.__tb_Codigo_curso.place(x = 218, y = 41)

    # BUTTON------
    self.__btn_Eliminar = Button(self.frame, text = "Eliminar", width = 13, height = 2, font = ("Arial", 9), bg = "#E7C09C")
    self.__btn_Eliminar.place(x = 98, y = 100)

    self.__btn_Regresar = Button(self.frame, text = "Regresar", command = self.__ir_pantalla_gestion_curso, width = 13, height = 2, font = ("Arial", 9), bg = "#E7C09C")
    self.__btn_Regresar.place(x = 248, y = 100)

    self.frame.mainloop()

Menu()