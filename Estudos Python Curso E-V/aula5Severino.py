#num = 0
#while num < 101:
#    num += 2
#    if num % 3:
#        print(num)
soma = 0
for n in range(3):
    adic = int(input("Digite um numero para adicionar na soma: "))
    soma += adic
print("Total dá: {}".format(soma))