
#!TERCEIRA QUESTÃO DA PROVA DE DICIONARIO E TUPLA - ISABELI MACHADO - 2137 - 25/09
dicionario = {}


#!B)-------------------------------------------------------------

def atualizar():
    if nome in dicionario.keys():
        quantidade = int(input(f'digite a nova quantidade de {nome}: '))
        dicionario.update({nome:quantidade})
        print('alterado!')
    else:
        print(f'{nome} não alterado')

#!A)-------------------------------------------------------------

def adicionar():
    dicionario[nome] = quantidade

#!C)-------------------------------------------------------------

def remover():
    if nome in dicionario.keys():
        del dicionario[nome]
        print('removido!!!')
    else:
        print(f'{nome} não achado!')

#!D)-------------------------------------------------------------

def visualizar():
    print('produtos: ')
    for chave,valor in dicionario.items():
        print(f'{chave}:{valor}')

#!E)-------------------------------------------------------------

def consulta():
    if nome in dicionario.keys():
        print(f'a quantidade dde {nome} é {dicionario[nome]}')
    else:
        print('nao cadastrado!!!')

while True:    
    print('-'*20)
    print("menu de opções\n\nA-adicionar produto\nB-atualizar estoque\nC-remover produto\nD-visualizar estoque\nE-consultar produto\nF-sair")
    print('-'*20)
    print('')

    op = input('digite a opção do menu: ').lower()

    if op == 'a':
        nome = input("digite o nome do produto: ")
        quantidade = int(input('digite a quantidade do produto anterior: '))
        adicionar()
    
    elif op == 'b':
        nome = input('digite o nome do produto que quer atualizar: ')
        atualizar()

    elif op == 'c':
        nome = input('digite o nome do produto que quer excluir: ')
        remover()

    elif op == 'd':
        visualizar()
    
    elif op == 'e':
        nome = input('digite o produto que voce quer consultar(nome dele): ')
        consulta()
    
    elif op == 'f':
        print('encerrando programa... tchau!!!')
        break