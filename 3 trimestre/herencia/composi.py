class Curso: # se define la clase con nombre
    def __init__(self,titulo): # definir la funcion del constructor con el respectivo parametro
        self.__titulo=titulo #defiir la variable de instancia que contenga el parametro d la funcion

    def getTitulo(self): #definir la funcion ver con la palabra reservada self.
        return self.__titulo #retorna el contenido de la avriable de instancia contenida en la funcion del constructor

class Aprendiz: #definir la clase con nombre
    def __init__(self,nombre): # definir la funcion del constructor con el respectivo parametro
        self.__nombre=nombre #defiir la variable de instancia que contenga el parametro d la funcion
        self.__cursos=[] # se define otra variable de instancia que contenga una lista

    def agregarCurso(self,nombreCursito): #definir la funcion agregar con la palabra reservada self y el parametro
        cursito=Curso(nombreCursito) #se instancia la clase curso con objeto cursito y el parametro
        self.__cursos.append(cursito) # se añade a la lista el parametro

    def getCursos(self): #definir la funcion ver con la palabra reservada self.
        return self.__cursos # # returna el contenido de la varaible de instancia (la lista)

    
ap=Aprendiz('Sofia') #se instancia la clase Aprendiz con el objeto ap y el parametro
ap.agregarCurso('Python Basico') # se le agrega al objeto ap, mediante el metodo agregar defiido en la clase aprendiz con el parametro
ap.agregarCurso('Python Intermedio') # se le agrega al objeto ap, mediante el metodo agregar defiido en la clase aprendiz con el parametro

for c in ap.getCursos(): #se define unciclo con el metodo ver definido en la clase aprendiz instanciado en el objeto ap
    print(c.getTitulo()) # imprime ver de la clase curso

del ap #se elimina el objeto ap que asu vez contenia la clase aprendiz
