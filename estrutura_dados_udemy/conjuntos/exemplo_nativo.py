
# exemplos de formação

c1 = {1, 2, 3, 4.44}
c2 = {'gabirel', 'navas', 'joão'}
c3 = {1, 'gabriel', 4.44, 2}
c4 = set([1,2,3])
c5 = {1, 2, 3, 4}
c6 = {3, 4, 5, 6}

# exibição

for elem in c1:
    print(elem)

# operações

print(c5 | c6) # uniao (união dos dois conjuntos, sem se repitir)
print(c5 & c6) # intersecção (somente os elementos que estão nos dois conjuntos)
print(c6 - c5) # diferença (estão num conjunto mas não está no outro)


# remover
len()

c1.remove(1)
c1.pop()
for elem in c1:
    print(elem)
