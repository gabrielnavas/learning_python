# tamanhos
tamanho_str = len("gabriel")

lista = [1, 2, 3, 4, 5]
tamanho_lista = len(lista)

print(tamanho_str)
print(lista)

# fores
dic = {'mascos': 28, 'joao': 45, 'maria': 54}

for chave in dic:
    print(dic[chave])

# condição ternária
num = 10
saida = 'par' if (num % 2 == 0) else 'impar'
print("{} é {}".format(num, saida))

# condição
if num % 2 == 0:
    print('par')
else:
    print('impar')

#funcoes
def sou_uma_funcao(param1, param2, param3):
    print(param1)
    print(param2)
    print(param3)

def isPar(num):

    if num % 2 == 0:
        return True
    return False

print("11 é par? {}".format(isPar(11)))

try:
    sou_uma_funcao(1,2)
except Exception as ex:
    print(type(ex))