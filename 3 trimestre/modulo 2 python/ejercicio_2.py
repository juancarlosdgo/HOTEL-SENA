'''pida una cadena por teclado y diga cual es su valor al sumar sus codigos'''
def sumdig ():
    a = input(" ingrese una cadena: ")
    sum = 0 
    for i in a:
        if ord(i):
            sum += ord(i)
    return sum

print(sumdig())

