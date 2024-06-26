# Distância Entre Dois Pontos
# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2)
# e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

# Distancia = sqrt((x2-x1)²+(y2-y1)²)
import math

x1,y1 = input().split()
x2,y2 = input().split()

distancia = math.sqrt((float(x2)-float(x1))*(float(x2)-float(x1)) + (float(y2)-float(y1))*(float(y2)-float(y1)))
print(f'{distancia:.4f}')

