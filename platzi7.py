import random

def run():
    na = random.randint(1, 100)
    n = int(input('ingrese un numero del 1 al 100: '))
    while n != na:
        if na < n:
            print('escribe un numero mas pequeño')
        else:
            print('escribe un numero mas grande')
        n = int(input('ingrese otro numero: '))
    print('ganaste')


run()

