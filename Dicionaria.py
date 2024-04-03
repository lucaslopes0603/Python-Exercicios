#1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
#2 - Utilizando o dicionário criado no item 1:Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa); Adicione um campo de profissão para essa pessoa;Remova um item do dicionário.
#3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
#4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
#5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

#1
pessoa = {'nome': 'Artur', 'idade': 20, 'cidade': 'Belo Horizonte'}

#2
pessoa['idade'] = 30
pessoa['profissao'] = 'Programador'
del pessoa['cidade']


print(f'{pessoa['idade'], pessoa['nome'], pessoa['profissao']}')

#3
numeros_quadrados = {x: x*x for x in range(1, 6)}
print(numeros_quadrados)

#4
chaves = {'nome':'Amanda','idade':23,'cidade':'Sao Paulo'}
nome_escolhido = input('Coloque um nome (DICA:Começa e termina com A): ')
if chaves['nome'] == nome_escolhido:
    print('Parabens você acertou o nome')
else:
    print('Errado')     


#5
frase = "Eu sou sou muito legal"
contagem = {}
palavras = frase.split()
for palavra in palavras:
    contagem[palavra] = contagem.get(palavra,0) + 1
print(contagem)    