# Faça um programa que leia qual o sexo do usuario, e caso erre digitando, apareça um erro, e o usuario deve repetir

sexo = str.upper((input("Digite o seu sexo, por favor [M/F]: ")))
while sexo not in ['M', 'F']:
    print("\x1b[38;5;9mDado inválido!\x1b[m")
    sexo = str.upper((input("Digite o seu sexo, por favor [M/F]: ")))
print("\x1b[38;5;36mDado salvo com sucesso!\x1b[m")