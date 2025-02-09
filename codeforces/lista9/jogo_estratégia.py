
jogadores, rodadas = map(int, input().split())
pontos = list(map(int, input().split()))

pontuacao = [0] * jogadores

for i in range(len(pontos)):
    jogador = i % jogadores
    pontuacao[jogador] += pontos[i]

max_pontuacao = max(pontuacao)

vencedor = -1
for i in range(jogadores):
    if pontuacao[i] == max_pontuacao:
        vencedor = i + 1  

print(vencedor)
