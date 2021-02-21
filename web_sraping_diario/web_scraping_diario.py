import time
from requests_html import HTMLSession

starttime = time.time()

# Loop para obtenção dos dados
while True:
    print(time.strftime('%H:%M:%S', time.localtime()))

    # Definição da sessão para o web scraping
    url = 'https://br.investing.com/equities/magaz-luiza-on-nm-historical-data'

    session = HTMLSession()
    r = session.get(url).html
    data = r.find('#results_box', first=True).text.split()

    # Criação das listas para armazenar os dados
    dados_diario = []
    dados_tam = len(data)
    linha = []

    # Obtenção dos dados apenas na primeira linha da tabela
    i = 7
    while i < 14:
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

        dados_diario.append(linha)
        linha = []

    # Mostrar os dados obtidos
    print(dados_diario)

    # Define o tempo de espera para executar novamente(em segundos)
    time.sleep(300.0 - ((time.time() - starttime) % 60.0))

# Depois será adicionada a função para salvar os dados em um arquivo
