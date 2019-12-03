matriz = [
    ['gabriel', 1, 2, 3],
    ['navas', 3, 2, 1],
    ['joao', 9, 8, 6]
]

for l in matriz:
    for c in l:
        print(str(c) + '\t',end='')
    print()