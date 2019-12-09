# 	Runtime error =(

arvs = {}

n = int(input())
branco = input()

while n > 0: 
    arvs_count = 0

    #pega arvores
    flag=True
    while flag:
        especie = input()

        if len(especie) == 0:
            flag=False            
        else:
            if especie in arvs:
                arvs[especie] += 1
            else:
                arvs[especie] = 1
            arvs_count += 1    

    #sort por nome do dic   
    arvs = dict(sorted(arvs.items()))

    #soma por valores            
    sum_tot = sum(arvs.values())

    # porcentagem          
    for chave in arvs:
        print('{} {:.4f}'.format(chave, (arvs[chave]*100)/arvs_count))

    if n > 1:
        print()
    
    n -= 1
    arvs.clear()
