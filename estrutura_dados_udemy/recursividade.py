# fibonati -------------------------------------

def fib(n):
    if (n == 1 or n == 2):
        return 1
    return fib(n - 1) + fib(n - 2)


fib_lb = lambda n: 1 if (n == 1 or n == 2) else fib(n - 1) + fib(n - 2)

def fib_iterativo(n):
    tot=0
    while(n > 1):
        tot += n+n-1
        n -= 1

    return tot

# print(fib_iterativo(6))
# print(fib(6))

def explosao_da_stack(N):
    cont=1
    try:
        while(cont < N):
            print("cont {}".format(cont))
            fib(cont)
            cont += 1
    except:
        return cont

# explosao = explosao_da_stack(500)
# print(explosao)


# exp -------------------------------------
"""
    base, exp
    base = 2
    exp=  10
    2 ** 10 = 1024
"""

def pot(base, exp):

    if(exp == 0):
        return 1
    return base * pot(base, exp-1)

print(pot(2, 10))


