from random import random, randint, seed

from Neuron import Neuron


class A(Neuron):
    """
    Класс А-нейрона.
    """
    def __init__(self, entries=None, weights=[], current_value=None):
        """
        Конструктор. Инициализирует экземпляр класса A с current_value = None, случайными весами -1, 0 или 1,
        задает случайный порог
        :param entries: Список входных нейронов. В данном случае список всех S-нейронов.
        :param weights: Список весов связей S-A этого нейрона.
        :param current_value: Текущее значение A-нейрона.
        """
        super().__init__(entries, weights, current_value)
        self.weights = []
        self.current_value = None
        for a in range(len(self.entries)):
            self.weights.append(randint(-1, 1))
        self.threshold = randint(0, 15)

    def getValue(self):
        """
        Метод "Получить значение". Вычисляет текущее значение A-нейрона с помощью пороговой функции активации
        и алгебраической суммы произведений весов и значений S-нейронов.
        :return: Новое значение поля current_value A-нейрона.
        """
        sum = 0
        self.current_value = None
        for i in range(len(self.entries)):
            sum += self.entries[i].getValue() * self.weights[i]
        sum -= self.threshold
        self.current_value = sign(sum)


def sign(x):
    if x > 0:
        return 1
    elif x <= 0:
        return -1