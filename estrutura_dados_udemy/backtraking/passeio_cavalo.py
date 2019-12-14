N = 8
Nmax = N*N

def posicoes(x, y, index):
    pos = [(x+2, y+1), (x+1, y+2),
          (x-1, y+2), (x-2, y+1),
          (x-2, y-1), (x-1, y-2),
          (x+1, y-2), (x+2, y-1)]
    pos = pos[index]
    x = pos[0]
    y = pos[1]
    return x, y

def is_possivel(matrix: [], x, y):
    return 0 <= x and x < N and  0 <= y and y < N and not matrix[x][y]

def show(matrix):
    for l in matrix:
        for i in l:
            print('{}, '.format(i), end='')
        print()
    print('{:2}'.format('-' * (Nmax + 5)))


def execute_run(matrix=[], x=0, y=0, cont=1):

    if cont == Nmax:
        return True
    else:
        for i in range(8):
            posX, posY = posicoes(x, y, i)

            if is_possivel(matrix, posX, posY):
                matrix[posX][posY] = cont

                if execute_run(matrix, posX, posY, cont+1):
                    return True
                else:
                    matrix[posX][posY] = 0
    return False

def create_matrix():
    matrix = [[] for i in range(N)]
    for i in range(N):
        matrix[i] = [0 for i in range(N)]
    return matrix

def main():

    # create matrix
    matrix = create_matrix()

    show(matrix)

    possivel = execute_run(matrix=matrix, x=3, y=4, cont=1)

    if possivel :
        show(matrix)
    else:
        print("Não é possível com esse 'x' e 'y'")

if __name__ == '__main__':
    main()