
#!SEGUNDA QUESTÃO DA PROVA DE DICIONARIO E TUPLA - ISABELI MACHADO - 2137 - 25/09
carros = {}
cont = 0

print("menu de opções\n\nC-cadastrar\nA-alterar\nE-excluir\nP-pesquisar\nS-sair")

print('')
while True:

    op = input('digite a opção do menu: ').lower()
    print('')

    #!A)-------------------------------------------------------------

    if op == "c":
        lista = []
        cont += 1
        marca= input("digite a marca do carro: ")  #posição 0      

        carro = input("digite o nome do carro: ") #posição 1    

        ano = int(input("digite o ano do carro: ")) #posição 2

        cor = input("digite a cor do carro: ") #posição 3
        # ou carros.update({cont:[marca,carro,ano,cor]}) 
        carros[cont] = [marca,carro,ano,cor]

        
    #!B)-------------------------------------------------------------

    elif op == 'a':
        cod = int(input("digite o codigo que voce quer alterar: "))
        if cod in carros:
            alteracao = input("voce quer alterar\nmarca\ncarro\nano\ncor: ").lower().strip()
            if alteracao == 'marca':
                nova_marca = input("digite a nova marca: ")
                carros[cod][0] = nova_marca

            elif alteracao == 'carro':
                novo_carro = input('digite o novo carro: ')
                carros[cod][1] = novo_carro

            elif alteracao == 'ano':
                novo_ano = int(input('digite o novo ano: '))
                carros[cod][2] = novo_ano

            elif alteracao == 'cor':
                nova_cor = input('digite a nova cor: ')
                carros[cod][3] = nova_cor

            else:
                print('digite uma opção valída')

    #!C)-------------------------------------------------------------

    elif op == 'e':
        cod = int(input("digite o codigo que voce quer alterar: "))
        if cod in carros: 
            del carros[cod]
        else:
            print('carro não encontrado!')

    #!D-------------------------------------------------------------
    
    elif op == 'p':
        for chave,valor in carros.items():
            print(f'codigo: {chave}\nMarca: {valor[0]}\nModelo: {valor[1]}\nAno: {valor[2]}\nCor: {valor[3]}')

    #!E)-------------------------------------------------------------

    elif op == 's':
        print('encerrando programa... tchau!!!')
        break
        




            
        





        


    
