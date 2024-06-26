# Consumo
# Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).

distancia_total = int(input())
combustivel_total = float(input())
consumo_medio = distancia_total/combustivel_total

print(f'{consumo_medio:.3f} km/l')