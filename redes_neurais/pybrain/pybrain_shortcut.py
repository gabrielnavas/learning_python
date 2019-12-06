from pybrain.tools.shortcuts import buildNetwork
# from pybrain.datasets import SupervisedDataSet
# from pybrain.supervised.trainers import BackpropTrainer
# from pybrain.structure.modules import SoftmaxLayer
# from pybrain.structure.modules import SigmoidLayer

rede = buildNetwork(2, 3, 1)
print(rede['in'])