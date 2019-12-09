class Stack:
    def __init__(self):
        self.stack = []
        self.len = 0

    def push(self, e):
        self.stack.append(e)
        self.len += 1

    def pop(self):
        self.stack.pop()
        self.len -= 1

    def top(self):
        return self.stack[-1]

    def empty(self):
        return self.len == 0


def check_parenteses(str):
    stk = Stack()

    for ch in str:
        if ch == '(':
            stk.push(ch)
        elif ch == ')':
            if not stk.empty() and stk.top() == '(':
                stk.pop()
            else:
                stk.push(ch)

    return stk.empty()


str = input()
while len(str) > 0:

    if (check_parenteses(str) == True):
        print('correct')
    else:
        print('incorrect')

    str = input()
