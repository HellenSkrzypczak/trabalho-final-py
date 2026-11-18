# 1 - Faça uma função que solicite 3 notas e imprima a média;

# def notas():
#     notas = []
#     somaNotas = 0

#     for i in range(3):
#         nota = float(input(f"Informe a {i + 1}º nota: "))
#         notas.append(nota)

#     for i in range(len(notas)):
#         somaNotas += notas[i]

#     media = somaNotas / (len(notas))
#     print(f"Média das notas: {media:.2f}")

# notas()

# 2 -  Faça uma função que leia um nome e um cpf e retorne os dados para quem chamou a função.

# def leitura_dados():
#     cpf = int(input("Informe o CPF: "))
#     nome = input("Informe o nome: ")

#     return cpf, nome

# cpf, nome = leitura_dados()
# print(f"CPF: {cpf}, Nome: {nome}")

# 3 -  Faça um programa que leia fora da função o nome e duas notas de 5 alunos e mostre a média final de cada estudante. O cálculo da média deve ser realizado em uma função. O retorno deve ser o valor da média.

# alunos = []

# # A função recebe apenas a lista de notas de UM aluno, ex: [8.0, 9.0]
# def calcular_media(lista_notas):
#     soma = 0
#     for j in range(len(lista_notas)):
#         soma += lista_notas[j]
    
#     media = soma / len(lista_notas)
#     return media


# # Leitura dos dados (mude para range(5) na versão final)
# for i in range(3):
#     notas = []
#     nome = input(f"Informe o nome do aluno {i + 1}: ")

#     for j in range(2):
#         nota = float(input(f"Informe a {j + 1}ª nota de {nome}: "))
#         notas.append(nota)

#     alunos.append([nome, notas])


# # Percorrendo a matriz para exibir cada aluno e chamar a função
# for i in range(len(alunos)):
#     nome_aluno = alunos[i][0]
#     notas_aluno = alunos[i][1]
    
#     media_final = calcular_media(notas_aluno)
#     print(f"Aluno: {nome_aluno} | Notas: {notas_aluno} | Média: {media_final:.2f}")


# 4 - Escreva um programa que leia dois valores e calcule qual o menor deles definindo a função min. A função min deve receber os dois valores de entrada e retornar o menor deles;

# 5 - Faça uma função que lê cinco (5) números inteiros digitados pelo usuário e no final imprima esses números ordenados. 

# 6 - Encontre os número primos gêmeos entre 1 e 1000, usando uma função para verificar se o número é primo. Primos gêmeos são aqueles que a diferença entre valores primos é igual a 2. Por exemplo, o número 5 e 7 são primos gêmeos.

# 7 - Dadas duas sequências com n números inteiros entre 0 e 9, interpretadas como dois números inteiros de n algarismos, faça uma função para calcular a sequência de números que representa a soma dos dois inteiros. 
# Exemplo: n1[8] = 8,2,4,2,4,2,5,1    n2[8]= 3,3,7,5,2,3,3,7
# saída: 1	1	6	1	7	6	5	8	8

# 8 - Faça uma função que receba um número inteiro positivo como parâmetro e retorne 1 ​ se o número em questão é perfeito, ou ​ 0(zero) caso contrário. Um número perfeito é ​aquele cuja soma de todos os seus divisores positivos (excluindo ele mesmo) é igual ao próprio número. Por exemplo, o número 6 é ​ um número perfeito, pois: 6 ​ = 1 + 2 + 3 . ​
# O próximo número perfeito é o 28, pois 28 ​ = 1 + 2 + 4 + 7 + 14 . ​

# Class
# 4 - Crie uma lista com 3 carros (class Car) e imprima todos.

# carros = []

# class Car:
#     Id = None
#     Modelo = None

# carro1 = Car()
# carro1.Modelo = 'Chevrolete'
# carro1.Id = 1

# carro2 = Car()
# carro2.Modelo = 'Caminhonete'
# carro2.Id = 2

# carro3 = Car()
# carro3.Modelo = 'Cavalo'
# carro3.Id = 3

# carros.append(carro1)
# carros.append(carro1)
# carros.append(carro3)

# for carro in carros:
#     print(f"ID: {carro.Id} | Modelo: {carro.Modelo}")


# 5 Escreva adiciona_conta(vetor): lê os dados do usuário e adiciona uma nova conta na lista.

# 6 - Escreva uma função que imprima os clientes com saldo maior que N reais, recebido por parâmetro.

class Clientes:
    Nome: None
    Saldo: None

def imprimir_saldo():


cUm = Clientes()


# 7 - Escreva uma função que transfira 100 reais da conta 2 para a conta 9. Se a conta de origem ficar com saldo menor que −100, aborte a operação.