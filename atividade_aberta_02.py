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
print(media)


# 2) Crie um programa de repetição que receba uma matriz de tamanho 5x5 e imprima a
# soma de cada linha

import numpy as np
matriz = [[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]]

for linha in range(0,5): # linha = 0,1
    soma = 0
for coluna in range(0,5): # coluna = 0,1,2
    soma = soma + matriz[linha][coluna]
print(soma)

