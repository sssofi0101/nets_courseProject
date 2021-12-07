import math
import os
import random

from A import A
from R import R
from S import S
from PIL import Image


class Perceptron:
    """S_layer - число S нейронов,  A_layer - число A-нейронов, R_layer - число R-нейронов"""
    def __init__(self, S_layer=None,  A_layer=None, R_layer=None):
        """Constructor"""
        self.S_layer = []
        self.A_layer = []
        self.R_layer = []
        if S_layer is not None:
            for i in range(S_layer):
                self.S_layer.append(S(None, None, None))
        if A_layer is not None:
            for i in range(A_layer):
                self.A_layer.append(A(self.S_layer, None, None))
        if R_layer is not None:
            for i in range(R_layer):
                self.R_layer.append(R(self.A_layer, None, None))

    def train(self, list_of_paths, classes_count):
        im = Image.open(list_of_paths[0])
        width = im.size[0]
        height = im.size[1]
        s_count = width*height
        for i in range(s_count):
            self.S_layer.append(S(None, None, None))
        for i in range(len(list_of_paths)):
            self.A_layer.append(A(self.S_layer, None, None))
        for i in range(len(classes_count)):
            self.R_layer.append(R(self.A_layer, None, None))

        def logistic(x):
            return 1.0 / (1 + math.exp(-x))

        def logistic_proizvodn(x):
            return logistic(x) * (1 - logistic(x))

        l_speed = 1
        epoch_count = 5

        random.seed(1)
        for a in self.A_layer:
            for i in range(s_count):
                a.weights.append(random.uniform(-1, 1))
        for r in self.R_layer:
            for i in range(len(list_of_paths)):
                r.weights.append(random.uniform(-1, 1))

        training_data =[]
        for i in range(len(list_of_paths)):
            img = Image.open(list_of_paths[i])
            pix = img.load()
            s1 = []
            for w in range(width):
                for h in range(height):
                    if pix[w, h]==(0, 0, 0):
                        s1.append(1)
                    elif pix[w, h]==(255, 255, 255):
                        s1.append(0)
            training_data.append(s1)
        target_output = []
        for i in range(len(list_of_paths)):
            path = os.path.dirname(list_of_paths[i])
            folder = os.path.basename(path)
            target_output.append(folder)
        training_count = len(list_of_paths)
        #прямое распространение ошибки
        for epoch in range(epoch_count):
            for sample in range(training_count):
                for node in range(self.A_layer):
                    self.A_layer[node].current_value = logistic(self.A_layer[node].getValue())
                for r in range(self.R_layer):
                    self.R_layer[r].current_value=logistic(self.R_layer[r].getValue())
                # постактивация - значение, которое должно получится
                FE = self.R_layer[r].current_value - target_output[sample]





    def getResult(self, image_data):
        pass
