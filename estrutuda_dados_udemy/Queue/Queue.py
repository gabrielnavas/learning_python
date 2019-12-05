class No:

    def __init__(self):
        self.elem = None
        self.next = None

class Queue:

    def __init__(self):
        self.starter = None
        self.end = None
        self.length = 0

    def enqueue(self, elem):

        newNo = No()
        newNo.elem = elem
        newNo.next = None

        if(self.end == None):
            self.starter = newNo
            self.end = newNo
        else:
            self.end.next = newNo
            self.end = newNo

        self.length += 1

    def dequeue(self):

        no = self.starter.elem

        if(self.starter == self.end):
            self.starter  = None
            self.end = None
        else:
            self.starter = self.starter.next
        self.length -= 1

        return no

    def front(self):
        return self.starter

    def back(self):
        return self.end

    def empty(self):
        return self.length == 0

if __name__ == '__main__':
    q = Queue()

    for i in range(20, 51):
        q.enqueue(i)

    while(not q.empty()):
        print(q.dequeue())