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
            self.S_layer.append(A(None, None, None))
        for i in range(len(list_of_paths)):
            self.A_layer.append(A(self.S_layer, None, None))
        for i in range(len(classes_count)):
            self.R_layer.append(A(self.A_layer, None, None))


    def getResult(self, image_data):
        pass