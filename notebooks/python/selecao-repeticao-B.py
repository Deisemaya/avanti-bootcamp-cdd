import random

# numero = int(input('Escolha um numero  entre 1 e 100'))
numero_sorteado = random.randint(1,11)
print(numero_sorteado)

numero =0
while numero != numero_sorteado:
    numero = int(input('Escolha um numero  entre 1 e 100 '))
    if numero > 100:
        print('numero invalido,escolha um numero entre 1 e 100')
    if numero == numero_sorteado:
        print('Parabens voce acertou')
        break
    if numero > numero_sorteado and numero <= 100: 
          print('Tente outra vez, Escolha um numero um pouco menor')
       
    if numero < numero_sorteado:
        print('tente outra vez, escolha um numero um pouco maior')

        

    
        
print('Jogo finalizado')





