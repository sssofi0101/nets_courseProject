import math
import os
import random

from A import A
from R import R
from S import S
from PIL import Image


class Perceptron:
    """S_layer - число S нейронов, соответствует числу входных пикселей,  A_layer - число A-нейронов, подбирается,
     изначально пусть будет равно количеству изображений для обучения, R_layer - число R-нейронов,
     число распознаваемых классов"""
    def __init__(self, S_layer_count,  A_layer_count, R_layer_count):
        """Constructor"""
        self.S_layer = []
        self.A_layer = []
        self.R_layer = []
        for i in S_layer_count:
            self.S_layer.append(S())  # current_value добавляем в train, либо уже при распознавании
        for i in A_layer_count:
            self.A_layer.append(A(self.S_layer))
        for i in R_layer_count:
            self.R_layer.append(R(self.A_layer))
        random.seed(1)
        for a in self.A_layer:
            for i in S_layer_count:
                a.weights.append(random.randint(-1, 1))  # протестировать нет ли ошибки, потому что weights заранее
                # не передан пустой массив до append при создании
        for r in self.R_layer:
            for i in A_layer_count:
                r.weights.append(0)

    def train(self, list_of_paths, classes_count):  # нужно ли мне здесь тогда classes_count?
        # перенести потом в главную программу до вызова конструктора. отсюда
        im = Image.open(list_of_paths[0])
        width = im.size[0]
        height = im.size[1]
        s_count = width*height  # досюда

        """def logistic(x):
            return 1.0 / (1 + math.exp(-x))

        def logistic_proizvodn(x):
            return logistic(x) * (1 - logistic(x))

        l_speed = 1"""
        epoch_count = 5

        # передавать в этот метод уже training_data, а то что ниже перенестив основную программу?
        training_data = []
        for i in range(len(list_of_paths)):
            img = Image.open(list_of_paths[i])
            pix = img.load()
            s1 = []
            for w in range(width):
                for h in range(height):
                    if pix[w, h] == (0, 0, 0):
                        s1.append(1)
                    elif pix[w, h] == (255, 255, 255):
                        s1.append(0)
            training_data.append(s1)
        target_output = []
        for i in range(len(list_of_paths)):
            path = os.path.dirname(list_of_paths[i])
            folder = os.path.basename(path)
            target_output.append(folder)
        training_count = len(list_of_paths)

        for epoch in range(epoch_count):
            for sample in range(training_count):
                for i in range(self.S_layer):
                    self.S_layer[i].current_value = training_data[sample][i]
                for i in range(self.A_layer):
                    self.A_layer[i].getValue()
                for i in range(self.R_layer):
                    self.R_layer[i].getValue()
                for i in range(self.R_layer):
                    if i==target_output[sample]:
                        if self.R_layer[target_output[sample]].current_value - target_output[sample] > 0:
                            for j in range(self.R_layer[target_output[sample]].entries):
                                if self.R_layer[target_output[sample]].entries[j] == 1:
                                    self.R_layer[target_output[sample]].weights[j] -= 1
                        elif self.R_layer[target_output[sample]].current_value - target_output[sample] < 0:
                            for j in range(self.R_layer[target_output[sample]].entries):
                                if self.R_layer[target_output[sample]].entries[j] == 1:
                                    self.R_layer[target_output[sample]].weights[j] += 1
                    else:
                        if self.R_layer[i].current_value - (-1) > 0:
                            for j in range(self.R_layer[i].entries):
                                if self.R_layer[i].entries[j] == 1:
                                    self.R_layer[i].weights[j] -= 1
                        elif self.R_layer[i].current_value - (-1) < 0:
                            for j in range(self.R_layer[i].entries):
                                if self.R_layer[i].entries[j] == 1:
                                    self.R_layer[i].weights[j] += 1

        """
        #прямое распространение ошибки
        for epoch in range(epoch_count):
            for sample in range(training_count):
                for node in range(self.A_layer):
                    self.A_layer[node].current_value = logistic(self.A_layer[node].getValue())
                for r in range(self.R_layer):
                    self.R_layer[r].current_value=logistic(self.R_layer[r].getValue())
                # постактивация - значение, которое должно получится
                FE = self.R_layer[r].current_value - target_output[sample]"""






    def getResult(self, image_data):
        pass
