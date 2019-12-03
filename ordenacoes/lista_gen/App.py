from ordenacoes.lista_gen.ListGen import ListGen

if __name__ == '__main__':
    lg = ListGen()

    str = "[aa, [bb,cc], [dd,[ee], ff,gg], hh]"

    lg.insertStr(str)
    lg.showString()


"""
[aa, [bb,cc], [dd,[ee], ff,gg], hh]
[aa, [bb,cc], hh]
[aa, [bb]]
[[dd, [ee],ff, []], [hh]]
[aa, [[bb]], [[[dd,lll]]]]
[aaaaaaaaaaaaa,ccccccccccccc,[a],[dd,[dd],[aa]]]
[[[[cc]]]]
[[[]]]

"""