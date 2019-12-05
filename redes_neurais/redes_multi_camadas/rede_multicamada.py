import numpy as np


class Network:
    entradas = np.array([[0, 0],
                         [0, 1],
                         [1, 0],
                         [1, 1]])

    saidas = np.array([[0], [1], [1], [0]])

    # pesos direcao da camada oculta
    pesos0 = np.array([[-0.424, -0.740, -0.961],
                       [0.358, -0.577, -0.469]])

    # pesos direcao saida
    pesos1 = np.array([[0.017], [-0.893], [0.148]])

    # quantidade de rodas (atualizando os pesos).
    epocas = 100


    def __init__(self):
        self.entradas = None
        self.saidas = None
        self.valoresAprendizagem = None

    def init_process(self):
        for j in range(epocas):
            # calculo da entrada com camada oculta
            camadaEntrada = entradas
            somaSinapse0 = np.dot(camadaEntrada, pesos0)
            camadaOculta = sigmoid(somaSinapse0)

            # calculo camada oculta com a saida
            somaSinapse1 = np.dot(camadaOculta, pesos1)
            camadaSaida = sigmoid(somaSinapse1)

            # calculo do erro e saida final
            erroCamadaSaida = saidas - camadaSaida
            mediaSaidaAbsoluta = np.mean(np.abs(erroCamadaSaida))

            # pergunta sobre o erro

            # atualiza pesos

    def setEntradas(self, entrada=np.array([])):
        self.entradas = entrada

    def setSaidas(self, saidas=np.array([])):
        self.saidas = saidas

    def setValoresParaAprendizagem(self, valores=np.array([])):
        self.valoresAprendizagem = valores

    def sigmoid(self, x):
        """
            :param x é a soma das entradas:
            :return calculo:
        """
        return 1 / (1 + np.exp(-x))

    def hyperbolic(self, x):
        """
        :param x é a soma das entradas:
        :return calculo para valores negativos:
        """
        return (np.exp(x) - np.exp(-x)) / np.exp(x) + np.exp(-x)


# if __name__ == '__main__':
#     nw = Network()
#     nw.setEntradas([[0,0], [0.1], [1.0], [1.1]])
#     nw.setSaidas([])
#
#     # print(nw.sigmoid(0.99))
#     # print(nw.hyperbolic(-5))
#     # print(np.exp(-1))

# ---------------------------------------------------------------------------------------

# utilizar classes depois:

def sigmoid(soma):
    """
        :param x é a soma das entradas:
        :return calculo:
    """
    return 1 / (1 + np.exp(-soma))

def sigmoidDerivada(sig):
    return sig * (1 - sig)

def delta(erro,  sigmoidDerivada):
    return erro * sigmoidDerivada


entradas = np.array([[0, 0],
                     [0, 1],
                     [1, 0],
                     [1, 1]])

saidas = np.array([[0], [1], [1], [0]])

# pesos direcao da camada oculta
pesos0 = np.array([[-0.424, -0.740, -0.961],
                   [0.358, -0.577, -0.469]])

# pesos direcao saida
pesos1 = np.array([[0.017], [-0.893], [0.148]])

# quantidade de rodas (atualizando os pesos).
epocas = 100

for j in range(epocas):
    # calculo da entrada com camada oculta
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada, pesos0)
    camadaOculta = sigmoid(somaSinapse0)

    # calculo camada oculta com a saida
    somaSinapse1 = np.dot(camadaOculta, pesos1)
    camadaSaida = sigmoid(somaSinapse1)

    # calculo do erro e saida final
    erroCamadaSaida = saidas - camadaSaida
    mediaSaidaAbsoluta = np.mean(np.abs(erroCamadaSaida))

    # pergunta sobre o erro

    # atualiza pesos
