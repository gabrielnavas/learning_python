import sys

class ListLinkedOrd:

    class No:
        def __init__(self, elem=None, next = None):
            self.elem = elem
            self.next = next

        def get_str(self):
            return '{address} => elem:{elem}, next:{nextValue}'\
                .format(address=self.__repr__(),
                        elem=self.elem,
                        nextValue=self.next.elem\
                            if self.next is not None\
                            else 'None')


    def __init__(self):
        self._starter = None
        self._len = 0

    def insert(self, e):

        new_no = ListLinkedOrd.No(e, None)
        prev = None
        no = self._starter

        while no is not None:
            prev = no
            no = no.next

        if prev is None:
            self._starter = new_no
        else:
            if no is None:
                prev.next = new_no
            else:
                new_no.next = no
                prev.next = new_no
        self._len += 1

    def getNoIndex(self, index):
        no = self._starter
        while no is not None and index > 0:
            no = no.next
            index -= 1

        return no

    def show(self):

        no = self._starter
        while no is not None:
            print(no.get_str())
            no = no.next

    def __iter__(self):
        curr_no = self._starter
        while curr_no is not None:
            yield curr_no
            curr_no = curr_no.next

class HashTable:

    def __init__(self, table_size=101):
        if table_size < 1:
            print('Error: le size must be greater than 1.')
            sys.exit(1)

        self._table_size = table_size
        self._table = [ListLinkedOrd() for _ in range(table_size)]

    def get_table(self):
        return self._table

    def _hash_func(self, key):
        return key % self._table_size

    def insert(self, key):
        index = self._hash_func(key)
        linked_list: ListLinkedOrd = self._table[index]
        linked_list.insert(key)

    def remove(self, key):
        linked_list: ListLinkedOrd = self._table[self._hash_func(key)]
        if linked_list is not None:
            noLinked = linked_list.getNoIndex(key)
            return noLinked.elem
        return None

    def show(self):

        cont=0
        for linked_list in self._table:
            print('{} -> '.format(cont), end='')
            for no in linked_list:
                print('{} -> '.format(no.elem), end='')
            print('/')

    def search(self, key):
        linked_list:[] = self._table[self._hash_func(key)]

        i=0
        while i < len and key > linked_list[i]:
            i += 1

        if i < len and key == linked_list[i] == key:
            return key, True
        return None, False



if __name__ == '__main__':
    ht = HashTable(15)

    for i in range(1, 500, (2*3) ** 2):
        ht.insert(i)

    ht.show()