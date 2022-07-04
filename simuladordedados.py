# Bibliotecas
from random import randint
from time import sleep

# Lista
listanum = []

print('=' * 35)
print('Bem-vindo(a) ao SIMULADOR DE DADOS')
print('=' * 35)
sleep(2)

while True:
    perg = str(input('Você quer rodar os dados? [S/N]: ')).strip().upper()
    if perg == 'N':
        break
    while perg != 'S':
        perg = str(input(
            'Escolha inválida! Insira novamente como [S ou N]\nInsira novamente: ')).strip().upper()
        if perg == 'N':
            break
    print('Girando os dados...')
    dados = randint(1, 6)
    sleep(2)
    print(f'O número que saiu nos dados foi: {dados}')
    print('=' * 35)
    listanum.append(dados)

print(f'Lista com os números que saíram: {listanum}')
print('Programa Finalizado!\nATÉ LOGO!')
