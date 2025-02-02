comprimento, distancia = map(int,input().split())
custo_km, valor_pedagio = map(int,input().split())
pedagios = comprimento // distancia
custo = custo_km * comprimento
preço_pedagio = pedagios * valor_pedagio
valor = custo + preço_pedagio
print(valor)
