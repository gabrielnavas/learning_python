import array

def main():

    arr1 = array.array('i', [1,2,3,4,5])

    for i in arr1:
        print(i, sep=', ', end='')

    print("\n\nindex {} => {}".format(2, arr1.index(2)))

if __name__ == '__main__':
    main()