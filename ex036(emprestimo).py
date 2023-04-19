

print("<Bem-vindo ao Consultor de Empréstimos Imoboliários Taxvá>")
print(58*"/")
c = float(input("Qual o valor do imóvel que voce deseja comprar: "))
s = float(input("Qual o seu salário mensal: "))
a = int(input("Em quanto tempo você deseja quitar o seu imóvel: "))

x = c / a
m = x / 12
y = s * 0.3

if y < m:
    print("Infelizmente, o banco \033[0;31mnão\033[m poderá realizar este empréstimo no momento. \nTente novamente com um imóvel de menor valor, ou com um tempo maior de quitabilidade.")
else:
    print("\033[;32mEmpréstimo validado!!\033[m \n\033[;34mPara o próximo passo, enviaremos um e-mail para o senhor com mais detalhes.\033[m")
