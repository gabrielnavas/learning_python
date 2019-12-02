# python2

import requests

url = 'https://bv4.digitalpages.com.br/'

#meu cabelho, simulando um navegador
cabecalho = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'}




#gerar resposta
resposta = requests.get(url, headers=cabecalho)


# codigo fonte do frontend
print(resposta.text)

# cookies
#print(resposta.cookies)

# cabecalhos
#print(resposta.headers)

