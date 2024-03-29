#1 - Crie uma lista para cada informação a seguir:
#Lista de números de 1 a 10;
#Lista com quatro nomes;
#Lista com o ano que você nasceu e o ano atual.
#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
#7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ['Lucas','Pedro','Vinicius','Gustavo']
anos = [2003,2024]
lista_numeros = [32,322,12,32213,23,212,21,8734,3236,43]


def percorrer():
    for numero in numeros:
        print(numero)

def calcular_variavel():
    soma_impares = 0
    for i in range(1, 11, 2):
        soma_impares += i
    print(soma_impares)

def decrescente():
    i=9    
    for numero in numeros:
        print(numeros[i])   
        i-=1

def tabuada():
    i = 10
    tabuada = int(input('Digite um Numero: '))
    while i>0:
        print(tabuada * i)
        i-=1

def soma():
   
    soma = 0
    try:
        for listas in lista_numeros:
            soma += listas  
        print(f'A soma é:{soma}')
    except Exception as e:
        print(f"Ocorreu um erro: {e}")    

def media():
    media = len(lista_numeros)
    soma = 0
    try:
        for listas in lista_numeros:
            soma += listas
        print (f'A media é {soma/media}')
    except ZeroDivisionError:
        print("Nao pode dividir por zero")
    except Exception as e:
        print(f'Ocorreu um erro {e}')            

                    

percorrer()
calcular_variavel()
decrescente()
tabuada()
soma()
media()



