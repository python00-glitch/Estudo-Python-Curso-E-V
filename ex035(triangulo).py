# Faça um software que calcule o tamanho de 3 retas e diga se pode formar um triangulo perfeito #
# Dica: Principio Matemático #
r1 = int(input("Digite o tamanho da reta 1: "))
r2 = int(input("Digite o tamanho da reta 2: "))
r3 = int(input("Digite o tamanho da base: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Este triângulo está perfeito.")
else:
    print("Não é possivel completar este triângulo...")
input("Digite Enter para finalizar...")