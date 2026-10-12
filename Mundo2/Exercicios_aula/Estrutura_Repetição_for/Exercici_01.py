''''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
 indo de 10 até 0, com uma pausa de 1 segundo
 entre eles.'''


#from time import # aqui usamos a bibliteca completa
from time import sleep # utilizando apenas o sleep
for c in range(10, -1, -1):
    print(c)
    #time.sleep(1)
    sleep(1)
print('BOOM')