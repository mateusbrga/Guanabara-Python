def terreno(larg, comp):
    t=larg*comp
    print(f'A área de um terreno {l}x{c} é de {t}m²')
    
#main
print('Controle de terrenos')
print('-'*30)
l=float(input('LARGURA (m): '))
c=float(input('COMPRIMENTO (m): '))
terreno(l, c)