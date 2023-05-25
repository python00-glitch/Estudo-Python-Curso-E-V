# Faça um programa que leia 3 numeros e diga qual deles é o maior e qual o menor #
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite mais um numero: "))

if n1 > n2 and n1 > n3:
    print("{} é o numero maior." .format(n1))
if n2 > n3 and n2 > n1: 
    print("{} é o numero maior." .format(n2))
else:
    print("{} é o numero maior" .format(n3))
