import sys  # sys нужен для передачи argv в QApplication

from PIL import Image
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QAction
import design

from Perceptron import Perceptron


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        loadAction = QAction("&Выбрать", self)
        self.loadImage.addAction(loadAction)
        loadAction.triggered.connect(self.load_image)
        self.image_data = []
        self.perceptron = None
        self.newPerceptron.triggered.connect(self.new_perceptron)
        self.trainPerceptron_2.triggered.connect(self.train_perceptron)
        self.dataset_perc=[]
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
            self.image_data=[]
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
        self.perceptron = None
        self.perceptron = Perceptron(60, 130, 10)
        return self.perceptron

    def train_perceptron(self):
        self.perceptron.train(self.dataset_perc)
        return self.perceptron

    def add_to_perc_dataset(self):
        if self.default_dataset_perc == True:
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
        result = self.perceptron.get_result(self.image_data)
        self.classTextbox.setText(str(result))


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()


if __name__ == '__main__':
    main()
