'''cuantas veces se repita un caracter dado'''


def carac():
    c = input("ingrese una cadena: ")
    d = list(c)
    e = []
    f = 0
    for i in d:
        if i in d:
            e.append(i)
            print(e)
            if i in e:
                f+=1
                print(f)

print(carac())