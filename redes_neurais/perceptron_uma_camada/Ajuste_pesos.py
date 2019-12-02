import numpy as np

entrada = np.array([[0, 0], [0,1], [1,0], [1,1]])
pesos = np.array([[0, 0], [0, 0], [0,0], [0,0]])
resultado = np.array([0,0,0,1])
TAXA_APRENDIZAGEM = 0.1

def calc_erro(respostaCorreta, respostaCalculada, pesoAtual, entradaAtual):
    erro = respostaCorreta - respostaCalculada
    novo_peso = pesoAtual + (TAXA_APRENDIZAGEM * entradaAtual * erro)

    return novo_peso

def aprender_no(entrada, peso, resultado, result_calc):

    novo_peso = calc_erro(resultado, result_calc, pesos, entrada)
    peso = novo_peso

def aprender(entrada, pesos, resultado):

    for i in range(4):
        print(entrada[i])
        print(pesos[i])
        print(resultado[i])

        soma = somar(entrada, pesos[i])
        result_calc = stepFun(soma)

        aprender_no(entrada[i], pesos[i], resultado[i], result_calc)

def stepFun(x):
    return 1 if x >= 1 else 0

def somar(e, p):
    return e.dot(p)

aprender(entrada, pesos, resultado)

print(entrada)
print(pesos)