total=0
f={}
f['nome']=str(input('Digite o nome do jogador: '))
qtd_p=int(input(f'quantas partidas {f["nome"]} jogou? '))
g=[]
for c in range(qtd_p):
    g.append(int(input(f'Na partida {c+1} fez quantos gols? ')))
    total+=g[c]
print('-='*30)
f['gols']=g
f['total']=total
for a, b in f.items():
    print(f'No campo {a} tem o valor {b}')
print('-='*30)
print(f'O jogador {f["nome"]} jogou {qtd_p} partidas.')
for j in range(qtd_p):
    print(f' => Na partida {j+1} fez {g[j]} gols.')
print(f'Foi um total de {f["total"]} gols.')