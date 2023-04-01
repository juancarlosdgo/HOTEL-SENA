import datetime
class pedido():
        def __init__(self, ID_user, titulo, codigo) -> None:
            self.ID_user=ID_user
            self.titulo=titulo
            self.codigo=codigo
        
        def reservar(self,fecha):
            fecha = datetime.date
            return fecha

        def entregar(self):
            fecha = datetime.date
            return fecha
        
        def getTitulo(self):
             return self.ID_user, self.titulo, self.codigo

class lector():
        def __init__(self, nombre, direccion, telefono) -> None:
            self.nombre=nombre
            self.direccion=direccion
            self.telefono=telefono
            self.lista= []
    
        def reservar(self,fecha,titulo,codigo):
            fechass = pedido(fecha, titulo, codigo)
            self.lista.append(fechass)
            

        def entregar(self):
            fecha = datetime.datetime
            return fecha
        
        def get_lector(self):
             return self.nombre, self.direccion, self.telefono
        pass

class estudiante(lector):

        def __init__(self, cod_estud) -> None:
            super().__init__()
            self.cod_estud=cod_estud


        def reservar(self):
            lib = libro
            return lib

        def entregar(self):
            lib = libro
            return lib
        
        def get_estudiante(self):
            return self.cod_estud
        pass

class docente(lector):
        def __init__(self, cod_docen) -> None:
            super().__init__()
            self.cod_docen=cod_docen

        def reservar(self):
            lib = libro
            return lib

        def entregar(self):
            lib = libro
            return lib
        
        def get_doente(self):
             self.cod_docen

        pass


class libro (pedido):
        def __init__(self,titulo,tipo,autor,editorial) -> None:
            super().__init__()
            self.tipo=tipo
            self.autor=autor
            self.editorial=editorial

        def reservar(self):
            fecha = datetime
            return fecha

        def entregar(self):
            fecha = datetime
            return fecha
        
        def get_lib(self):
            return self.titulo, self.tipo, self.autor, self.editorial
        pass
   


class tipo_libro (libro):
        def __init__(self, fisico, digital) -> None:
            super().__init__()
            self.fisico=fisico
            self.digital=digital

        def reservar(self):
            fecha = datetime.date
            return fecha

        def entregar(self):
            fecha = datetime.date
            return fecha
        
        def get_tip_lib(self):
            return self.fisico , self.digital
        pass
          


class revista (pedido):
        def __init__(self, tipo,autor,edicion) -> None:
            super().__init__()
            self.tipo=tipo
            self.autor=autor
            self.edicion=edicion

        def reservar(self):
            fecha = datetime.date
            return fecha

        def entregar(self):
            fecha = datetime.date
            return fecha
        
        def get_revis(self):
            return self.tipo, self.autor, self.edicion
        pass



class tipo_revista(revista):        
        def __init__(self, fisico, digital) -> None:
            super().__init__()
            self.fisico=fisico
            self.digital=digital

        def reservar(self):
            fecha = datetime.date
            return fecha

        def entregar(self):
            fecha = datetime.date
            return fecha
            
        def get(self):
             return self.fisico, self.digital
        pass
             



aa = lector("year",34342,32423423.)

aa.reservar("dcsdcsc",23234234,"fvdfv")
ab = pedido
ba = estudiante.entregar("22-4-23")
bb = docente
ca = libro
cb = revista
da = tipo_libro
db = tipo_revista
#print('titulo de a=',aa.lista[0].getTitulo())


"""try:
except:
    print("Ocurrio algun error")"""

print("ingrese un numero para escoger del menu")

a = input("ingrese un numero para escoger del menu")
b = input("ingrese un numero para escoger del menu")
c = input("ingrese un numero para escoger del menu")
d = input("ingrese un numero para escoger del menu")
e = input("ingrese un numero para escoger del menu")
f = input("ingrese un numero para escoger del menu")
g = input("ingrese un numero para escoger del menu")
h = input("ingrese un numero para escoger del menu")


#print(aa.get_lector())



print("ingrese un numero para escoger del menu")
if a == 1:
     print(aa.get_lector)
elif b == 2:
     print(ab)
elif c == 3:
     print(ba)
elif d == 4:
     print(bb)
elif e == 5:
     print(ca)
elif f == 6:
     print(cb)
elif g == 7:
     print(da)
elif h == 8:
     print(db)