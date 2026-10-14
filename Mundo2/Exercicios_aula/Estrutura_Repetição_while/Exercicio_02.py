'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer'''

from random import randint

computador = randint(0, 10 )
palpite = -1 # valor neutro, fora do sorteio (0 a 10), só para entrar no while 
contador = 0
print('Sou seu computador... Acabei de Pensar em um número entre 0 e 10. Tente adivinhar...')
while palpite != computador:
    palpite = int(input('Qual é o seu palpite? '))
    contador += 1

print (f'Parabéns! Você acertou o número {computador} em {contador} tentativa(s)!')