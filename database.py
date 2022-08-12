class Database():
    def __init__(self):
        self._cursos = []
        self._codigos = []
        self._creditos = []

    def Crear_curso(self, curso):
        self._cursos.append(curso)
        
    def Curso_prueba(self):
        return self._cursos


DB = Database()