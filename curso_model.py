class Curso():
    def __init__(self, codigo, nombre, prerequisito, obligatorio, semestre, creditos, estado):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__prerequisito = prerequisito
        self.__obligatorio = obligatorio
        self.__semestre = semestre
        self.__creditos = creditos
        self.__estado = estado

    # SETTERS----------
    def setCodigo(self, codigo):
        self.__codigo = codigo

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setPrerequisito(self, prerequisito):
        self.__prerequisito = prerequisito

    def setObligatorio(self, obligatorio):
        self.__obligatorio = obligatorio

    def setSemestre(self, semestre):
        self.__semestre = semestre
    
    def setCreditos(self, creditos):
        self.__creditos = creditos

    def setEstado(self, estado):
        self.__estado = estado


    # GETTERS----------
    def getCodigo(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre

    def getPrerequisito(self):
        return self.__prerequisito

    def getObligatorio(self):
        return self.__obligatorio

    def getSemestre(self):
        return self.__semestre
    
    def getCreditos(self):
        return self.__creditos

    def getEstado(self):
        return self.__estado