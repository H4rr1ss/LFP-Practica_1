class Database():
    def __init__(self):
        self._cursos = []
        self._codigos = []
        self._creditos = []

    def Crear_curso(self, curso):#curso es el objeto entonces tengo acceso a los atributos
        self._cursos.append(curso)
        self._codigos.append(curso.getCodigo())
        print(self._codigos)
        self._creditos.append(curso.getCreditos())
        
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
                print("-------CAMBIO-------")
                print(self._codigos)
                return True

        return None

DB = Database()