class HopfieldNet:
    """
    Класс нейронной сети Хопфилда.
    """
    def __init__(self, S_entries_layer = None, R_layer = None, S_outputs_layer = None):
        """
        Конструктор. Инициализирует экземпляр класса HopfieldNet.
        :param S_entries_layer: Слой входных S-нейронов.
        :param R_layer: Слой R-нейронов.
        :param S_outputs_layer:Слой выходных S-нейронов.
        """
        self.S_entries_layer = S_entries_layer
        self.R_layer = R_layer
        self.S_outputs_layer = S_outputs_layer

    def train(self, list_of_paths):
        """
        Обучение сети Хопфилда
        :param list_of_paths: Список путей к набору данных для обучения.
        :return: Обученный экземпляр сети Хопфилда.
        """
        pass

    def getResult(self, image_data):
        """
        Получить результат работы сети Хопфилда.
        :param image_data: Данные загруженной картинки в формате 1/0 по цвету.
        :return: Восстановленное изображение.
        """
        pass