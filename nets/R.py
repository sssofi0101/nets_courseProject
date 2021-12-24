from Neuron import Neuron


class R(Neuron):
    """
    Класс R-нейрона.
    """
    def __init__(self, entries=None, weights=[], current_value=None):
        """
        Конструктор. Инициалиирует экземпляр R-нейрона с current_value = None, переданным списков входных нейронов(A)
        и весами A-R связей равными 0.
        :param entries: Список входных нейронов (всех A-нейронов).
        :param weights: Список весов A-R связей.
        :param current_value: Текущее значение нейрона.
        """
        super().__init__(entries, weights, current_value)
        self.weights = []
        self.current_value = None
        for a in range(len(self.entries)):
            self.weights.append(0)

    # number - порядковый номер нейрона, такой же как индекс нейрона в списке у сети. Нужен для того, чтобы
    # получить соответствующий вес связи.
    def getValue(self):
        """
        Метод "Получить значение". Вычисляет текущее значение R-нейрона с помощью пороговой функции активации
        и алгебраической суммы произведений весов A-R связей и значений входных A-нейронов.
        :return: Вычисленное текущее значение нейрона.
        """
        sum = 0
        self.current_value = None
        for i in range(len(self.entries)):
            sum += self.entries[i].current_value * self.weights[i]  # порог = 0
        self.current_value = sign(sum)


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    elif x == 0:
        return 0
