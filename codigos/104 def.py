def leiaInt(n):
    while True:
        n=input('Digite um numero: ')
        if n.isnumeric():
            n=int(n)
            return n
            break
        else:
            print('ERRO! Digite um numero inteiro válido.')

#main
n=leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')