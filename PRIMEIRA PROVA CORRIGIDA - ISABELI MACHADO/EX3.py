dicionario = {}
def alterar():
    if nome in dicionario.keys():
        del dic[nome]
        print('alterado!')
    else:
        print(f'{nome} não alterado')

def adicionar():
    dicionario[nome] = a

def remover():
    if nome in dicionario.keys():
        del dicionario[nome]
        print('removido!!!')
    else:
        print(f'{nome} não achado')

def visualizar():
    print('produtos: ')
    for chave,valor in dicionario.items():
        print(f'{chave}:{valor}')

def consulta():
    if nome nome in dicionario.keys()

while True:    
    print("menu de opções\n\nA-adicionar produto\nB-atualizar estoque\nC-remover produto\nD-visualizar estoque\nE-consultar produto\nF-sair")
