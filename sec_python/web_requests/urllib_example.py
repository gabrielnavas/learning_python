#python 2

import urllib2

url = 'http://solyd.com.br'
cabecalho = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'}

# gera a requisicao com a url e o user agent (cabecalho)
requisicao = urllib2.Request(url, headers=cabecalho)

# gera abre a url com esse tipo de requisicao
resposta = urllib2.urlopen(requisicao)

# le o html do site
html = resposta.read()


#exite o html
print(html)
