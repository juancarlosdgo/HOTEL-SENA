'''cual es el valor numerico de acuerdo a los codigos del alfabeto'''
def valnum():
    abc= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in abc:
        if ord(i):
            print(ord(i))

valnum()
