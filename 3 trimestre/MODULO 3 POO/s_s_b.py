import datetime

class lector():

    cont = 0

    try:
        def __init__(self, nombre, direccion, telefono) -> None:
            self.nombre=nombre
            self.direccion=direccion
            self.telefono=telefono
            lector.cont += 1
            lista= []
    
        def reservar(self,fecha):
            fecha = pedido()
            return fecha
            lista.append()

        def entregar(self):
            fecha = datetime.datetime
            return fecha
    except:
        print("ocirrio algun problema")

class estudiante(lector):
    try:
        super().__init__()

        def __init__(self, cod_estud) -> None:
            self.cod_estud=cod_estud


        def reservar(self):
            lib = libro
            return lib

        def entregar(self):
            lib = libro
            return lib
    except:
        print("Ocurrio algun error")


class docente(lector):
    try:
        def __init__(self, nombre, direccion, telefono) -> None:
            super().__init__(nombre, direccion, telefono)

        def __init__(self, cod_docen) -> None:
            self.cod_docen=cod_docen

        def reservar(self):
            lib = libro
            return lib

        def entregar(self):
            lib = libro
            return lib
    except:
        print("Ocurrio algun error")
    

    
class pedido(lector):
    try:
        def __init__(self, nombre, direccion, telefono) -> None:
            super().__init__(nombre, direccion, telefono)

        def __init__(self, ID_user, titulo, codigo) -> None:
            self.ID_user=ID_user
            self.titulo=titulo
            self.codigo=codigo
        
        def reservar(self):
            fecha = datetime.datetime
            return fecha

        def entregar(self):
            fecha = datetime.datetime
            return fecha
            pass
    except:
        print("Ocurrio algun error")


class libro (pedido):
    try:
        def __init__(self, ID_user, titulo, codigo) -> None:
            super().__init__(ID_user, titulo, codigo)

        def __init__(self,titulo,tipo,autor,editorial) -> None:
            self.tipo=tipo
            self.autor=autor
            self.editorial=editorial

        def reservar(self):
            fecha = datetime.datetime
            return fecha

        def entregar(self):
            fecha = datetime.datetime
            return fecha
            pass
    except:
        print("Ocurrio algun error")    


class tipo_libro (libro):
    try:
        def __init__(self, titulo, tipo, autor, editorial) -> None:
            super().__init__(titulo, tipo, autor, editorial)
        def __init__(self, fisico, digital) -> None:
            self.fisico=fisico
            self.fisico=fisico

        def reservar(self):
            fecha = datetime.datetime
            return fecha

        def entregar(self):
            fecha = datetime.datetime
            return fecha
            pass
    except:
        print("Ocurrio algun error")       


class revista (pedido):
    try:
        def __init__(self, ID_user, titulo, codigo) -> None:
            super().__init__(ID_user, titulo, codigo)

        def __init__(self, tipo,autor,edicion) -> None:
            self.tipo=tipo
            self.autor=autor
            self.edicion=edicion

        def reservar(self):
            fecha = datetime.datetime
            return fecha

        def entregar(self):
            fecha = datetime.datetime
            return fecha
            pass
    except:
        print("Ocurrio algun error")


class tipo_revista(revista):
    try:
        def __init__(self, tipo, autor, edicion) -> None:
            super().__init__(tipo, autor, edicion)
        
        def __init__(self, fisico, digital) -> None:
            self.fisico=fisico
            self.digital=digital

        def reservar(self):
            fecha = datetime.datetime
            return fecha

        def entregar(self):
            fecha = datetime.datetime
            return fecha
            pass
    except:
        print("Ocurrio algun error")



class bibliotecario(lector):
    try:
        def __init__(self, nombre, direccion, telefono) -> None:
            super().__init__(nombre, direccion, telefono)

        def __init__(self, id_personal) -> None:
            self.id_personal=id_personal

        def reservar(self):
            fecha = datetime.datetime
            return fecha

        def entregar(self):
            fecha = datetime.datetime
            return fecha
            pass
    except:
        print("Ocurrio algun error")


op = pedido(12345, "el general no tiene quien le escriba", 54321)
ap = lector("juan", "calle 34", 3208508703)
jc = bibliotecario(56778)
print(op.entregar())
print(ap.cont)
