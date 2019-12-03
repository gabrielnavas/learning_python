from ordenacoes.lista_gen.NoGen import NoGen


class Info(NoGen):

    def __init__(self):
        self._info=""

    def __init__(self, info):
        self._info = info


    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, info):
        self._info = info
