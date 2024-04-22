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