lista = [1, 2, 3, 4, 5, 6]


#
# for i in lista:
#     print(i)
#
# for i in range(0, len(lista)):
#     print(lista[i])
#

# 0 ate 5-1
#
# for i in range(0, 5):
#     print(lista[i])


#OBJETOS

class PrimeiraClasse():
    pass


class SegundaClasse:
    pass


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

class ListPerson:

    def __init__(self):
        self.listPerson= []

    def inserirDados(self):
        p1 = Person('Gabriel', 43)
        p2 = Person('Navas', 65)
        p3 = Person('Rafael', 45)
        p4 = Person('Ana', 63)
        p5 = Person('José', 81)

        self.listPerson.append(p1)
        self.listPerson.append(p2)
        self.listPerson.append(p3)
        self.listPerson.append(p4)
        self.listPerson.append(p5)


    def relatorioPessoas(self):
        for person in self.listPerson:
            print('Nome: %s' % person.getName())
            print('Idade: %d' % person.getAge(), end='')

            print('')


lpeople = ListPerson()
lpeople.inserirDados()
lpeople.relatorioPessoas()




# compressao
# inserir numeros dentro de uma lista com condições 0 até 10, com numeros impares
lista = [num for num in range(0, 50000) if (num % 2 != 0)]
print(lista)

