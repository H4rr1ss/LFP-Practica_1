class CargarArchivo:
    def __init__(self, codigo, nombre, prerrequisito, obligatorio):
        self.codigo = codigo
        self.nombre = nombre
        self.prerrequisito = prerrequisito
        self.obligatorio = obligatorio

    # GETTERS
    def get_codigo(self):
        return self.codigo  

    def get_nombre(self):
        return self.nombre

    def get_prerrequisito(self):
        return self.prerrequisito

    def get_obligatorio(self):
        return self.obligatorio

