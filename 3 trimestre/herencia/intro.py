class vehiculos:
    def __init__(self, tipo):
        self.__tipo=tipo
        
    def descripcion(self):
        print("soy generico no tengo descripcion")

    def gettipo(self):
        return self.__tipo
    
    def __str__(self) -> str:
        return "soy objeto de la clase vehiculo"
    


class herramientas:
    def __init__(self, proposito):
        self.__proposito=proposito
    
    def getproposito(self):
        return self.__proposito
    
    def __str__(self) -> str:
        return "soy objeto de la clase herrmientas"


#v = vehiculos("cualquier vehiculo")

class terrestres(vehiculos):
    def __init__(self, tipo):
        vehiculos.__init__(self.__tipo)
    
    def datos():
        print("tipo: ", super().gettipo())

    def __str__(self) -> str:
        return "soy objeto de la clase terrestre"
    
t = terrestres()
print(t.gettipo())


lista = [1,2,3]
print(lista)