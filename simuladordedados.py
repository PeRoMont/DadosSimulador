# Bibliotecas
from random import randint #Biblioteca para geração de números aleatoriamente
from time import sleep #Biblioteca para o temporizados

# Lista
listanum = []

print('=' * 35)
print('Bem-vindo(a) ao SIMULADOR DE DADOS')
print('=' * 35)
sleep(2)

while True:
    perg = str(input('Você quer rodar os dados? [S/N]: ')).strip().upper() #Pergunta se quer rodar os dados
    if perg == 'N': #Caso não queira rodar mais ele para
        break
    while perg != 'S':
        perg = str(input('Escolha inválida! Insira novamente como [S ou N]\nInsira novamente: ')).strip().upper() #Pergunta novamente caso "S ou N" não tenha sido inserido
        if perg == 'N': #Caso não queira rodar mais ele para
            break
    print('Girando os dados...')
    dados = randint(1, 6) #Gerar o valor que vai sair no dado
    sleep(2)
    print(f'O número que saiu nos dados foi: {dados}')
    print('=' * 35)
    listanum.append(dados) #Adicionar os valores a uma lista

print(f'Lista com os números que saíram: {listanum}') #Apresentar os valores da lista
print('Programa Finalizado!\nATÉ LOGO!')
