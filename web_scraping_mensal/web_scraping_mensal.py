from requests_html import HTMLSession

# Definição da sessão para o web scraping
url = 'https://br.investing.com/equities/magaz-luiza-on-nm-historical-data'

session = HTMLSession()
r = session.get(url).html
data = r.find('#results_box', first=True).text.split()

# Criação das listas para armazenar os dados
dados_historicos = []
dados_tam = len(data)
linha = []

# Obtenção dos dados diários no prazo de um mês
i = 0
# Definição da quantidade de linhas da tabela,
# sendo cada linha um dia útil do mês, nesse caso foi definido 20 dias.
# Depois o valor é multiplicado pelo número de colunas na tabela, nesse caso 7.
dias_uteis = 20
dias_uteis = dias_uteis * 7
while i < dados_tam:
    if i <= dias_uteis:
        Data_dh = data[i]
        linha.append(Data_dh)
        i = i + 1

        Abertura = data[i]
        linha.append(Abertura)
        i = i + 1

        Fechamento = data[i]
        linha.append(Fechamento)
        i = i + 1

        Maxima = data[i]
        linha.append(Maxima)
        i = i + 1

        Minima = data[i]
        linha.append(Minima)
        i = i + 1

        Volume = data[i]
        linha.append(Volume)
        i = i + 1

        Var = data[i]
        linha.append(Var)
        i = i + 1

        dados_historicos.append(linha)
        linha = []
    else:
        break

# Mostrar os dados obtidos
for dia in dados_historicos:
    print(dia)

# Depois será adicionada a função para salvar os dados em um arquivo
