class producto:
    cont = 0
    
    def __init__(self,nombre, precio):
        self.__nombre = nombre
        self.__precio = precio
        producto.cont+=1

    def calcular(self):
        try:
            return self.__precio * 0.19
        except:
            return "error"
    
    def getnom(self):
        try:
            return self.__nombre, self.__precio
        except:
            return "ocurrio un error"
        
    def setnom_1(self, nombre):
        try:
            self.__nombre=nombre
        except:
            return "ocurrio un error"
        
    def setnom_2(self, precio):
        try:
            self.__precio=precio
        except:
            return "ocurrio un error"
        
        producto.j = precio
        
#############################################################################################


d = producto("harry",23345)
print(d.getnom())


a = producto("juan",10000)
print(a.getnom())
a.setnom_1("maicol")
a.setnom_2(20000)
print(a.getnom())
print("se instancio",a.cont, "veces")
i = a.j
b = a.calcular()
print("el IVA del producto es de: ", b, "y el total + IVA es de: ", b + i)

p= producto("cfce",4334453)