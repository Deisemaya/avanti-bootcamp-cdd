from math import pi

raio =float(input('Informe o raio do circulo em cm que deseja calcular a area ')) 

def area(raio):
    return pi * (raio**2)

print(f'Area do circulo = {round(area(raio), 2)} cm')
    
