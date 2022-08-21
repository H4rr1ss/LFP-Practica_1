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
    self.Ventana_frame()

  def General_ventana(self):
    self.ventana = Tk()
    self.ventana.resizable(0,0)
    self.ventana.config(bg = "#BB0D6A", relief = "flat", bd = 16)

  def centrar(self, ventana, ancho, alto):
    altura_pantalla = ventana.winfo_screenheight()
    ancho_pantalla = ventana.winfo_screenwidth()
    x = (ancho_pantalla//2) - (ancho//2)
    y = (altura_pantalla//2) - (alto//2)
    ventana.geometry(f"+{x}+{y}")
  
  def __ir_pantalla_cargar_curso(self):
    self.ventana.destroy()
    CargarArchivo()

  def __ir_pantalla_gestion_curso(self):
    self.ventana.destroy()
    Gestion_cursos()

  def __ir_pantalla_conteo_creditos(self):
    self.ventana.destroy()
    Conteo_creditos()

  def Ventana_frame(self):
    self.frame = Frame()
    self.frame.pack()
    self.frame.config(bg = "#F9E1BE", width = "580", height = "330", relief = "ridge", bd = 12)

    # LABELS-----
    self.__lbl_Nombre_curso = Label(self.frame, text = "Lenguajes Formales y de Programación", bg = "#F9E1BE", font = ("Comic Sans MS", 17)).place(x = 72, y = 20)

    self.__lbl_Nombre_estudiante = Label(self.frame, text = "Harry Aaron Gómez Sanic", bg = "#F9E1BE", bd = 0, font = ("Arial", 12)).place(x = 80, y = 100)

    self.__lbl_Carnet_estudiante = Label(self.frame, text = "carnet: 202103718", bg = "#F9E1BE", bd = 0, font = ("Arial", 12)).place(x = 80, y = 140)

    # BUTTON-----
    self.__btn_CargarArchivo = Button(self.frame, text = "Cargar Archivos", command = self.__ir_pantalla_cargar_curso, width = 19, height = 2, font = ("Arial", 9), bg = "#D5A273").place(x = 335, y = 80)

    self.__btn_GestionarCursos = Button(self.frame, text = "Gestionar Archivos", command = self.__ir_pantalla_gestion_curso, width = 19, height = 2, font = ("Arial", 9), bg = "#D5A273").place(x = 335, y = 155)

    self.__btn_ConteoCreditos = Button(self.frame, text = "Conteo de Créditos", command = self.__ir_pantalla_conteo_creditos, width = 19, height = 2, font = ("Arial", 9), bg = "#D5A273").place(x = 335, y = 230)

    self.__btn_Salir = Button(self.frame, text = "Salir", command = self.ventana.quit, width = 11, height = 2, font = ("Arial", 10), bg = "#E7C09C").place(x = 115, y = 215)
    self.frame.mainloop()  

# -------------------------------------------------------CARGAR-ARCHIVOS-------------------------------------------------------------------------
class CargarArchivo(Menu):
  def __init__(self):
    super().General_ventana()
    self.ventana.title("Cargar Archivos")
    super().centrar(self.ventana, 600, 300)
    self.ventana.geometry("600x300")
    self.Ventana_frame()

  def __ir_pantalla_menu(self):
    self.ventana.destroy()
    Menu()

  def __Insertar_archivo(self):
    self.almacen_cursos = [] #[['017', 'Social Humanística 1', '7', '8', '1', '4', '0\n'], ...,  [...]]
    if not self.__tb_Ruta.get():
      tkinter.messagebox.showinfo("Error", "Por favor ingrese la ruta.")
    else:
      with open(self.__tb_Ruta.get(), encoding = "utf8") as archivo:
        self.lista_cursos = archivo.readlines()

      # Almacenar cada linea en otra lista individual, Quitar caracteres especiales "\n"
      self.lista_cursos_string = str(list(map(str.strip, self.lista_cursos)))
      self.lista_cursos_entrada = eval(self.lista_cursos_string)

      for linea_curso in self.lista_cursos_entrada:
        self.almacen_cursos.append(linea_curso.split(","))

      for curso in self.almacen_cursos:
        if curso == [""]:
          break
        else:
          indice_curso = self.almacen_cursos.index(curso)
          codigo = self.almacen_cursos[indice_curso][0]
          curso = Curso(codigo, self.almacen_cursos[indice_curso][1], self.almacen_cursos[indice_curso][2], 
          self.almacen_cursos[indice_curso][3], self.almacen_cursos[indice_curso][4], self.almacen_cursos[indice_curso][5], self.almacen_cursos[indice_curso][6])
        
          DB.Crear_curso(curso, codigo)
      tkinter.messagebox.showinfo("Confirmación", "Archivo cargado exitosamente!")

  def Ventana_frame(self):
    self.frame = Frame()
    self.frame.pack()
    self.frame.config(bg = "#F9E1BE", width = "580", height = "280", relief = "ridge", bd = 12)

    # LABEL-----
    self.__lbl_Ruta = Label(self.frame, text = "Ruta", bg = "#F9E1BE", font = ("Comic Sans MS", 13)).place(x = 85, y = 75)

    # TEXFIELD-----
    self.__tb_Ruta = Entry(self.frame, font = "Arial", width = 29, justify = "center")
    self.__tb_Ruta.place(x = 135, y = 78)

    # BUTTON------
    self.__btn_Seleccionar = Button(self.frame, text = "Seleccionar", command = self.__Insertar_archivo, width = 13, height = 2, font = ("Arial", 9), bg = "#E7C09C")
    self.__btn_Seleccionar.place(x = 145, y = 147)

    self.__btn_Regresar = Button(self.frame, text = "Regresar", command = self.__ir_pantalla_menu, width = 13, height = 2, font = ("Arial", 9), bg = "#E7C09C")
    self.__btn_Regresar.place(x = 310, y = 147)
    self.frame.mainloop()

# ---------------------------------------------------GESTIONAR-ARCHIVOS-------------------------------------------------------------------------
class Gestion_cursos(Menu):
  def __init__(self):
    super().General_ventana()
    self.ventana.title("Gestionar Curso")
    super().centrar(self.ventana, 350, 320)
    self.ventana.geometry("350x320")
    self.Ventana_frame()

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
    
  def Ventana_frame(self):
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

# ----------------------------------------------------LISTAR-CURSOS-------------------------------------------------------------------------
class listar_cursos(Menu):
  def __init__(self):
    super().General_ventana()
    self.ventana.title("Listar Cursos")
    super().centrar(self.ventana, 800, 460)
    self.ventana.geometry("800x460")
    self.__Ventana_frame()

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
    self.tabla.column("#3", width = 70, anchor = CENTER)
    self.tabla.column("#4", width = 63, anchor = CENTER)
    self.tabla.column("#5", width = 60, anchor = CENTER)
    self.tabla.column("#6", width = 100, anchor = CENTER)

    self.tabla.heading("#0", text = "Codigo", anchor = CENTER)
    self.tabla.heading("#1", text = "Nombre", anchor = CENTER)
    self.tabla.heading("#2", text = "Pre-requisito", anchor = CENTER)
    self.tabla.heading("#3", text = "Obligatorio", anchor = CENTER)
    self.tabla.heading("#4", text = "Semestre", anchor = CENTER)
    self.tabla.heading("#5", text = "Créditos", anchor = CENTER)
    self.tabla.heading("#6", text = "Estado", anchor = CENTER)
    
    cursos = DB.Recibir_curso()
    for curso in cursos:
      indice_curso = cursos.index(curso)
      codigo = cursos[indice_curso].getCodigo()

      self.tabla.insert("", END, text = codigo, values = (cursos[indice_curso].getNombre(), cursos[indice_curso].getPrerequisito(), cursos[indice_curso].getObligatorio(),
      cursos[indice_curso].getSemestre(), cursos[indice_curso].getCreditos(), cursos[indice_curso].getEstado()))

  def __Ventana_frame(self):
    self.frame = Frame()
    self.frame.pack()
    self.frame.config(bg = "#F9E1BE", width = "780", height = "430", relief = "ridge", bd = 12)
    self.__Mostrar_tabla()

    # BUTTON------
    self.__btn_Regresar = Button(self.frame, text = "Regresar", command = self.__ir_pantalla_gestion_curso, width = 14, height = 1, font = ("Arial", 9), bg = "#E7C09C")
    self.__btn_Regresar.place(x = 580, y = 364)
    self.frame.mainloop() 

# -------------------------------------------------AGREGAR-CURSO-------------------------------------------------------------------------
class Agregar_curso(Menu):
  def __init__(self):
    super().General_ventana()
    self.ventana.title("Agregar Curso")
    super().centrar(self.ventana, 670, 465)
    self.ventana.geometry("670x465")
    self.__Ventana_frame()

  def __ir_pantalla_gestion_curso(self):
    self.ventana.destroy()
    Gestion_cursos()

  def __btn_Agregar_curso(self):
    curso = Curso(self.__tb_Codigo.get(), self.__tb_Nombre.get(), self.__tb_Prerequisito.get(), self.__tb_Obligatorio.get(),
    self.__tb_Semestre.get(), self.__tb_Creditos.get(), self.__tb_Estado.get())

    if not self.__tb_Codigo.get():
      tkinter.messagebox.showinfo("Error", "Por favor ingrese datos.")
    elif int(self.__tb_Semestre.get()) > 10:
      tkinter.messagebox.showinfo("Error", "Por favor ingrese un semestre válido.")
    else:
      DB.Crear_curso(curso, self.__tb_Codigo.get())
      tkinter.messagebox.showinfo("Confirmación", "¡Curso agregado exitosamente!")

  def __Ventana_frame(self):
    self.frame = Frame()
    self.frame.pack()
    self.frame.config(bg = "#F9E1BE", width = "650", height = "435", relief = "ridge", bd = 12)

    # LABELS-----
    self.__lbl_Codigo = Label(self.frame, text = "Código:", bg = "#F9E1BE", font = ("Arial", 12)).place(x = 45, y = 40)

    self.__lbl_Nombre = Label(self.frame, text = "Nombre:", bg = "#F9E1BE", font = ("Arial", 12)).place(x = 45, y = 90)

    self.__lbl_Prerequisito = Label(self.frame, text = "Pre-requisito:", bg = "#F9E1BE", font = ("Arial", 12)).place(x = 45, y = 140)

    self.__lbl_Semestre = Label(self.frame, text = "Semestre:", bg = "#F9E1BE", font = ("Arial", 12)).place(x = 45, y = 190)

    self.__lbl_Obligatorio = Label(self.frame, text = "Obligatorio:", bg = "#F9E1BE", font = ("Arial", 12)).place(x = 45, y = 240)

    self.__lbl_Creditos = Label(self.frame, text = "Créditos:", bg = "#F9E1BE", font = ("Arial", 12)).place(x = 45, y = 290)

    self.__lbl_Estado = Label(self.frame, text = "Estado:", bg = "#F9E1BE", font = ("Arial", 12)).place(x = 45, y = 340)

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
  
# ---------------------------------------------------EDITAR-CURSO-------------------------------------------------------------------------
class Editar_curso(Menu):
  def __init__(self):
    super().General_ventana()
    self.ventana.title("Editar Curso")
    super().centrar(self.ventana, 670, 465)
    self.ventana.geometry("670x465")
    self.__Ventana_frame()

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
      tkinter.messagebox.showinfo("Error", "El curso con código: " + self.__tb_Codigo.get() + ", no existe." )
    
  def __Editar_curso(self):
    if int(self.__tb_Semestre.get()) > 10:
      tkinter.messagebox.showinfo("Error", "Por favor ingrese un semestre válido.")
    else:
      DB.Actualizar_curso(self.__tb_Codigo.get(), self.__tb_Nombre.get(), self.__tb_Prerequisito.get(), self.__tb_Obligatorio.get(), self.__tb_Semestre.get(), self.__tb_Creditos.get(), self.__tb_Estado.get())
      tkinter.messagebox.showinfo("Confirmación", "¡Curso Editado exitosamente!")

  def __Ventana_frame(self):
    self.frame = Frame()
    self.frame.pack()
    self.frame.config(bg = "#F9E1BE", width = "650", height = "435", relief = "ridge", bd = 12)

    # LABELS-----
    self.__lbl_Codigo = Label(self.frame, text = "Código:", bg = "#F9E1BE", font = ("Arial", 12)).place(x = 45, y = 40)

    self.__lbl_Nombre = Label(self.frame, text = "Nombre:", bg = "#F9E1BE", font = ("Arial", 12)).place(x = 45, y = 90)
    
    self.__lbl_Prerequisito = Label(self.frame, text = "Pre-requisito:", bg = "#F9E1BE", font = ("Arial", 12)).place(x = 45, y = 140)

    self.__lbl_Semestre = Label(self.frame, text = "Semestre:", bg = "#F9E1BE", font = ("Arial", 12)).place(x = 45, y = 190)

    self.__lbl_Obligatorio = Label(self.frame, text = "Obligatorio:", bg = "#F9E1BE", font = ("Arial", 12)).place(x = 45, y = 240)

    self.__lbl_Creditos = Label(self.frame, text = "Créditos:", bg = "#F9E1BE", font = ("Arial", 12)).place(x = 45, y = 290)

    self.__lbl_Estado = Label(self.frame, text = "Estado:", bg = "#F9E1BE", font = ("Arial", 12)).place(x = 45, y = 340)

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

# ------------------------------------------------ELIMINAR-CURSO-------------------------------------------------------------------------
class Eliminar_curso(Menu):
  def __init__(self):
    super().General_ventana()
    self.ventana.title("Eliminar Curso")
    super().centrar(self.ventana, 515, 235)
    self.ventana.geometry("515x235")
    self.__Ventana_frame()

  def __ir_pantalla_gestion_curso(self):
    self.ventana.destroy()
    Gestion_cursos()

  def __Eliminar_curso(self):
    if DB.Eliminar_curso(self.__tb_Codigo_curso.get()) is not None:
      tkinter.messagebox.showinfo("Confirmación", "¡Curso Eliminado exitosamente!")
    else:
      tkinter.messagebox.showinfo("Error", "El curso con código: " + self.__tb_Codigo_curso.get() + ", no existe.")

  def __Ventana_frame(self):
    self.frame = Frame()
    self.frame.pack()
    self.frame.config(bg = "#F9E1BE", width = "495", height = "215", relief = "ridge", bd = 12)

    # LABEL-----
    self.__lbl_Codigo_curso = Label(self.frame, text = "Código de curso:", bg = "#F9E1BE", font = ("Comic Sans MS", 13)).place(x = 63, y = 38)

    # TEXFIELD-----
    self.__tb_Codigo_curso = Entry(self.frame, font = "Arial", width = 16, justify = "center")
    self.__tb_Codigo_curso.place(x = 218, y = 41)

    # BUTTON------
    self.__btn_Eliminar = Button(self.frame, text = "Eliminar", command = self.__Eliminar_curso, width = 13, height = 2, font = ("Arial", 9), bg = "#E7C09C")
    self.__btn_Eliminar.place(x = 98, y = 100)

    self.__btn_Regresar = Button(self.frame, text = "Regresar", command = self.__ir_pantalla_gestion_curso, width = 13, height = 2, font = ("Arial", 9), bg = "#E7C09C")
    self.__btn_Regresar.place(x = 248, y = 100)
    self.frame.mainloop()

# ----------------------------------------------CONTEO-DE-CREDITOS-------------------------------------------------------------------------
class Conteo_creditos(Menu):
  def __init__(self):
    super().General_ventana()
    self.ventana.title("Conteo Créditos")
    super().centrar(self.ventana, 590, 480)
    self.ventana.geometry("590x480")
    self.Ventana_frame()

  def __ir_pantalla_Menu(self):
    self.ventana.destroy()
    Menu()

  def __Creditos_semestreN(self):
    if not self.__tb_Creditos_obligatorios.get():
      tkinter.messagebox.showinfo("Error", "Por favor ingrese datos.")
    elif int(self.__tb_Creditos_obligatorios.get()) > 10:
      tkinter.messagebox.showinfo("Error", "Por favor ingrese un semestre válido.")
    else:
      Cant_creditos_SemestreN = DB.Devolver_creditos_semestreN(self.__tb_Creditos_obligatorios.get())
      self.__lbl_Creditos_obligatorios_text2.configure(text = Cant_creditos_SemestreN)

  def __Creditos_de_Semestre(self):
    if not self.__tb_Creditos_semestre.get():
      tkinter.messagebox.showinfo("Error", "Por favor ingrese datos.")
    elif int(self.__tb_Creditos_semestre.get()) > 10:
      tkinter.messagebox.showinfo("Error", "Por favor ingrese un semestre válido.")
    else:
      Cant_creditos_semestre = DB.Devolver_creditos_semestre_aprobados(self.__tb_Creditos_semestre.get())
      self.__lbl_Creditos_semestre_text1_2.configure(text = Cant_creditos_semestre)

      Cant_creditos_semestre = DB.Devolver_creditos_semestre_cursando(self.__tb_Creditos_semestre.get())
      self.__lbl_Creditos_semestre_text2_2.configure(text = Cant_creditos_semestre)

      Cant_creditos_semestre = DB.Devolver_creditos_semestre_pendientes(self.__tb_Creditos_semestre.get())
      self.__lbl_Creditos_semestre_text3_2.configure(text = Cant_creditos_semestre)

      self.__lbl_Creditos_semestre_text1.configure(text = "Aprobados: ")
      self.__lbl_Creditos_semestre_text2.configure(text = "Cursando: ")
      self.__lbl_Creditos_semestre_text3.configure(text = "Pendientes: ")

  def Ventana_frame(self):
    self.frame = Frame()
    self.frame.pack()
    self.frame.config(bg = "#F9E1BE", width = "570", height = "450", relief = "ridge", bd = 12)    

    # LABEL-----
    self.__lbl_Creditos_aprobados = Label(self.frame, text = "Créditos aprobados:", bg = "#F9E1BE", font = ("Comic Sans MS", 13)).place(x = 160, y = 25)
    self.__lbl_Creditos_cursando_text = Label(self.frame, text = DB.Devolver_creditos_aprobados(), bg = "#F9E1BE", font = ("Comic Sans MS", 13)).place(x = 333, y = 25)

    self.__lbl_Creditos_cursando = Label(self.frame, text = "Créditos cursando:", bg = "#F9E1BE", font = ("Comic Sans MS", 13)).place(x = 160, y = 75)
    self.__lbl_Creditos_cursando_text = Label(self.frame, text = DB.Devolver_creditos_cursando(), bg = "#F9E1BE", font = ("Comic Sans MS", 13)).place(x = 333, y = 77)

    self.__lbl_Creditos_pendientes = Label(self.frame, text = "Créditos pendientes:", bg = "#F9E1BE", font = ("Comic Sans MS", 13)).place(x = 160, y = 125)
    self.__lbl_Creditos_pendientes_text = Label(self.frame, text = DB.Devolver_creditos_pendiente(), bg = "#F9E1BE", font = ("Comic Sans MS", 13)).place(x = 333, y = 125)
  #-------------------------------------------------------------------------------------------------------
    self.__lbl_Creditos_obligatorios = Label(self.frame, text = "Créditos obligatorios hasta semestre:", bg = "#F9E1BE", font = ("Comic Sans MS", 13)).place(x = 90, y = 195)
    self.__lbl_Creditos_obligatorios_text1 = Label(self.frame, text = "Creditos: ", bg = "#F9E1BE", font = ("Comic Sans MS", 12)).place(x = 160, y = 233)
    self.__lbl_Creditos_obligatorios_text2 = Label(self.frame, bg = "#F9E1BE", font = ("Comic Sans MS", 12))
    self.__lbl_Creditos_obligatorios_text2.place(x = 230, y = 233)

    self.__lbl_Creditos_semestre = Label(self.frame, text = "Créditos del semestre:", bg = "#F9E1BE", font = ("Comic Sans MS", 13))
    self.__lbl_Creditos_semestre.place(x = 88, y = 310)

    self.__lbl_Creditos_semestre_text1 = Label(self.frame, bg = "#F9E1BE", font = ("Comic Sans MS", 12))#APROBADOS
    self.__lbl_Creditos_semestre_text1.place(x = 330, y = 310)
    self.__lbl_Creditos_semestre_text1_2 = Label(self.frame, bg = "#F9E1BE", font = ("Comic Sans MS", 12))
    self.__lbl_Creditos_semestre_text1_2.place(x = 420, y = 310)

    self.__lbl_Creditos_semestre_text2 = Label(self.frame, bg = "#F9E1BE", font = ("Comic Sans MS", 12))#CURSANDO
    self.__lbl_Creditos_semestre_text2.place(x = 330, y = 341)
    self.__lbl_Creditos_semestre_text2_2 = Label(self.frame, bg = "#F9E1BE", font = ("Comic Sans MS", 12))
    self.__lbl_Creditos_semestre_text2_2.place(x = 420, y = 341)

    self.__lbl_Creditos_semestre_text3 = Label(self.frame, bg = "#F9E1BE", font = ("Comic Sans MS", 12))#PENDIENTES
    self.__lbl_Creditos_semestre_text3.place(x = 329, y = 372)
    self.__lbl_Creditos_semestre_text3_2 = Label(self.frame, bg = "#F9E1BE", font = ("Comic Sans MS", 12))
    self.__lbl_Creditos_semestre_text3_2.place(x = 420, y = 372)

    # TEXFIELD-----
    self.__tb_Creditos_obligatorios = Entry(self.frame, font = "Arial", width = 3, justify = "center")
    self.__tb_Creditos_obligatorios.place(x = 400, y = 197)

    self.__tb_Creditos_semestre = Entry(self.frame, font = "Arial", width = 3, justify = "center")
    self.__tb_Creditos_semestre.place(x = 280, y = 312)

    # BUTTON------
    self.__btn_Contar_creditos_obligatorios = Button(self.frame, text = "Contar", command = self.__Creditos_semestreN, width = 10, height = 1, font = ("Arial", 9), bg = "#E7C09C").place(x = 265, y = 236)
    
    self.__btn_Contar_Creditos_semestre = Button(self.frame, text = "Contar", command = self.__Creditos_de_Semestre, width = 10, height = 1, font = ("Arial", 9), bg = "#E7C09C").place(x = 190, y = 351)

    self.__btn_Regresar = Button(self.frame, text = "Regresar", command = self.__ir_pantalla_Menu, width = 9, height = 1, font = ("Arial", 9), bg = "#E7C09C").place(x = 10, y = 385)
    self.frame.mainloop()
Menu()