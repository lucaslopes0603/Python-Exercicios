class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praça = Restaurante()
restaurante_praça.nome = 'Praça'
restaurante_praça.categoria = 'Italiana'
nome_restaurante = restaurante_praça.nome

if(restaurante_praça.ativo == False):
    print('Inativo')
else:
    print('Nativo')    


categoria = Restaurante.categoria
restaurante_praça.nome = 'Bistro'

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = False

if(restaurante_pizza.categoria == 'Fast Food'):
    print('Igual')
else:
    print('Diferente')    

restaurante_pizza.ativo = True

print(f'Nome:{restaurante_praça.nome}  Categoria:{restaurante_praça.categoria}')
