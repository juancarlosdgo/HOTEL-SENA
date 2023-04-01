'''modulo de python. origen'''

'''Aqui se encuentran ejercicios de funciones, condicionales y excepciones'''

'''programa que tome un numero ingresado y con el determine si es postivo, negativo o cero,
ademas contruirlo con algunas excepciones.'''

def condi1 (num):
    try:
        if num > 0:
            return "el numero es positivo"
        elif num < 0:
            return "el numero es negativo"
        else:
            return "el numero es cero"
    except ValueError:
        return "ingresa datos numericos"
    except SyntaxError:
        return " existe un error en al dato que escribiste"
    except AttributeError:
        return "error de atributos"
    except TypeError:
        return "error del tipo d dato"


'''crear un programa que tome un dato ingresado sobre la edad de una persona y con el 
determine, si esa persona es mayor o menor de edad. '''

def condi2 (edad):
    try:
        if edad >= 18 and edad < 100:
            return "eres mayor de edad. ya te cabe"
        elif edad < 0:
            return "ese dato es incorrecto"
        else:
            return "eres menor de edad"
    except ValueError:
        return "ingresa datos numericos"
    except SyntaxError:
        return " existe un error en al dato que escribiste"
    except AttributeError:
        return "error de atributos"
    except TypeError:
        return "error del tipo de dato"


'''crear un programa que al recibir como dato el salario de un instructor del SENA del area
de ADSO, calcule el incremento del salario del año 2023 tomando como base que aumento fue del
16% '''
def condi3 ():
    sal = int(input("ingrese el valor de su salario como instructor del SENA: "))
    res = sal * 0.16
    res2 = res + sal
    try:
        if sal > 1160000:
            return "el valor tu incremento es de: ", res, "y el valor total de salario es de: ",res2
        else:
            return "no puedes gnar menos del salrio minimo establecido. Acaso eres Aprendiz del SENA"
    except ValueError:
        return "ingresa datos numericos"
    except SyntaxError:
        return " existe un error en al dato que escribiste"
    except AttributeError:
        return "error de atributos"
    except TypeError:
        return "error del tipo de dato"


'''crear un programa que al recibir dos numeros enteros. determine si uno es divisor de otro'''

def condi4 (num1, num2):
    num1 = int(input("ingrese un numero: "))
    num2 = int(input("ingrese otro numero: "))
    try:
        if num1 & num2 == 0:
            return num2, "es divisor de, ", num1
        else:
            return num2, "no es divisor de, ", num1
    except ValueError:
        return "ingresa datos numericos"
    except SyntaxError:
        return " existe un error en al dato que escribiste"
    except AttributeError:
        return "error de atributos"
    except TypeError:
        return "error del tipo de dato"


'''crear un programa que muestre vario valores de una lista en desorden y los organice'''

def condi5 ():
    lis = [6,5,3,9,5,1,2,9,2,8,3,5,0,4,8,9,1,4]
    print(lis)
    try:
        for i in range(1,len(lis)):
            for posicion in range (len(lis)- i):
                if lis[posicion] > lis[posicion + 1]:
                    temp = lis[posicion]
                    lis[posicion] = lis[posicion + 1]
                    lis[posicion + 1] = temp
        return lis
    except ValueError:
        return "ingresa datos numericos"
    except SyntaxError:
        return " existe un error en al dato que escribiste"
    except AttributeError:
        return "error de atributos"
    except TypeError:
        return "error del tipo de dato"