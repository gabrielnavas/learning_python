f_index = lambda x, y: x % y

mount_list = lambda max_list: [[] for _ in range(max_list)]

def main():
    qntd_tests = int(input())

    while qntd_tests > 0:

        enderecos, chaves = input().rsplit(' ')
        enderecos = int(enderecos)
        #chaves = int(chaves)

        ll = mount_list(enderecos)
        nums = input().rsplit(' ')

        for num in nums:
            num = int(num)
            index = f_index(num, enderecos)
            ll[index].append(num)

        #show lista of list
        i=0
        for l in ll:
            print('{} ->'.format(i), end=' ')
            for num in l:
                print('{} ->'.format(num), end=' ')
            print('/')
            i += 1

        qntd_tests -= 1

        if(qntd_tests > 0):
            print()


main()