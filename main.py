def q1():
    """
    1. Escreva um programa que solicita um número ao usuário e determina se 
    é positivo, negativo ou zero. 
    """
    n = int(input("Digite um numero"))
    if n > 0:
        print("positivo")
    elif n < 0:
        print("negativo")
    else:
        print("zero")

def q2():
    """
    2. Verificação de Número Par/Ímpar: Crie um programa que pede ao usuário 
    um número e imprima se ele é par ou ímpar.
    """
    n= int(input('Digite um numero: '))
    if n %2 == 0:
        print('par')
    else: 
        print('ímpar')

    

def q3():
    """
    3. Calculadora Simples: Faça uma calculadora que pede ao usuário dois 
    números e uma operação (+, -, *, /) e imprima o resultado dessa operação.
    """
    n1 = float(input('Digite um valor: '))
    n2 = float(input('Digite outro valor: '))
    op = input('Digite uma operação: ')

    if op == '+':
        print(n1 + n2)
    elif op == '-':
        print(n1-n2)
    elif op == '*':
        print(n1 * n2)
    elif op == '/':
        print(n1 / n2)       
    

def q4():
    """
    4. Maior de Três Números: Escreva um programa que solicita três números 
    ao usuário e imprima o maior dentre eles.
    """
    n1 = float(input('Digite um valor: '))
    n2 = float(input('Digite outro valor: '))
    n3 = float(input('Digite um valor: '))

    if n1 > n2 and n1 > n3:
        print(n1)
    elif n2 > n1 and n2 > n3:
        print(n2)
    else:
        print(n3)        
    
def q5():
    """
    5. Classificação de Idade: Peça a idade do usuário e imprima a classificação
    em "Criança" (0-12), "Adolescente" (13-19), "Adulto" (20-59) ou "Idoso" (60+).
    """
    idade = int(input("Digite sua idade: "))

    if idade >= 0 and idade <= 12:
        print('Criança')
    elif idade >= 13 and idade <= 19:
        print('Adolescente')
    elif idade >= 20 and idade <= 59:
        print('Adulto')
    else:
        print('Idoso')        

def q6():
    """
    6. Verificação de Triângulo: Peça ao usuário o comprimento de três 
    lados e verifique se eles podem formar um triângulo. Se sim, determine 
    se é um triângulo equilátero, isósceles ou escaleno.
    """
    n1 = int(input('Digite um comprimento: '))
    n2 = int(input('Digite um comprimento: '))
    n3 = int(input('Digite um comprimento: '))

    if n1 + n2 < n3 or n2 + n3 < n1 or n3 + n1 < n2:
        print('Inválido')
    elif n1 != n2 != n3:
        print("Escaleno")  
    elif n1 == n2 == n3:
        print("Equilátero") 
    elif n1 == n2 != n3 or n2 == n3 != n1 or n3 == n1 != n2:
        print("Isósceles")        

def q7():
    """
    7. Conversão de Notas: Escreva um programa que converte uma nota 
    de 0 a 100 em uma escala de conceitos: 
    A (90-100), B (80-89), C (70-79), D (60-69), E (50-59).e F (0-49)
    """
    notas = int(input("Digite sua nota: "))

    if notas >= 90 and notas <=100:
        print('A')
    elif notas >= 80 and notas <=89:
        print('B')
    elif notas >= 70 and notas <= 79:
        print('C')
    elif notas >= 60 and notas <=69:
        print('D')             
    elif notas >= 50 and notas <=59:
        print('E')
    else:
        print('F')                 

def q8():
    """
    8. Validação de Login: Crie um programa que pede ao usuário um nome 
    de usuário e uma senha. Se o nome de usuário for "admin" e a senha for 
    "12345", exiba "Acesso concedido", caso contrário, exiba "Acesso negado".
    """
    usuario = input('Digite seu usuário: ')
    senha = int(input('Digite sua senha: '))

    if senha == 12345 and usuario == 'admin':
        print('Acesso concedido')
    else:
        print('Acesso negado')    

def q9():
    """
    9. Calculadora de IMC: Peça ao usuário sua altura e peso e calcule o
      índice de massa corporal (IMC). Em seguida, mostre uma mensagem 
      indicando se a pessoa está: Abaixo do peso, Peso normal, Sobrepeso, 
      Obeso ou Muito obesa.
    """
    peso = float(input('digite seu peso: '))
    altura = float(input('Digite sua altura: '))
    imc = peso / altura ** 2
    
    if imc <= 18.5:
        print('Abaixo do peso')
    elif imc >=18.6 and imc <= 24.9:
        print('Peso normal') 
    elif imc >= 25.0 and imc <= 29.9:
        print('Sobrepeso')
    elif imc >= 30.0 and imc <= 34.9:
        print('Obeso')
    else:
        print('Muito obeso')    


def q10():
    """
    10. Verificação de Ano Bissexto: Escreva um programa que verifica 
    se um ano fornecido pelo usuário é bissexto ou não.
    """
    pass