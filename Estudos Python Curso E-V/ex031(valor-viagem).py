# Desenvolva um software que calcule o preço da viagem por KM RODADO #
# Para viagens até 200 km, se cobra 0,50 para cada km #
# Acima de 200 km, se cobra 0,45 #
print("Viaje conosco na Lange's Viagens! Calcule aqui sua viagem.")
v = float(input("Quantos kilômetros dá a sua viagem: "))
if v <= 200:
    c1 = v*0.5
    print("A sua viagem dará o total de R${:.1f}" .format(c1))
if v > 200:
    c2 = v*0.45
    print("A sua viagem dará o total de R${:.1f}" .format(c2))
input("Pressione 'Enter' para continuar...")
