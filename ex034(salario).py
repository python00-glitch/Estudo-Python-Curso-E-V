# Pergunte o salario #
# Caso o salario for superior a 1250.00, calcule 10% a mais para ele #
# Caso for igual ou abaixo de 1250.00, calcule 15% a mais # 
n1 = float(input("Digite o seu salário: R$"))

c1 = n1*1.1
c2 = n1*1.25
if n1>1250:
    print("Seu salário atual é de R${:.1f}".format(c1))
else:
    print("Seu salário atual é de R${:.1f}" .format(c2))
input("Pressione 'Enter' para finalizar...")