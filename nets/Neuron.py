class Neuron:
    """
    Класс нейрона.
    """
    def __init__(self, entries=[], weights=[], current_value=None):
        """Конструктор. Инициализирует экзепляр класса Neuron с переданными в качестве параметров,либо пустыми
         значениями полей."""
        self.entries = entries
        self.weights = weights
        self.current_value = current_value

    def getValue(self):
        """
        Вычислить текущее значение нейрона.
        :return: Текущее значение нейрона.
        """
        pass
