# Faça um programa que leia a quantidade de algarismos que o usuario queira ver da Sequencia de Fibonacci

print("Bem vindo á exposição da Sequencia de Fibonacci")
num = int(input("Escreva a quantidade de algarismos que voce deseja ver na Sequencia: "))
n = (num - 1) + (num - 2)
for i in range(num):
    print(n, end='→')