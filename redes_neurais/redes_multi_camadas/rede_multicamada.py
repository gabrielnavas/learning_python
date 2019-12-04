import numpy as np

class Network:

    def __init__(self):
        self.entradas = None
        self.saidas = None
        self.valoresAprendizagem = None

    def setEntradas(self, entrada = np.array([])):
        self.entradas = entrada

    def setSaidas(self, saidas = np.array([])):
        self.saidas = saidas

    def setValoresParaAprendizagem(self, valores=np.array([])):
        self.valoresAprendizagem = valores

    def sigmoid(self, x):
        """
            :param x é a soma das entradas:
            :return calculo:
        """
        return 1 / (1+np.exp(-x))

    def hyperbolic(self, x):
        """
        :param x é a soma das entradas:
        :return calculo:
        """
        return (np.exp(x)-np.exp(-x)) / np.exp(x)+np.exp(-x)

# if __name__ == '__main__':
#     nw = Network()
#     nw.setEntradas([[0,0], [0.1], [1.0], [1.1]])
#     nw.setSaidas([])
#
#     # print(nw.sigmoid(0.99))
#     # print(nw.hyperbolic(-5))
#     # print(np.exp(-1))



# utilizar classes depois:

def sigmoid(self, x):
    """
        :param x é a soma das entradas:
        :return calculo:
    """
    return 1 / (1+np.exp(-x))

entradas = np.array([[0,0],
                     [0,1],
                     [1,0],
                     [1,1]])

saidas = np.array([[0], [1], [1], [0]])

#pesos direcao da camada oculta
pesos0 = np.array([[-0.424, -0.740, -0.961]],
                        [0.358, -0.577, -0.469])

#pesos direcao saida
pesos1 = np.array([[0.017], [-0.893], [0.148]])

# quantidade de rodas (atualizando os pesos).
epocas = 100

for j in range(epocas):
    #codigo aqui
    pass