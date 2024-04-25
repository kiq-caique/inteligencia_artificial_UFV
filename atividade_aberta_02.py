# 1) Utilizando vetores e comando de repetição, crie um código que receba as notas de 5
# atividades, que será informada pelo usuário. Em seguida, faça a média das notas e
# imprima na tela a média e “Aluno aprovado!” caso a média seja superior ou igual a
# 60,0 e “Aluno reprovado” caso a média seja inferior a 60,0.

import numpy as np
notas = np.empty(5, dtype=float)

for i in range(0,5): #i=0,1,2,3,4
    nota = float(input("Digite a nota %d do aluno: " %(i+1)))
    notas[i] = nota

media = 0
for i in range(0,5):
    media = media + notas[i]
media = media/5

if media >= 60:
    print("Aluno aprovado com média %.2f!" % media)
else:
    print("Aluno repovado com média %.2f" % media)

print(notas)

# 2) Crie um programa de repetição que receba uma matriz de tamanho 5x5 e imprima a
# soma de cada linha

import numpy as np
matriz = [[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]]

for linha in range(0,5): # linha = 0
    soma = 0
for coluna in range(0,5): # coluna = 0,1,2,3,4
    soma = soma + matriz[linha][coluna]
print(soma)

import numpy as np
matriz = np.empty((5,5))

# leitura da matriz
for i in range(0,5):
    for j in range(0,5):
        num = float(input("Digite o elemento da linha %d, coluna %d: " %(i+1,j+1)))
        matriz[i][j] = num

# calcular soma das linhas
for i in range(0,5):
    soma = 0
    for j in range(0,5):
        soma = soma + matriz[i][j]
    print(soma)


# 3) Crie uma função que receba dois inteiros ent1 e ent2 . Essa função deve imprimir todos os textos quando a condição for atendida:
# “ent1 - ent2 é negativo”, condição: caso ent1 menos ent2 seja menor que zero,
# “ent1 * ent2 é negativo”, condição: caso ent1 multiplicado por ent2 seja menor que zero,
# “ent1 + ent2 é negativo”, condição: caso ent1 somado a ent2 seja menor que zero.

def questao3(ent1,ent2): #10,1
  if ent1 - ent2 <0:
    print("ent1 - ent2 é negativo")
  if ent1 * ent2 <0:
    print("ent1 * ent2 é negativo")
  if ent1 + ent2 <0:
    print("ent1 + ent2 é negativo")

#testa en1 - ent2 menor que zero, outras duas opções positivo
a= 1
b= 2
print("\nteste 1 (%d, %d):" %(a,b))
questao3(a,b)

#testa ent1 * ent2 negativo, outras duas opções positivo
a= 10
b = -1
print("\nteste 2 (%d, %d):" %(a,b))
questao3(a,b)

#testa ent1 + ent2 negativo, outras duas opções positivo
a= -1
b = -2
print("\nteste 3 (%d, %d):" %(a,b))
questao3(a,b)

#testa todas opções negativas
a= -10
b=1
print("\nteste 4 (%d, %d):" %(a,b))
questao3(a,b)

#testa todas opções positivas
a= 10
b = 1
print("\nteste 5 (%d, %d):" %(a,b))
questao3(a,b)

# 4) Crie uma função que receba um caractere, um string e o tamanho do string. Essa função deve substituir os caracteres de índice par do string pelo caractere informado como parâmetro de entrada e retornar o novo string gerado.
