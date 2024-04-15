# 1) Em python, qual a saída esperada para o seguinte código:

a = 13
b = 18
c= b - a
d = a + c
e = b - c 
                     # RESPOSTAS:
print("b - a = ", c) # b - a =  5
print("a + c = ", d) # a + c =  18
print("b - c = ", e) # b - c =  13
print("a > b: ", a > b) # a > b:  False
print("d < b: ", d < b) # d < b:  False
print("a != a: ", a != a) # a != a:  False
print("a >= d: ", a >= d) # a >= d:  False
print("d <= e: ", d <= e) # d <= e:  False


# 2) Em python, qual a saída esperada para o seguinte código:

a = 5
b = 2
c = b* a
d = a * a 
e = b * b
                     # RESPOSTAS:
print("b * a = ", c) # b * a =  10
print("a * a = ", d) # a * a =  25
print("b * b = ", e) # b * b =  4
print("d > e : ", d > e) # d > e :  True
print("d < e : ", d < e) # d < e :  False
print("d == (a * a): ", d == (a * a)) # d == (a * a):  True
print("(d * b) != (e * a): ", (d * b) != (e * a)) # (d * b) != (e * a):  True
print("a >= c: ", a >= c) # a >= c:  False
print("c <= e: ", c <= e) # c <= e:  False


# 3) Para o código seguinte, qual a saída esperada:

x = 64

while x > 2:
    print(x)
    x = int(x/2)
    
# RESPOSTAS:
# 64
# 32
# 16
# 8
# 4

# 4) Para o seguinte código:

nota = int(input("digite uma nota entre 0 e 100; "))

while nota > 100 or nota <0:
    print("nota invalida!")
    nota = int(input("digite uma nota entre 0 e 100: "))

if nota < 60:
    print("aluno reprovado")
else:
    print("aluno aprovado")

# RESPOSTAS:
# 101 - nota invalida!
# 80 - aluno aprovado







