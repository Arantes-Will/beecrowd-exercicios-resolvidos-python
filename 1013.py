# O Maior
# Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:
# MaiorAB = (a + b + abs * (a-b))/2
# Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário
# para chegar no resultado esperado.

a,b,c = input().split()

MaiorAB = (int(a) + int(b) + abs(int(a)-int(b)))/2
MaiorAC = (MaiorAB + int(c) + abs(MaiorAB-int(c)))/2

print(f'{int(MaiorAC)} eh o maior')



