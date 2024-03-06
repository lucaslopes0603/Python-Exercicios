#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.
#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.

def exercicio1():
    numero = int(input("Insira um numero: "))
    if numero % 2 == 0:
            print("PAR")
    else:
            print("IMPAR")    

def exercicio2():
      idade = int(input("Coloque sua idade: "))
      if 0<idade<= 12:
            print('Você é criança')
      elif 13>=idade<=18:
            print ('Você é adolescente')
      elif idade>18:
            print('Você é adulto')           
      else:
            print("Valor Invalido")  
    
def exercicio3(): 
      usuario_correto = "peixes"
      senha_correta = "amebas"
      usuario = input("Digite seu usuario: ")
      senha = input("Digite sua senha: ")
      if usuario == usuario_correto and senha == senha_correta:
            ("Acesso permitido")
      else:
            print("Usuario ou senha errada")         
      
def exercicio4():
        x = float(input("Digite a coordenada x: "))
        y = float(input("Digite a coordenada y: "))

        if x > 0 and y > 0:
            print("O ponto está no primeiro quadrante.")
        elif x < 0 and y > 0:
            print("O ponto está no segundo quadrante.")
        elif x < 0 and y < 0:
            print("O ponto está no terceiro quadrante.")
        elif x > 0 and y < 0:
            print("O ponto está no quarto quadrante.")
        else:
            print("O ponto está sobre um eixo ou na origem.")
      

exercicios = int(input(""" 1-Exercicio Par ou impar
 2-Exercicio de Idade
 3-Exercicio Usuario e Senha 
 4-Exercicio de Cordenada                      
 -Selecione o Exercicio que você quer:"""))
if exercicios == 1:
    exercicio1()
elif exercicios == 2:
      exercicio2()
elif exercicios == 3:
      exercicio3()   
else:
      exercicio4()



