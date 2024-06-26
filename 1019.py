# Conversão de Tempo
# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:
# minutos:segundos.

segundos = int(input())

horas = segundos//3600
minutos = (segundos%3600) // 60
seg = ((segundos%3600)%60)//1
print(f'{horas}:{minutos}:{seg}')