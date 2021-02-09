def reves(my_num):
    if not my_num.isdigit():
        dot=my_num.split('.')
        if len(dot) == 2 and (dot[0].isdigit() and dot[1].isdigit()):
            print(num[::-1])
        else:
            print('Valor incorrecto solo se aceptan Enteros o Flotantes')
            exit()
    else:
        print(num[::-1])



num = input("Introduce un numero: ")
print(type(num))
reves(num)


