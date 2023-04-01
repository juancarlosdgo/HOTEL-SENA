class Personas:
    def __init__(self, nombre, docuemnto) -> None:
        self.__nombre=nombre
        self.__documento=docuemnto

    def getNombre(self):
        return self.__nombre
    def getDocuemnto(self):
        return self.__documento
    def setNombre(self, nombre):
        self.__nombre=nombre
    def setDocumento(self, documento):
        self.__documento=documento



