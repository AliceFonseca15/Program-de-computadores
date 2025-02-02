valor_100 = int(input())
t = valor_100 // 100
valor_50= valor_100 % 100
print(valor_100)
print(t,"nota(s) de R$ 100,00")
t2 = valor_50 // 50
valor_20 = valor_50 % 50
print(t2,"nota(s) de R$ 50,00")
t3 = valor_20 // 20
valor_10 = valor_20 % 20
print(t3,"nota(s) de R$ 20,00")
t4 = valor_10 // 10
valor_5 = valor_10 % 10
print(t4,"nota(s) de R$ 10,00")
t5 = valor_5 // 5 
valor_2 = valor_5 % 5
print(t5,"nota(s) de R$ 5,00")
t6 = valor_2 // 2
valor_1 = valor_2 % 2
print(t6,"nota(s) de R$ 2,00")
t7 = valor_1 // 1
print(t7,"nota(s) de R$ 1,00")