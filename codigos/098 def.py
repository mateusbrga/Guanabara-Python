from time import sleep

def contador(i, f, p=0):
    print(f'Contagem de {i} a {f} de {p} em {p}.')
    sleep(2)
    if p<0:
        p*=-1
    if p==0:
        p=1
    
    if f>i:
        for cont in range(i,f+1,p):
            print(f'{cont}', end=' ')
            sleep(0.5)
        print('FIM!')
    elif i>f:
        for cont in range(i,f-1,p*-1):
            print(f'{cont}', end=' ')
            sleep(0.5)
        print('FIM!')
        
#main
contador(1,10,1)
contador(10,0,2)
print('Agora é sua hora de contar!')
ini=int(input('Digite o inicio da contagem: '))
fim=int(input('O fim: '))
pas=int(input('Por fim o passo: '))
contador(ini, fim, pas)