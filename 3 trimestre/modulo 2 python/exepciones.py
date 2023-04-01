#programa que muestre la raiz de un numero... ((ASSERT))
def fun():
    x = int(input("ingrese un numero:"))
    assert x >= 0
    y = x ** 2
    return y
    


try:
    print(fun())
except(TypeError, ValueError, SyntaxError):
    print("error")