mediçoes = int(input())
list = []
for i in range(mediçoes):
    aferiçoes = int(input())
    list.append(aferiçoes)
soma = sum(list)
media = soma // mediçoes
print(media)

media_acima = media + (media * 10) // 100
print(media_acima)
media_abaixo = media - (media * 10) // 100
print(media_abaixo)


quantidade = 0
for i in range(0,len(list)):
    if list[i] > media_acima:
        quantidade = quantidade + 1
    else:
        if list[i] < media_abaixo:
            quantidade = quantidade + 1
print(quantidade)
