class Persona (): #crear la clace con el nombre persona y los 2 puntos
    cont = 0
    def __init__(self,nombre,documento): #dentro de la clase se crea la primera funcion __init__. con parametro reservado self y se parado por comas el nombre de otros 2 parametrs(self,nombre,documento).
        self.__nombre=nombre # (variable de instacia) parametro reservado (self.) y el doble guin bajo es para poner el parametro privado.(indicamos parametro privado es igual a parametro(self.__nombre=nombre))
        self.__documento=documento # (variable de instacia) parametro reservado (self.) y el doble guin bajo es para poner el parametro privado.(indicamos parametro privado es igual a parametro(self.__documento=documento))
        #print('Constructor Activado')        

    def getNombre(self): #dentro de la clase persona definir otra funcion (dependiente de la funcion __init__, mediante parametro especial (self)),"asegurandonos de que refleje los dtos relacionados con la funcion __init__"
        try: #dentro de esta funcion se define el bloque try para excepciones seguido de 2 puntos
            return self.__nombre, self.__documento #try nos retornara mediante el parametro (self.)(que empieza a actuar como metodo), mostrando los datos relacionados en la funcion __init__
        except: #creamos un bloque de excepcion generico por si se presenta algun error.
            return "se ha presentado un error" # de existir el error lo va a exceptuar y retornara el mensaje de error.

    def setNombre(self,nombre,documento): #dentro de la clase persona definir una funcion que permita modificar los datos relacionados en la funcion __init__
        try: #dentro de la funcion (setnombre) diseñada para modificar los datos relacionados en la funcion __init__( abrimos la primera parte del bloque de codigo de excepcione mediante la palabra try), eguida de 2 punto.
            self.__nombre=nombre, self.__documento=documento # try nos retornara mediante el parametro (self.) los dato relacionado en la funcion __iniit__ definida entro d la clae persona
        except: #creamos un bloque de excepcion generico por si se presenta algun error
            return "hay un error" # de existir el error lo va a exceptuar y retornara el mensaje de error.

ob=Persona('Maria', 1012444700) #('Constructor Activado'),,(se crea el objeto ob que es == a la clase persona, que asu ves contiene 2 parametros)
print(ob.getNombre()) #imprimir objeto (ob), que a su vez contine la clase persona, que a su vez contiene las funciones __init__ como base principal de la clae persona y 2 funciones mas una para mostras y otra para modificr los datos de la clae 
ob.setNombre('Ana',32423423422) #cambiamos los datos relacionados en los parametros de la funcion __init__
print(ob.getNombre()) #imprimimos nuevamente el objeto (ob), pera ya se refleja que los datos fueron modificdos mediante la funcion setnombre, definida dentro de la clase persona
#print(type(ob))

class Aprendiz(Persona): # crear una nueva clase con nombre aprendiz la cual contiene como parametro, la clase personas
    def __init__(self,nombre,ficha,documento): # defiir la funcion epecial __init__, con el parametro especial (self.) y separada por coma los otros dos parametros previamente establecido en la clase persona pero esta vez lo volvemos a llamar y agregamos un nuevo parametro para esta clase aprendiz
        Persona.__init__(self,nombre,documento) # llamamos la funcion __init__ de la clae persona con los parametros previamnete esctablecidos
        self.__nombre=nombre # (variable de instacia) parametro reservado (self.) y el doble guin bajo es para poner el parametro privado.(indicamos parametro privado es igual a parametro(self.__nombre=nombre))
        self.__ficha=ficha # (variable de instacia) parametro reservado (self.) y el doble guin bajo es para poner el parametro privado.(indicamos parametro privado es igual a parametro(self.__ficha=ficha))
        self.__documento=documento # (variable de instacia)  parametro reservado (self.) y el doble guin bajo es para poner el parametro privado.(indicamos parametro privado es igual a parametro(self.__documento=documento))

    def getFicha(self): #dentro de la clase aprendiz definir otra funcion (dependiente de la funcion __init__, mediante parametro especial (self)),"asegurandonos de que refleje los datos relacionados con la funcion __init__"
        try: #dentro de la funcion (setficha) diseñada para mostrar los datos relacionados en la funcion __init__( abrimos la primera parte del bloque de codigo de excepcione mediante la palabra try), eguida de 2 puntos.
            return self.__ficha #try nos retornara mediante el parametro (self.)(que empieza a actuar como metodo), mostrando los datos relacionados en la funcion __init__
        except: #creamos un bloque de excepcion generico por si se presenta algun error
            return "ocurrio un error" #de existir el error lo va a exceptuar y retornara el mensaje de error.
    
    def getall(self): #dentro de la clase aprendiz definir una funcion que permita mostrar todos los datos relacionados en la clase persona y la clase aprendiz
        try: #dentro de la funcion (getall) diseñada para mostrar los datos relacionados en la clase persona y aprendiz abrimos la primera parte del bloque de codigo de excepcione mediante la palabra try), eguida de 2 punto.
            return self.__nombre, self.__ficha, self.__documento # try nos retornara mediante el parametro (self.) los dato relacionado en la funcion __iniit__ definida entro de la clae persona y aprendiz
        except: #creamos un bloque de excepcion generico por si se presenta algun error
            return " ocurrio un error" #de existir el error lo va a exceptuar y retornara el mensaje de error.

app=Aprendiz('Pedro',12345,1012444700) # instanciamos el ojeto app que posee la clase aprendiz con 3 parameros
#print(app.getFicha())
#print(app.getNombre())
print(app.getall()) # imprimir el metodo getall de la clase app

print(type(app)) # imprimir tipo de dato del ojeto app