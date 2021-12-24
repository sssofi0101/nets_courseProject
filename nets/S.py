from Neuron import Neuron


class S(Neuron):
    """
    Класс S-нейрона.
    """
    def __init__(self, entries=None, weights=None, current_value=None):
        """
        Конструктор. Инициализирует S-нейрон с entries и weights = None и заданным текущим значением.
        :param entries: Список входных нейронов. У S-нейронов = None.
        :param weights: Список весов. У S-нейронов = None.
        :param current_value: Текущее значение нейрона.
        """
        super().__init__(entries, weights, current_value)
        self.entries = None
        self.weights = None

    def getValue(self):
        """
        Метод "Получить значение". Возвращет текущее значение нейрона.
        :return: Текущее значение нейрона
        """
        return self.current_value
