class Curso():
    def __init__(self, codigo, nombre, prerequisito, obligatorio, semestre, creditos, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.prerequisito = prerequisito
        self.obligatorio = obligatorio
        self.semestre = semestre
        self.creditos = creditos
        self.estado = estado

    # SETTERS----------
    def setCodigo(self, codigo):
        self.codigo = codigo

    def setNombre(self, nombre):
        self.nombre = nombre

    def setPrerequisito(self, prerequisito):
        self.prerequisito = prerequisito

    def setObligatorio(self, obligatorio):
        self.obligatorio = obligatorio

    def setSemestre(self, semestre):
        self.semestre = semestre
    
    def setCreditos(self, creditos):
        self.creditos = creditos

    def setEstado(self, estado):
        self.estado = estado


    # GETTERS----------
    def getCodigo(self):
        return self.codigo

    def getNombre(self):
        return self.nombre

    def getPrerequisito(self):
        return self.prerequisito

    def getObligatorio(self):
        return self.obligatorio

    def getSemestre(self):
        return self.semestre
    
    def getCreditos(self):
        return self.creditos

    def getEstado(self):
        return self.estado