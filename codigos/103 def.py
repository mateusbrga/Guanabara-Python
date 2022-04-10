def jogo(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')
    
#main
n=input('Nome do jogador: ')
g=input('Numero de gols: ')
if g.isnumeric():
    g=int(g)
else:
    g=0
if n.strip()=='':
    jogo(gol=g)
else:
    jogo(n, g)