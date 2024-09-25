
#!PRIMEIRA QUESTÃO DA PROVA DE DICIONARIO E TUPLA - ISABELI MACHADO - 2137 - 25/09
tuplaa = ()
cont = 0
for i in range(4):
    n = int(input('digite o número : '))
    tuplaa += (n, )
    print(tuplaa)
#!A-------------------------------------------------------------

    if n == 9:
        cont += 1
        print(f"9 está na tupla, {cont} vezes")
print("")

#!B-------------------------------------------------------------

y=3
if y in tuplaa:
    print(f"3 está na posição {tuplaa.index(y)}") 
else:
    print('valor não está na tupla')

#!C-------------------------------------------------------------

for i in tuplaa:    
    if i % 2 == 0:
        print(f"{i} é par")

#!D-------------------------------------------------------------

soma = sum(tuplaa)
media = soma/len(tuplaa)
print(f'{media} é a media da tupla')