from tkinter import *
from tkinter import ttk
from curso_model import Curso
from database import DB

# -------------------------------------------------------------MENÚ----------------------------------------------------------------------
class Menu():
  def __init__(self):
    self.ventana = Tk()
    self.ventana.title("Menú Principal")
    self.ventana.iconbitmap("Extras/logo.ico")
    self.ventana.resizable(0,0)
    self.ventana.config(bg = "#BB0D6A", relief = "flat", bd = 16)
    self.centrar(self.ventana, 600, 350)
    self.ventana.geometry("600x350")
    self.ventana_frame()

  def centrar(self, ventana, ancho, alto):
    altura_pantalla = ventana.winfo_screenheight()
    ancho_pantalla = ventana.winfo_screenwidth()
    x = (ancho_pantalla//2) - (ancho//2)
    y = (altura_pantalla//2) - (alto//2)
    ventana.geometry(f"+{x}+{y}")
  
  # Cambio de pantallas---------------
  def ir_pantalla_c(self):
    self.ventana.destroy()
    CargarArchivo()

  def ir_pantalla_g(self):
    self.ventana.destroy()
    Gestion_cursos()
  # ----------------------------------
  def ventana_frame(self):
    self.frame = Frame()
    self.frame.pack()
    self.frame.config(bg = "#F9E1BE", width = "580", height = "330", relief = "ridge", bd = 12)

    # Labels
    self.lbl_Nombre_curso = Label(self.frame, text = "Lenguajes Formales y de Programación", bg = "#F9E1BE", font = ("Comic Sans MS", 17))
    self.lbl_Nombre_curso.place(x = 72, y = 20)

    self.lbl_Nombre_estudiante = Label(self.frame, text = "Harry Aaron Gómez Sanic", bg = "#F9E1BE", bd = 0, font = ("Arial", 12))
    self.lbl_Nombre_estudiante.place(x = 80, y = 100)

    self.lbl_Carnet_estudiante = Label(self.frame, text = "carnet: 202103718", bg = "#F9E1BE", bd = 0, font = ("Arial", 12))
    self.lbl_Carnet_estudiante.place(x = 80, y = 140)

    #BOTONES

    self.btn_CargarArchivo = Button(self.frame, text = "Cargar Archivos",command = self.ir_pantalla_c, width = 19, height = 2, font = ("Arial", 9), bg = "#D5A273")
    self.btn_CargarArchivo.place(x = 335, y = 80)

    self.btn_GestionarCursos = Button(self.frame, text = "Gestionar Archivos", command = self.ir_pantalla_g, width = 19, height = 2, font = ("Arial", 9), bg = "#D5A273")
    self.btn_GestionarCursos.place(x = 335, y = 155)

    self.btn_ConteoCreditos = Button(self.frame, text = "Conteo de Créditos", width = 19, height = 2, font = ("Arial", 9), bg = "#D5A273")
    self.btn_ConteoCreditos.place(x = 335, y = 230)

    self.btn_Salir = Button(self.frame, text = "Salir", width = 11, height = 2, font = ("Arial", 10), bg = "#E7C09C")
    self.btn_Salir.place(x = 115, y = 215)

    self.frame.mainloop()  



# ----------------------------------------------------------CARGAR-ARCHIVOS-------------------------------------------------------------------------
class CargarArchivo():
  def __init__(self):
    self.ventana = Tk()
    self.ventana.title("Cargar Archivos")
    self.ventana.iconbitmap("Extras/logo.ico")
    self.ventana.resizable(0,0)
    self.ventana.config(bg = "#BB0D6A", relief = "flat", bd = 16)
    self.centrar(self.ventana, 600, 300)
    self.ventana.geometry("600x300")
    self.ventana_frame()

  def centrar(self, ventana, ancho, alto):
    altura_pantalla = ventana.winfo_screenheight()
    ancho_pantalla = ventana.winfo_screenwidth()
    x = (ancho_pantalla//2) - (ancho//2)
    y = (altura_pantalla//2) - (alto//2)
    ventana.geometry(f"+{x}+{y}")

  def ir_pantalla_m(self):
    self.ventana.destroy()
    Menu()

  def ventana_frame(self):
    self.frame = Frame()
    self.frame.pack()
    self.frame.config(bg = "#F9E1BE", width = "580", height = "280", relief = "ridge", bd = 12)

    # LABEL-----
    self.lbl_Ruta = Label(self.frame, text = "Ruta", bg = "#F9E1BE", font = ("Comic Sans MS", 13))
    self.lbl_Ruta.place(x = 85, y = 75)

    # TEXFIELD-----
    self.tb_Ruta = Entry(self.frame, font = "Arial", width = 29, justify = "center")
    self.tb_Ruta.place(x = 135, y = 78)

    # BUTTON------
    self.btn_Seleccionar = Button(self.frame, text = "Seleccionar", width = 13, height = 2, font = ("Arial", 9), bg = "#E7C09C")
    self.btn_Seleccionar.place(x = 145, y = 147)

    self.btn_Regresar = Button(self.frame, text = "Regresar", command = self.ir_pantalla_m, width = 13, height = 2, font = ("Arial", 9), bg = "#E7C09C")
    self.btn_Regresar.place(x = 310, y = 147)

    self.frame.mainloop()
  
  almacen_cursos = [] #[['017', 'Social Humanística 1', '7', '8', '1', '4', '0\n'], ...,  [...]]

  with open("entrada.LFP", "r") as archivo:
    lista_cursos = archivo.readlines()

  # Almacenar cada linea en otra lista individual
  for linea_curso in lista_cursos:
    #print(linea.rstrip())
    almacen_cursos.append(linea_curso.split(","))

    #print(almacen_cursos)
    #print(".......................")
    #print(almacen_cursos[0][0])#codigo
    #print(almacen_cursos[0][1])#nombre
  print("---------------------CAMBIO-----------------------------")
  for curso in almacen_cursos:
    indice_curso = almacen_cursos.index(curso)
        
    codigo = almacen_cursos[indice_curso][0]
    nombre = almacen_cursos[indice_curso][1]
    prerequisito = almacen_cursos[indice_curso][2]
    obligatorio = almacen_cursos[indice_curso][3]
    semestre = almacen_cursos[indice_curso][4]
    creditos = almacen_cursos[indice_curso][5]
    estado = almacen_cursos[indice_curso][6]

    curso = Curso(codigo, nombre, prerequisito, obligatorio, semestre, creditos, estado)
    
    DB.Crear_curso(curso)

# ---------------------------------------------------------GESTIONAR-ARCHIVOS-------------------------------------------------------------------------
class Gestion_cursos():
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

  def ir_pantalla_m(self):
    self.ventana.destroy()
    Menu()

  def ir_pantalla_l(self):
    self.ventana.destroy()
    listar_cursos()

  def ir_pantalla_a(self):
    self.ventana.destroy()
    Agregar_curso()

  def ir_pantalla_e(self):
    self.ventana.destroy()
    Editar_curso()
    

  def ventana_frame(self):
    self.frame = Frame()
    self.frame.pack()
    self.frame.config(bg = "#F9E1BE", width = "330", height = "300", relief = "ridge", bd = 12)

    # BUTTON------
    self.btn_Lista_cursos = Button(self.frame, text = "Listar Cursos",width = 14, command = self.ir_pantalla_l,  height = 1, font = ("Arial", 9), bg = "#E7C09C")
    self.btn_Lista_cursos.place(x = 90, y = 24)

    self.btn_Agregar_curso = Button(self.frame, text = "Agregar Curso", width = 14, command = self.ir_pantalla_a, height = 1, font = ("Arial", 9), bg = "#E7C09C")
    self.btn_Agregar_curso.place(x = 90, y = 69)

    self.btn_Editar_curso = Button(self.frame, text = "Editar Curso", width = 14, command = self.ir_pantalla_e, height = 1, font = ("Arial", 9), bg = "#E7C09C")
    self.btn_Editar_curso.place(x = 90, y = 117)

    self.btn_Eliminar_curso = Button(self.frame, text = "Eliminar Curso", width = 14, height = 1, font = ("Arial", 9), bg = "#E7C09C")
    self.btn_Eliminar_curso.place(x = 90, y = 165)  

    self.btn_Regresar = Button(self.frame, text = "Regresar", command = self.ir_pantalla_m, width = 10, height = 1, font = ("Arial", 9), bg = "#E7C09C")
    self.btn_Regresar.place(x = 103, y = 214)      

    self.frame.mainloop() 

# ----------------------------------------------------------LISTAR-CURSOS-------------------------------------------------------------------------
class listar_cursos():
  def __init__(self):
    self.ventana = Tk()
    self.ventana.title("Listar Cursos")
    self.ventana.iconbitmap("Extras/logo.ico")
    self.ventana.resizable(0,0)
    self.ventana.config(bg = "#BB0D6A", relief = "flat", bd = 16)
    self.centrar(self.ventana, 800, 460)
    self.ventana.geometry("800x460")
    self.ventana_frame()

  def centrar(self, ventana, ancho, alto):
    altura_pantalla = ventana.winfo_screenheight()
    ancho_pantalla = ventana.winfo_screenwidth()
    x = (ancho_pantalla//2) - (ancho//2)
    y = (altura_pantalla//2) - (alto//2)
    ventana.geometry(f"+{x}+{y}")

  def ir_pantalla_g(self):
    self.ventana.destroy()
    Gestion_cursos()

  def ventana_frame(self):
    self.frame = Frame()
    self.frame.pack()
    self.frame.config(bg = "#F9E1BE", width = "780", height = "430", relief = "ridge", bd = 12)

    # TABLA-----
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
    
    cursos = DB.Curso_prueba()
    print("hola")
    print(cursos[1].getNombre())

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

    # BUTTON------
    self.btn_Regresar = Button(self.frame, text = "Regresar", command = self.ir_pantalla_g, width = 14, height = 1, font = ("Arial", 9), bg = "#E7C09C")
    self.btn_Regresar.place(x = 580, y = 364)
    
    self.frame.mainloop() 



# ---------------------------------------------------------AGREGAR-CURSO-------------------------------------------------------------------------
class Agregar_curso():
  def __init__(self):
    self.ventana = Tk()
    self.ventana.title("Agregar Curso")
    self.ventana.iconbitmap("Extras/logo.ico")
    self.ventana.resizable(0,0)
    self.ventana.config(bg = "#BB0D6A", relief = "flat", bd = 16)
    self.centrar(self.ventana, 670, 465)
    self.ventana.geometry("670x465")
    self.ventana_frame()

  def centrar(self, ventana, ancho, alto):
    altura_pantalla = ventana.winfo_screenheight()
    ancho_pantalla = ventana.winfo_screenwidth()
    x = (ancho_pantalla//2) - (ancho//2)
    y = (altura_pantalla//2) - (alto//2)
    ventana.geometry(f"+{x}+{y}")

  def ir_pantalla_g(self):
    self.ventana.destroy()
    Gestion_cursos()

  def ventana_frame(self):
    self.frame = Frame()
    self.frame.pack()
    self.frame.config(bg = "#F9E1BE", width = "650", height = "435", relief = "ridge", bd = 12)

    # LABELS-----
    self.lbl_Codigo = Label(self.frame, text = "Código:", bg = "#F9E1BE", font = ("Arial", 12))
    self.lbl_Codigo.place(x = 45, y = 40)

    self.lbl_Nombre = Label(self.frame, text = "Nombre:", bg = "#F9E1BE", font = ("Arial", 12))
    self.lbl_Nombre.place(x = 45, y = 90)
    
    self.lbl_Prerequisito = Label(self.frame, text = "Pre-requisito:", bg = "#F9E1BE", font = ("Arial", 12))
    self.lbl_Prerequisito.place(x = 45, y = 140)

    self.lbl_Semestre = Label(self.frame, text = "Semestre:", bg = "#F9E1BE", font = ("Arial", 12))
    self.lbl_Semestre.place(x = 45, y = 190)

    self.lbl_Obligatorio = Label(self.frame, text = "Obligatorio:", bg = "#F9E1BE", font = ("Arial", 12))
    self.lbl_Obligatorio.place(x = 45, y = 240)

    self.lbl_Creditos = Label(self.frame, text = "Créditos:", bg = "#F9E1BE", font = ("Arial", 12))
    self.lbl_Creditos.place(x = 45, y = 290)

    self.lbl_Estado = Label(self.frame, text = "Estado:", bg = "#F9E1BE", font = ("Arial", 12))
    self.lbl_Estado.place(x = 45, y = 340)

    # TEXFIELD-----
    self.tb_Codigo = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.tb_Codigo.place(x = 160, y = 42)

    self.tb_Nombre = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.tb_Nombre.place(x = 160, y = 92)

    self.tb_Prerequisito = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.tb_Prerequisito.place(x = 160, y = 142)

    self.tb_Semestre = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.tb_Semestre.place(x = 160, y = 192)

    self.tb_Obligatorio = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.tb_Obligatorio.place(x = 160, y = 242)

    self.tb_Creditos = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.tb_Creditos.place(x = 160, y = 292)

    self.tb_Estado = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.tb_Estado.place(x = 160, y = 342)

    # BUTTON-----
    self.btn_Agregar = Button(self.frame, text = "Agregar", width = 14, height = 3, font = ("Arial", 9), bg = "#E7C09C")
    self.btn_Agregar.place(x = 460, y = 130)

    self.btn_Regresar = Button(self.frame, text = "Regresar", command = self.ir_pantalla_g, width = 14, height = 3, font = ("Arial", 9), bg = "#E7C09C")
    self.btn_Regresar.place(x = 460, y = 225)

    self.frame.mainloop() 



# ---------------------------------------------------------EDITAR-CURSO-------------------------------------------------------------------------
class Editar_curso():
  def __init__(self):
    self.ventana = Tk()
    self.ventana.title("Editar Curso")
    self.ventana.iconbitmap("Extras/logo.ico")
    self.ventana.resizable(0,0)
    self.ventana.config(bg = "#BB0D6A", relief = "flat", bd = 16)
    self.centrar(self.ventana, 670, 465)
    self.ventana.geometry("670x465")
    self.ventana_frame()

  def centrar(self, ventana, ancho, alto):
    altura_pantalla = ventana.winfo_screenheight()
    ancho_pantalla = ventana.winfo_screenwidth()
    x = (ancho_pantalla//2) - (ancho//2)
    y = (altura_pantalla//2) - (alto//2)
    ventana.geometry(f"+{x}+{y}")

  def ir_pantalla_g(self):
    self.ventana.destroy()
    Gestion_cursos()

  def ventana_frame(self):
    self.frame = Frame()
    self.frame.pack()
    self.frame.config(bg = "#F9E1BE", width = "650", height = "435", relief = "ridge", bd = 12)

    # LABELS-----
    self.lbl_Codigo = Label(self.frame, text = "Código:", bg = "#F9E1BE", font = ("Arial", 12))
    self.lbl_Codigo.place(x = 45, y = 40)

    self.lbl_Nombre = Label(self.frame, text = "Nombre:", bg = "#F9E1BE", font = ("Arial", 12))
    self.lbl_Nombre.place(x = 45, y = 90)
    
    self.lbl_Prerequisito = Label(self.frame, text = "Pre-requisito:", bg = "#F9E1BE", font = ("Arial", 12))
    self.lbl_Prerequisito.place(x = 45, y = 140)

    self.lbl_Semestre = Label(self.frame, text = "Semestre:", bg = "#F9E1BE", font = ("Arial", 12))
    self.lbl_Semestre.place(x = 45, y = 190)

    self.lbl_Obligatorio = Label(self.frame, text = "Obligatorio:", bg = "#F9E1BE", font = ("Arial", 12))
    self.lbl_Obligatorio.place(x = 45, y = 240)

    self.lbl_Creditos = Label(self.frame, text = "Créditos:", bg = "#F9E1BE", font = ("Arial", 12))
    self.lbl_Creditos.place(x = 45, y = 290)

    self.lbl_Estado = Label(self.frame, text = "Estado:", bg = "#F9E1BE", font = ("Arial", 12))
    self.lbl_Estado.place(x = 45, y = 340)

    # TEXFIELD-----
    self.tb_Codigo = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.tb_Codigo.place(x = 160, y = 42)

    self.tb_Nombre = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.tb_Nombre.place(x = 160, y = 92)

    self.tb_Prerequisito = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.tb_Prerequisito.place(x = 160, y = 142)

    self.tb_Semestre = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.tb_Semestre.place(x = 160, y = 192)

    self.tb_Obligatorio = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.tb_Obligatorio.place(x = 160, y = 242)

    self.tb_Creditos = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.tb_Creditos.place(x = 160, y = 292)

    self.tb_Estado = Entry(self.frame, font = "Arial", width = 28, justify = "center")
    self.tb_Estado.place(x = 160, y = 342)

    # BUTTON-----
    self.btn_Editar = Button(self.frame, text = "Editar", width = 14, height = 3, font = ("Arial", 9), bg = "#E7C09C")
    self.btn_Editar.place(x = 460, y = 130)

    self.btn_Regresar = Button(self.frame, text = "Regresar", command = self.ir_pantalla_g, width = 14, height = 3, font = ("Arial", 9), bg = "#E7C09C")
    self.btn_Regresar.place(x = 460, y = 225)

    self.frame.mainloop() 

# ---------------------------------------------------------ELIMINAR-CURSO-------------------------------------------------------------------------


Menu()