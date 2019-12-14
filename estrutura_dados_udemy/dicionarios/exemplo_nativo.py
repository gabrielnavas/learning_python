


dic = {}


# insert in dict

dic['gabriel'] = 22
dic['navas'] = 32
dic['rafael'] = 44
dic['joaquim'] = 99
dic['ana'] = 44

# delete in dict

del dic['gabriel']
del dic['ana']

if 'gabriel' not in dic.keys():
    print("não existe a chave 'gabriel' no dicionário")

# show all dict

for key in dic.keys():
    print(dic[key])
