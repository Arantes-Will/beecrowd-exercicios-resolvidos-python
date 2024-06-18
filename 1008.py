# Salário
# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o
# salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

numero = int(input())
horas = int(input())
salario = float(input())

print(f'NUMBER = {numero}')
print(f'SALARY = U$ {(horas*salario):.2f}')