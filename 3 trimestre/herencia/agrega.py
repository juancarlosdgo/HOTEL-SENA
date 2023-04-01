class Aprendiz: #se define la clase con nombre
    def __init__(self,nombre): #se define la funcion del constructor, co el respectivo parametro
        self.__nombre=nombre # se define una varaible de instancia que contenga el oarametro de la funcion
        self.__cursos=[] # se define otra variable de instancia que contenga una lista
    def agregarCurso(self,nombreCurso):# se define la funcion de gregar con la plabra reservada self y el parametro
        self.__cursos.append(nombreCurso) # se añade a la lista el parametro
    def verCursos(self): # se define otra funcion para ver con la palabra reservada self.
        return self.__cursos # returna el contenido de la varaible de instancia (la lista)

class Curso: # se define otra clase
    def __init__(self,nombreCurso): # se define la funcion del constructor, con el respectivo parametro
        self.__nombreCurso=nombreCurso #se define una variable de instancia que contenga el parametro de la funcion

    def getNombreCurso(self): # se define la funcion de ver con la palabra reservada self.
        return self.__nombreCurso # retorna el contenido de la varible de instancia que contenga el parametro de la funcion
    
ob=Aprendiz('Miguel') #se instancia la clase aprendiz con objeto ob y el parametro
c1=Curso('Python Basico') # se instancia la clase curso con el objeto c1 y el parametro
c2=Curso('Python Intermedio') # se instancia la clase curso con el objeto c2 y el parametro
c3=Curso('Java Basico') # se instancia la clase curso con el objeto c3 y el parametro

ob.agregarCurso(c1) # se le agrega al objeto ob, el objeto c1 que a su vez el objeto ob instancia la clase aprendizque asu vez contiene una lista en donde se agregaran los parametros establecidos en los objetos
ob.agregarCurso(c2) # se le agrega al objeto ob, el objeto c2 que a su vez el objeto ob instancia la clase aprendizque asu vez contiene una lista en donde se agregaran los parametros establecidos en los objetos
ob.agregarCurso(c3) # se le agrega al objeto ob, el objeto c3 que a su vez el objeto ob instancia la clase aprendizque asu vez contiene una lista en donde se agregaran los parametros establecidos en los objetos

for curso in ob.verCursos():# define un ciclo con el metodo vercurso perteneciente al objeto ob que a suz instacia la clase aprendiz
    print(curso.getNombreCurso()) #imprime el metodo ver de la clase

del ob #elimina el objeto ob que asu vez contiene la clase a prendiz
#print(ob)
print('.....',c1.getNombreCurso()) # imprime el objeto c1 con el metodo ver de la clase curso

