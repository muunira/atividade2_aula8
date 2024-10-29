nome_cliente1 = input('Nome: ')
idade_cliente1 = input('Idade: ')

nome_cliente2 = input('Nome: ')
idade_cliente2= input('Idade: ')

nome_cliente3 = input('Nome: ')
idade_cliente3 = input('Idade: ')

print('''Os tipos de quarto disponíveis são:
1. Simples: R$100,00 por dia.
2. Duplo: R$150,00 por dia.
3. Luxo: R$250,00 por dia. ''')

cliente1_quarto = input('''Digite o número do quarto que o cliente1 deseja:
>>> ''')
cliente2_quarto = input('''Digite o número do quarto que o cliente2 deseja:
>>> ''')
cliente3_quarto = input('''Digite o número do quarto que o cliente3 deseja:
>>> ''')

valor_simples = 100
valor_duplo = 150
valor_luxo = 250

cliente1_dias = int(input(f'Quantos dias o Cliente 1 ({nome_cliente1}) ficará hospedado? '))
cliente2_dias = int(input(f'Quantos dias o Cliente 2 ({nome_cliente2}) ficará hospedado?  '))
cliente3_dias = int(input(f'Quantos dias o Cliente 3 ({nome_cliente3}) ficará hospedado?  '))

if cliente1_quarto == 'Simples':
    valor_cliente1 = valor_simples*cliente1_dias
elif cliente1_quarto == 'Duplo':
    valor_cliente1 = valor_duplo*cliente1_dias
else:
    valor_cliente1 = valor_luxo*cliente1_dias

if cliente2_quarto == 'Simples':
    valor_cliente2 = valor_simples*cliente2_dias
elif cliente2_quarto == 'Duplo':
    valor_cliente2 = valor_duplo*cliente2_dias
else:
    valor_cliente2 = valor_luxo*cliente2_dias

if cliente3_quarto == 'Simples':
    valor_cliente3 = valor_simples*cliente3_dias
elif cliente3_quarto == 'Duplo':
    valor_cliente3 = valor_duplo*cliente3_dias
else:
    valor_cliente3 = valor_luxo*cliente3_dias

print(f'Cliente 1: {nome_cliente1}, {idade_cliente1} anos, Quarto {cliente1_quarto}, {cliente1_dias} dias')
print(f'Valor Total Cliente 1: R$ {valor_cliente1:.2f}')

print(f'Cliente 2: {nome_cliente2}, {idade_cliente2} anos, Quarto {cliente2_quarto}, {cliente2_dias} dias')
print(f'Valor Total Cliente 2: R$ {valor_cliente2:.2f}')

print(f'Cliente 3: {nome_cliente3}, {idade_cliente3} anos, Quarto {cliente3_quarto}, {cliente3_dias} dias')
print(f'Valor Total Cliente 3: R$ {valor_cliente3:.2f}')