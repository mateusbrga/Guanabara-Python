def voto(ano_nasc):
    from datetime import date
    ano=date.today().year
    idade=ano-ano_nasc
    if idade<18:
        return'NEGADO'
    elif idade>18 and idade<65:
        return 'OBRIGATORIO'
    else:
        return 'OPCIONAL'
#main
ano_nasc=int(input('Em que ano voce nasceu? '))
tipo_voto = voto(ano_nasc)
print(f'Com o voto é: {tipo_voto}')