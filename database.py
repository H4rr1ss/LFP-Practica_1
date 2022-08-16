class Database():
    def __init__(self):
        self._cursos = []#Almacena los objetos "get set"
        self._codigos = []
        self._creditos = []
    # ---------------------------CREAR CURSO NUEVO---------------------------
    def __Crear(self, curso):
        self._cursos.append(curso)
        self._codigos.append(curso.getCodigo())
        self._creditos.append(curso.getCreditos())
        print(self._creditos)

    def __Verificacion_curso_nuevo(self, curso_nuevo, codigo):
        print(self._codigos)
        for curso in self._cursos:
            if curso.getCodigo() == codigo:
                print(self._codigos.count(str(codigo)))
                self._cursos.remove(curso)
                self._codigos.remove(curso.getCodigo())
                print("LISTA ACTUALIZADA:")
                self.Crear(curso_nuevo)
                print(self._codigos)
                return True

    def Crear_curso(self, curso, codigo):#curso es el objeto entonces tengo acceso a los atributos
        if codigo in self._codigos:#Si ya existe el código ingresado
            print("si se encuentra ya credado")
            self.__Verificacion_curso_nuevo(curso, codigo)
        else:# Si no existe el código ingresado, lo creara
            self.__Crear(curso)
    # -----------------------------------------------------------------------

    # ---------------------------CRÉDITOS GENERALES--------------------------
    def Devolver_creditos_aprobados(self):
        total_creditos = 0
        for curso in self._cursos:
            if curso.getEstado() == "0":
                total_creditos += int(curso.getCreditos())
        return total_creditos

    def Devolver_creditos_cursando(self):
        total_creditos = 0
        for curso in self._cursos:
            if curso.getEstado() == "1":
                total_creditos += int(curso.getCreditos())
        return total_creditos
    
    def Devolver_creditos_pendiente(self):
        total_creditos = 0
        for curso in self._cursos:
            if curso.getEstado() == "-1" and curso.getObligatorio() == "1":
                total_creditos += int(curso.getCreditos())
        return total_creditos
    # -----------------------------------------------------------------------

    def Devolver_creditos_semestreN(self, semestre):
        total_creditos = 0
        for curso in self._cursos:
            if curso.getObligatorio() == "1" and (int(curso.getSemestre()) <= int(semestre)):
                total_creditos += int(curso.getCreditos())
        return total_creditos

    def Devolver_creditos_semestre_aprobados(self, semestre):
        total_creditos = 0
        for curso in self._cursos:
            if int(curso.getSemestre()) == int(semestre) and curso.getEstado() == "0":
                total_creditos += int(curso.getCreditos())
        return total_creditos
    
    def Devolver_creditos_semestre_cursando(self, semestre):
        total_creditos = 0
        for curso in self._cursos:
            if int(curso.getSemestre()) == int(semestre) and curso.getEstado() == "1":
                total_creditos += int(curso.getCreditos())
        return total_creditos

    def Devolver_creditos_semestre_pendientes(self, semestre):
        total_creditos = 0
        for curso in self._cursos:
            if int(curso.getSemestre()) == int(semestre) and curso.getEstado() == "-1":
                total_creditos += int(curso.getCreditos())
        return total_creditos

    def Recibir_curso(self):
        return self._cursos

    def Mostrar_curso(self, codigo):
        print("----------------------------")
        for curso in self._cursos:
            if curso.getCodigo() == codigo:
                return curso
        return None
            
    def Actualizar_curso(self, codigo, nombre, prerequisito, obligatorio, semestre, creditos, estado):
        for curso in self._cursos:
            if curso.getCodigo() == codigo:
                curso.setNombre(nombre)
                curso.setPrerequisito(prerequisito)
                curso.setObligatorio(obligatorio)
                curso.setSemestre(semestre)
                curso.setCreditos(creditos)
                curso.setEstado(estado)
    
    def Eliminar_curso(self, codigo):
        for curso in self._cursos:
            if curso.getCodigo() == codigo:
                self._cursos.remove(curso)
                self._codigos.remove(codigo)
                return True
        return None

DB = Database()