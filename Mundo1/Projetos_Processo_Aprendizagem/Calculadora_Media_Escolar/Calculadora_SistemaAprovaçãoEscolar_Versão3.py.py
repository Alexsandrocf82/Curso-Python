'''Projeto 4 — Sistema de Aprovação Escolar

Desenvolva um sistema que leia:

o nome do aluno
três notas (nota1, nota2, nota3)
o percentual de frequência do aluno nas aulas (de 0 a 100)

Calcule a média aritmética das três notas.

Regras de aprovação:

Se a frequência for menor que 75%, o aluno está automaticamente reprovado por falta — não importa a média, nem precisa calculá-la considerar pra decidir isso.
Se a frequência for suficiente (75% ou mais), aplique as regras normais:
Média maior ou igual a 7 → Aprovado
Média entre 5 (inclusive) e 7 (exclusive) → vai pra exame final: leia uma nova nota (a do exame) e calcule a média entre a média anterior e essa nova nota. Se esse resultado for maior ou igual a 5, o aluno é aprovado; senão, reprovado.
Média menor que 5 → Reprovado direto, sem direito a exame final

Ao final, exiba um relatório com: nome do aluno, frequência, média final calculada, e a situação (Aprovado / Reprovado por nota / Reprovado por falta).'''

nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
frequencia = float(input('Digite a frequencia do aluno'))
media = (nota1+nota2+nota3)/3
if frequencia < 75:
    print(f'Aluno: {nome}, Reprovado por Falta')
else:
    if media >= 7:
        print(f'Aluno: {nome}, Aprovado com Média: {media:.2f}')
    elif media >= 5:
        exame_final = float(input('Digite a nota do exame final: '))
        if exame_final >= 7:
            print(f'Aluno: {nome}, Aprovado por Exame Final')
        else:
            print(f'Aluno: {nome}, Reprovado por Exame Final')
    else:
        print(f'Aluno: {nome}, Reprovado por média Menor que :{media:.2f}')
  
