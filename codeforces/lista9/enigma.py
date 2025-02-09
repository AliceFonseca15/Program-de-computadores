def contar_posicoes(mensagem, crib):
    msg = len(mensagem)
    crip = len(crib)
    contador = 0

    for i in range(msg - crip + 1):
        valido = True
        for x in range(crip):
            if mensagem[i + x] == crib[x]:
                valido = False
                break
        if valido:
            contador += 1

    return contador


mensagem_codigo = input()
crib = input()

resultado = contar_posicoes(mensagem_codigo, crib)

print(resultado)