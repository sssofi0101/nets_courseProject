import sys  # sys нужен для передачи argv в QApplication

from PIL import Image
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QAction, QMessageBox
import design

from Perceptron import Perceptron


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    """
    Класс приложения. Объединяет логику программы с интерфейсом.
    """
    def __init__(self):
        """
        Конструктор. Создает экземпляр приложения. Соединяет кнопки интерфейса и действия при их нажатии.
        """
        super().__init__()
        self.setupUi(self)
        loadAction = QAction("&Выбрать", self)
        self.loadImage.addAction(loadAction)
        loadAction.triggered.connect(self.load_image)
        self.image_data = []
        self.perceptron = None
        self.newPerceptron.triggered.connect(self.new_perceptron)
        self.trainPerceptron_2.triggered.connect(self.train_perceptron)
        self.dataset_perc = []
        self.dataset_perc.append('../dataset1/0/0.png')
        self.dataset_perc.append('../dataset1/1/1_1.png')
        self.dataset_perc.append('../dataset1/1/1_2.png')
        self.dataset_perc.append('../dataset1/2/2_1.png')
        self.dataset_perc.append('../dataset1/2/2_2.png')
        self.dataset_perc.append('../dataset1/3/3_1.png')
        self.dataset_perc.append('../dataset1/3/3_2.png')
        self.dataset_perc.append('../dataset1/4/4.png')
        self.dataset_perc.append('../dataset1/5/5_1.png')
        self.dataset_perc.append('../dataset1/5/5_2.png')
        self.dataset_perc.append('../dataset1/5/5_3.png')
        self.dataset_perc.append('../dataset1/5/5_4.png')
        self.dataset_perc.append('../dataset1/6/6_1.png')
        self.dataset_perc.append('../dataset1/7/7.png')
        self.dataset_perc.append('../dataset1/8/8_1.png')
        self.dataset_perc.append('../dataset1/8/8_2.png')
        self.dataset_perc.append('../dataset1/9/9_1.png')
        self.dataset_perc.append('../dataset1/9/9_2.png')
        self.addToDatasetPerceptron.triggered.connect(self.add_to_perc_dataset)
        self.default_dataset_perc = True
        self.getClass.clicked.connect(self.get_class)

    def load_image(self):
        """
        Метод "Загрузить картинку". Выполняется при нажатии пользователем кнопки "Выбрать" меню "Загрузить картинку".
        Запускает встроенное окно с проводником для выбора файла к загрузке. При выборе файла получает
        его абсолютный путь,записывает данные о цвете пикселей и выводит загруженную картинку на экран приложения.
        :return: Данные загруженной картинки в формате цвета пикселей. Черный - 1, белый - 0.
        """
        dialog = QtWidgets.QFileDialog(self)
        dialog.setWindowTitle('Выберите изображение')
        filename = None
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            filename = dialog.selectedFiles()

        if filename:  # не продолжать выполнение, если пользователь не выбрал файл
            img = Image.open(filename[0])
            width = img.size[0]
            height = img.size[1]
            pix = img.load()
            img.close()
            self.image_data = []
            for w in range(width):
                for h in range(height):
                    if pix[w, h] == (0, 0, 0, 255):  # черный
                        self.image_data.append(1)
                    elif pix[w, h] == (255, 255, 255, 255):  # белый
                        self.image_data.append(0)
        self.label.setScaledContents(True)
        pixmap = QPixmap(filename[0])
        self.label.setPixmap(pixmap)

    def new_perceptron(self):
        """
        Метод "Новый перцептрон". Выполняется при нажатии пользователем кнопки "Количество классов" подменю
         "Перцептрон" меню "Новая сеть".Запускает встроенные окна с выбором количества S-нейронов, A-нейронов и
         R-нейронов соответственно. Получает эти значения и на их основе создает экземпляр перцептрона. Если эти
        параметры не были введены корректно, то создается экзепляр класса перцептрон с дефолтными параметрами.
        :return: Созданный экземпляр перцептрона и информационное окно об успешном создании сети перцептрон.
        """
        s = QtWidgets.QInputDialog.getInt(self, "Введите количество S-нейронов",
                                              "Количество S-нейронов(ширина*высота изображений):")
        a = QtWidgets.QInputDialog.getInt(self, "Введите количество A-нейронов", "Количество A-нейронов:")
        r = QtWidgets.QInputDialog.getInt(self, "Введите количество R-нейронов",
                                          "Количество R-нейронов(распознаваемых классов):")
        self.perceptron = None
        if (s[0] != 0) and (s[1] is True) and (a[0] != 0) and (a[1] is True) and (r[0] != 0) and (r[1] is True):
            s_c = s[0]
            a_c = a[0]
            r_c = r[0]
            self.perceptron = Perceptron(s_c, a_c, r_c)
            inf = QMessageBox()
            inf.setWindowTitle("Информация")
            inf.setText("Новая сеть перцептрон создана. Обучите ее для дальнейшей работы с ней.")
            inf.setIcon(QMessageBox.Information)
            inf.setStandardButtons(QMessageBox.Ok)
            inf.exec_()
        else:
            self.perceptron = Perceptron(60, 130, 10)
            inf = QMessageBox()
            inf.setWindowTitle("Информация")
            inf.setText("Новая сеть перцептрон создана c значениями по умолчанию.Обучите ее для дальнейшей работы "
                        "с ней. Для пользовательских настроек перцептрона создайте сеть заново и укажите количество"
                        " нейронов корректно.")
            inf.setIcon(QMessageBox.Information)
            inf.setStandardButtons(QMessageBox.Ok)
            inf.exec_()
        return self.perceptron

    def train_perceptron(self):
        """
        Метод "Обучить перцептрон". Выполняется при нажатии пользователем кнопки "Обучить" подменю
         "Перцептрон" меню "Обучить сеть". Обучает перцептрон, который инициализирован в программе на основе набора
          данных, загруженных пользователем.
        :return: Обученный перцептрон.
        """
        self.perceptron.train(self.dataset_perc)
        return self.perceptron

    def add_to_perc_dataset(self):
        """
        Метод "Добавить в датасет перцептрона". Выполняется при нажатии пользователем кнопки "Добавить в датасет"
         подменю "Перцептрон" меню "Обучить сеть". Запускает встроенное окно с проводником для выбора файла к загрузке.
        При выборе файла получает его абсолютный путь и добавляет его в список датасета для перцептрона -
         поля класса ExampleApp. Если этот метод не был вызван, то используется дефолтный датасет для перцептрона.
        :return: Обновленный список набора данных для обучения перцептрона.
        """
        if self.default_dataset_perc:
            self.dataset_perc = []
            self.default_dataset_perc = False
        dialog = QtWidgets.QFileDialog(self)
        dialog.setWindowTitle('Выберите изображение')
        filename = None
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            filename = dialog.selectedFiles()

        if filename:
            for i in range(len(filename)):
                self.dataset_perc.append(filename[i])

    def get_class(self):
        """
        Метод "Получить класс". Выполняется при нажатии пользователем кнопки "распознанный класс" главного окна
        приложения. Получает результат работы перцептрона по распознаванию загруженной картинки.
        :return: Распознанный класс или информационное окно с информацией о необходимости загрузить изображение,
         если оно не было загружено.
        """
        if self.image_data:
            result = self.perceptron.get_result(self.image_data)
            self.classTextbox.setText("")
            self.classTextbox.setText(str(result))
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Для работы программы загрузите изображение")
            error.setIcon(QMessageBox.Critical)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()


if __name__ == '__main__':
    main()
