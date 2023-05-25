# Analise de Dados
import pandas as pd

# Usa-se a bibilioteca 'pandas' para manejar dados com python

# Para ler um arquivo, usamos o 'pandas.read_{}()', onde as chaves sao o tipo de arquivo que vai ser lido
# Dentro das aspas, colocamos o caminho do arquivo no gerenciador de arquivos para o pandas ler
# 'r' (raw) é para o python ler o caminho sem que nenhum caractere especial com '\' atrapalhe a leitura
# '.sep' é um separador, que usa para separar o texto da tabela e mante-la organizada no terminal
tabela = pd.read_csv(r"C:\Users\rosel\OneDrive\Documentos\Estudos Intensivão Python\Compras.csv", sep=";")
# Para deletar uma COLUNA (column) ou uma LINHA (row), usa-se '{} = {}.drop()'
    # Obs.: {} é o novo nome da variável que usará para a nova tabela alterada, e a outras {} é o nome da variavel
    # com a tabela anterior.
        # exemplo:
#tabela = tabela.drop()
# Para escolher qual coluna ou linha deverá ser deletada, usamos nas condiçoes o nome de um elemento que esta em um dos
    # eixos, e coloca-lo entre aspas, e depois com o PARÂMETRO 'axis=0' para o eixo das LINHAS, ou 'axis=1' para o eixo das COLUNAS
        # exemplo:
#tabela = tabela.drop("ValorFinal", axis=1)

print(tabela)

#             Codigo    Data                Valor     ValorFinal
#             Compra             ...        Unitario
#0            65014  01/12/2023  ...        259.00    1295.00
#1            65014  01/12/2023  ...        380.00     380.00
#2            65016  01/12/2023  ...        479.00     958.00
#3            65016  01/12/2023  ...         18.90      18.90
#4            65017  01/12/2023  ...        159.90     479.70
#...            ...         ...  ...           ...        ...
#4538         69996  26/12/2023  ...         10.00      20.00
#4539         69996  26/12/2023  ...        156.40     625.60
#4540         69996  26/12/2023  ...        183.89     183.89
#4541         69997  26/12/2023  ...        359.91     359.91
#4542         69997  26/12/2023  ...        502.55    1005.10