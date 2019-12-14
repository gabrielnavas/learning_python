import random
import time

lista = [1, 'a', []]
# print(lista)
# for i in range(len(lista)):
#     print(lista[i])


lista2 = [4, 5, 'gabriel']

#concatenar listas

lista3 = lista + lista2

#
# print("tamanho agora {}".format(len(lista3)))


#deletei um elemento
# del lista3[0]

#tamanho agora
# print("tamanho agora {}".format(len(lista3)))
#
# print("Concatenei lista com lista2")
# for elem in lista3:
#     print("cont: {}".format(elem))

lista3.pop(0) #remove por posicao

print(lista3)

lista3.insert(0, 1)
print(lista3)

lista3.append((562))
print(lista3)



# lista3.remove(562) #remove por elemento

def search_sentinel(elem, lista: []):
    lista.append(elem)

    i=0
    while(elem != lista[i]):
        i += 1

    if(i < len(lista)-1):
        lista.pop(len(lista)-1)
        return i

    lista.pop(len(lista) - 1)
    return -1

pos = search_sentinel(562, lista3)

if(pos != -1):
    print(pos)
    lista3.pop(pos)
    print(lista3)
else:
    print("elemento nao existe.")


# ordenar
lista4 = [i for i in range(10000)]



random.shuffle(lista4)

lista4.sort()

print(lista4)

# [1, 'a', [], 4, 5, 'gabriel']
print(lista3[1:-2]) # ['a', [], 4]

print(lista3[::-1]) # inverter

print(lista3[-2])