from Neuron import Neuron


class R(Neuron):
    def __init__(self,entries=None, weights=None,current_value=None):
        """Constructor"""
        super().__init__(entries,weights,current_value)
        self.weights=None

    # number - порядковый номер нейрона, такой же как индекс нейрона в списке у сети. Нужен для того, чтобы
    # получить соответствующий вес связи.
    def getValue(self,number):
        sum = 0
        for entry in self.entries:
            sum += entry.current_value * entry.weights[number]  # порог = 0
        self.current_value = sign(sum)
        return self.current_value


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    elif x == 0:
        return 0