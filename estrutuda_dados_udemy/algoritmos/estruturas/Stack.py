class Stack: #Stack

    def __init__(self):
        self.stack = []
        self.len_stack=0

    def push(self, elem):
        self.stack.append(elem)
        self.len_stack += 1

    def pop(self):
        elem = self.stack[self.len_stack-1]
        self.stack.pop(self.len_stack-1)
        self.len_stack -= 1

        return elem

    def empty(self):
        return self.len_stack == 0

    def top(self):
        return self.stack[-1]

    def len(self):
        return self.len_stack


# if __name__ == '__main__':
#     #test
#
#     stk = Stack()
#
#     for i in range(10):
#         stk.push(i)
#
#     print("tamanho: {}".format(stk.len()))
#     print("top: {}".format(stk.top()))
#
#     i=0
#     while(not stk.empty()):
#         e = stk.pop()
#         print(e)

