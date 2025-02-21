jogadores, min_pontos = map(int,input().split())
passou = []

  for i in range(0,jogadores):
      pontos1, pontos2 = map(int,input().split())
      if pontos1 + pontos2 >= min_pontos:
          passou.append(1)    
print(sum(passou))
