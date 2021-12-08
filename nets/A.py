from random import random

from Neuron import Neuron


class A(Neuron):
    # number - порядковый номер нейрона, такой же как индекс нейрона в списке у сети. Нужен для того, чтобы
    # получить соответствующий вес связи.
    def getValue(self):
        sum = 0
        threshold = random.randint(0, 15)  # случайное число
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
