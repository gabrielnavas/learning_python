
# potenciação

# com função normal
def pot2(x):
    return x ** 2

#funcional
pot2_lamb = lambda x: x**2
# print(pot2_lamb(4))



# fatorial

# com função
def fat_real(num):

    x1=num
    x=num-1
    while x > 1:
        x1 = x1*x
        x = x-1

    return x1

def fat_rec(x):
    if(x == 0):
        return 1
    return (x * fat_rec(x-1))

# print(fat_real(4))
# print(fat_rec(4))

# funcional
fat_lb = lambda x: 1 if x == 0 else x*fat_rec(x-1)
# print(fat_lb(4))


# map ------------- :)
# aplicado uma funcao sobre cada elemento
lista = [1,2,3]
new_lista = map(lambda x: x+1, lista)

# print("resultado da nova lista")
# for num in new_lista:
#     print(num)




# reduce ------------- :)
# aplica uma funcao sobre uma sequencia sobre e vai acumulando o valor de retorno da funcao apartir de um valor inicial

import functools as ft

lista = [3,2,1]

acumulo = ft.reduce(lambda x, y: x+y, lista)

# print("acumulo do reduce: {}".format(acumulo))




# filter  ------------- :)
# elementos que respondem ao uma determinada condição

lista = [1,3,4,6,7,9, 12]

new_lista = filter(lambda x: x % 2 == 0, lista)

for i in new_lista:
    print(i)