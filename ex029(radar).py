radar = float(input("Digite a velocidade registrada (Use ponto '.' ao invés de vírgula ','): "))
if radar >= 81:
    print("Velocidade registrada está acima do limite permitido da via.")
    m = radar - 80
    v = m * 7
    print("Multa a pagar:{:.1f}" .format(v))
else:
    print("Velocidade registrada está no limite permitido da via.")

#Colocar {:.1} dentro da interprete da 'variável' que vai no 'print' corta todos os numeros decimais que vem logo após #
#como exemplo: {:.1} = 201.9 // {} = 201,96767676767.. #