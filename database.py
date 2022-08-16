class Database():
    def __init__(self):
        self._cursos = []#Almacena los objetos 
        self._codigos = []
    # ---------------------------CREAR CURSO NUEVO---------------------------
    def __Crear(self, curso):
        self._cursos.append(curso)
        self._codigos.append(curso.getCodigo())

    def __Verificacion_curso_nuevo(self, curso_nuevo, codigo):
        for curso in self._cursos:
            if curso.getCodigo() == codigo:
                self._cursos.remove(curso)
                self._codigos.remove(curso.getCodigo())
                self.__Crear(curso_nuevo)
                return True

    def Crear_curso(self, curso, codigo):# Curso es el objeto entonces tengo acceso a los atributos
        if codigo in self._codigos:# Si ya existe el código ingresado
            self.__Verificacion_curso_nuevo(curso, codigo)
        else:# Si no existe el código ingresado, lo creará
            self.__Crear(curso)
    # -----------------------------------------------------------------------

    # -------------------------------LISTAR CURSO----------------------------
    def Recibir_curso(self):
        return self._cursos
    # -----------------------------------------------------------------------

    # -----------------------------EDITAR CURSO-----------------------------
    def Mostrar_curso(self, codigo):
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
    # -----------------------------------------------------------------------

    # -----------------------------ELIMINAR CURSO----------------------------
    def Eliminar_curso(self, codigo):
        for curso in self._cursos:
            if curso.getCodigo() == codigo:
                self._cursos.remove(curso)
                self._codigos.remove(codigo)
                return True
        return None
    # -----------------------------------------------------------------------

    # ---------------------------CONTEO DE CREDITOS--------------------------
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
            if (int(curso.getSemestre()) == int(semestre)) and (curso.getEstado() == "0"):
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
    # -----------------------------------------------------------------------
DB = Database()