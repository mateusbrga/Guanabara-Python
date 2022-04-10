g={}
l=[]
idade=0
f=[]
while True:
    g['nome']=str(input('digite o nome: '))
    g['idade']=int(input('digite a idade: '))
    g['sexo']=str(input('digite o sexo [M/F]: ')).upper()
    if g['sexo'] == 'F':
        f.append(g['nome'])
    idade+=g['idade']
    
    conti=str(input('Quer continuar? [S/N] ')).upper()
    l.append(g.copy())
    media=idade/len(l)  
    if conti!='S':
        break
        
print('-='*30)
print(f'O grupo tem {len(l)} pessoas.')
print(f'A media de idade é de {media:.2f} anos')
print(f'Mulheres do grupo: {f}')
for i in range(len(l)):
    if l[i]['idade']>media:
        print(l[i])
        