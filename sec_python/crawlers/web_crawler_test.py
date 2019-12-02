import re

str = 'nome_usuario@gmail.com'

padrao = re.search(r'\w@\w.\w', str)

if(padrao):
    print(padrao.group()) 
else:
    print('not found')    