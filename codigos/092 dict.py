from datetime import date
ano=date.today().year
c={}
c['nome']=str(input('Digite o nome: '))
ano_nasc=int(input('Digite o ano de nascimento: '))
c['idade']=ano - ano_nasc
c['ctps']=int(input('Digite a carteira de trabalho(0 = sem carteira): '))
if c['ctps']!=0:
    c['contratacao']=int(input('Digite o ano de contratação: '))
    c['salario']=float(input('Digite o salario: '))
    c['aposentatoria']=(c['contratacao']+35)- ano_nasc
    for a, b in c.items():
        print(f'{a} tem o valor {b}')
else:
    for e, d in c.items():
        print(f'{e} tem o valor {d}')
