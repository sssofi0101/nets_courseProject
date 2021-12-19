from Neuron import Neuron


class R(Neuron):
    def __init__(self, entries=None, weights=[], current_value=None):
        """Constructor"""
        super().__init__(entries, weights, current_value)
        self.weights = []
        self.current_value = None
        for a in range(len(self.entries)):
            self.weights.append(0)

    # number - порядковый номер нейрона, такой же как индекс нейрона в списке у сети. Нужен для того, чтобы
    # получить соответствующий вес связи.
    def getValue(self):
        sum = 0
        self.current_value = None
        for i in range(len(self.entries)):
            sum += self.entries[i].current_value * self.weights[i]  # порог = 0
        self.current_value = sign(sum)
        #return self.current_value
        return True


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    elif x == 0:
        return 0