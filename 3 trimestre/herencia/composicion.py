class aprendiz:
    def __init__(self,nombre):
        self.nombre = nombre
        self.__cursos=[]

    def agregarcurso(self,nombrecurso):
        self.__cursos.append(nombrecurso)

    def vercurso(self):
        return self.__cursos
    

class curso:
    def __init__(self,nombrecurso):
        self.__nombrecurso=nombrecurso

    def vercurso(self):
        return self.__nombrecurso

ob = aprendiz("miguel")
c1 = curso("python basico")
c2 = curso("python intermedio")
c3 = curso("java basico")

ob.agregarcurso(c1)
ob.agregarcurso(c2)
ob.agregarcurso(c3)

for curso in ob.vercurso():
    print(curso.getnombrecurso())