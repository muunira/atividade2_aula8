nome = input('Digite seu nome: ')
senha = input('Digite sua senha: ')

produtos = ['Escova','Shampoo','Sabonete','Pasta de dente']
valores = [15.0,20.50,5.49,12.39]

carrinho = []
total = 0

if senha != 'Munirinha123':
    print('Senha inválida! Tente novamente.')

else:

    print('Acesso liberado.')

    print('Escolha o seu produto')

    produto1 = input(''' 
1. Escova - R$15.00
2. Shampoo - R$20.50
3. Sabonete - R$5.00
4. Pasta de dente - R$12.50
                     
Digite o número do produto: ''')

    if produto1 == '1':
        carrinho.append(produtos[0])
        total += valores[0]
    elif produto1 == '2':
        carrinho.append(produtos[1])
        total += valores[1]
    elif produto1 == '3':
        carrinho.append(produtos[2])
        total += valores[2]
    elif produto1 == '4':
        carrinho.append(produtos[3])
        total += valores[3]

    print(carrinho)
    print('R$',total)


    print('Deseja comprar mais alguma coisa?')
    saida = input('Sim/Não: ')

    if saida == 'Sim':

        produto2 = input(''' 
1. Escova - R$15.00
2. Shampoo - R$20.50
3. Sabonete - R$5.00
4. Pasta de dente - R$12.50
                         
Digite o número do produto: ''')

        if produto2 == '1':
            carrinho.append(produtos[0])
            total += valores[0]
        elif produto2 == '2':
            carrinho.append(produtos[1])
            total += valores[1]
        elif produto2 == '3':
            carrinho.append(produtos[2])
            total += valores[2]
        elif produto2 == '4':
            carrinho.append(produtos[3])
            total += valores[3]

        print(carrinho)
        print('R$',total)

        print('Deseja comprar mais alguma coisa?')
        saida = input('Sim/Não: ')

        if saida == 'Sim':

            produto3 = input(''' 
1. Escova - R$15.00
2. Shampoo - R$20.50
3. Sabonete - R$5.00
4. Pasta de dente - R$12.50
                                
Digite o número do produto: ''')

            if produto3 == '1':
                carrinho.append(produtos[0])
                total += valores[0]
            elif produto3 == '2':
                carrinho.append(produtos[1])
                total += valores[1]
            elif produto3 == '3':
                carrinho.append(produtos[2])
                total += valores[2]
            elif produto3 == '4':
                carrinho.append(produtos[3])
                total += valores[3]

            print(carrinho)
            print('R$',total)

            print('Compra finalizada automaticamente (máximo de 3 itens por carrinho).')
            pagamento = input('''Qual a forma de pagamento? 
Débito/Crédito: ''')
            if pagamento == 'Crédito' or 'Débito':
                print(f'''Total a pagar:
R${total:.2f}''')

            else:
                pagamento = input('''Qual a forma de pagamento? 
Débito/Crédito: ''')
            if pagamento == 'Crédito' or 'Débito':
                    print("\nVocê comprou:")
                    len(carrinho)
                    print(carrinho)

        else:
            pagamento = input('''Qual a forma de pagamento? 
Débito/Crédito: ''')
            if pagamento == 'Crédito' or 'Débito':
                print(f'''Total a pagar:
R${total:.2f}''')
                print("\nVocê comprou:")
                len(carrinho)
                print(carrinho)

    else:
        pagamento = input('''Qual a forma de pagamento? 
Débito/Crédito: ''')
        if pagamento == 'Crédito' or 'Débito':
            print(f'''Total a pagar:
R${total:.2f}''')
            print("\nVocê comprou:")
            len(carrinho)
            print(carrinho)