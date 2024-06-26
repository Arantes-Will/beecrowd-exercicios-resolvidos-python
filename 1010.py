# Cálculo Simples
# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1,
# o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

codigo1, numero1, valor1 = input().split()
codigo2, numero2, valor2 = input().split()
pagamento = (int(numero1)*float(valor1)) + (int(numero2)*float(valor2))

print(f'VALOR A PAGAR: R$ {pagamento:.2f}')


