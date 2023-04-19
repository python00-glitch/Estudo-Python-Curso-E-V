nome = str.upper(input("Digite seu nome: "))
sob_nome = str.upper(input("Digite seu sobrenome: "))
if nome == "RICARDO" and sob_nome == "PARDIM" or nome == "GIULIA" and sob_nome == "GABRIELLE":
    print("\033[1;32mACESSO AUTORIZADO PARA {} {}\033[m".format(nome, sob_nome))
elif nome == "RICARDO" and sob_nome == "NAZARENO" or nome == "ROSELI" and sob_nome == "PARDIM" or nome == "RAYSSA" and sob_nome == "PARDIM":
    print("\033[1;31mACESSO NÃO PERMITIDO. \nPROPRIETÁRIOS FORA DE CASA NO MOMENTO.\033[m")
elif nome in "REGINALDO BRUNA LENA VANDA DAVI LULU LUIZ JULIA LAURA BRUNO MARIA VANESSA KIMBERLY IVAN":
    print("\033[1;31mACESSO NÃO PERMITIDO PARA {} {}. \nCONTATAR JÚNIOR PARA INFORMAÇÕES\033[m" .format(nome, sob_nome))
else:
    print("\033[1;31mACESSO NEGADO. CONTATAR PROPRIETÁRIO.\033[m")