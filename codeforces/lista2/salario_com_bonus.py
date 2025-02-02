nome = input()
nome1 = nome.capitalize()
salario = float(input())
vendas = float(input())
bonus = (vendas * 15) / 100
total = salario + bonus
print(nome1)
tol = "{:.2f}".format(total)
print("R$", tol)
