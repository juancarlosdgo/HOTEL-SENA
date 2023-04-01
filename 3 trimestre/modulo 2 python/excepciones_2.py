#importerror

def errorsyn():
    from math import sqrts
    x = int(input("ingresa un numero: "))
    y = sqrt(x)
    return y
    
try:
    print(errorsyn())

except SyntaxError:
    print("error de sintaxis")
except ImportError:
    print("error al momento de importa la funcion ")
except ValueError:
    print("error de valor")
except TypeError:
    print("error del tipo de dato")