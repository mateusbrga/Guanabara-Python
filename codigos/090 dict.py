a={}
a['nome']=input('Digite o nome do aluno: ')
a['media']=float(input('Digite a media do aluno: '))
print(f'Nome é igual a {a["nome"]}')
print(f'Media é igual a {a["media"]}')
if a["media"]>=7:
    print('Situacao é aprovado')
elif a['media'] <7 and a['media']>=5:
    print('Situacao é recuperacao')
else:
    print('Situacao é reprovado')
