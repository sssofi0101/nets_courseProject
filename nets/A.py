from random import random, randint

from Neuron import Neuron


class A(Neuron):
    def __init__(self, entries=None, weights=[], current_value=None):
        """Constructor"""
        super().__init__(entries, weights, current_value)
        self.weights = []
        self.current_value = None
        for a in range(len(self.entries)):
            self.weights.append(randint(-1, 1))
    def getValue(self):
        sum = 0
        threshold = randint(0, 15)  # случайное число
        self.current_value = None
        for i in range(len(self.entries)):
            sum += self.entries[i].getValue() * self.weights[i]
        sum -= threshold
        self.current_value = sign(sum)
        return True #self.current_value
    # было: getValue -преактивация, current_value- постактивация


def sign(x):
    if x > 0:
        return 1
    elif x <= 0:
        return -1
    """elif x == 0:
        return 0"""
