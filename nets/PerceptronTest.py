import unittest

from PIL import Image

from Perceptron import Perceptron


class MyTestCase(unittest.TestCase):
    def test_result(self):
        p = Perceptron(60, 18, 10)
        list_of_paths = []
        list_of_paths.append('../dataset1/0/0.png')
        list_of_paths.append('../dataset1/1/1_1.png')
        list_of_paths.append('../dataset1/1/1_2.png')
        list_of_paths.append('../dataset1/2/2_1.png')
        list_of_paths.append('../dataset1/2/2_2.png')
        list_of_paths.append('../dataset1/3/3_1.png')
        list_of_paths.append('../dataset1/3/3_2.png')
        list_of_paths.append('../dataset1/4/4.png')
        list_of_paths.append('../dataset1/5/5_1.png')
        list_of_paths.append('../dataset1/5/5_2.png')
        list_of_paths.append('../dataset1/5/5_3.png')
        list_of_paths.append('../dataset1/5/5_4.png')
        list_of_paths.append('../dataset1/6/6_1.png')
        list_of_paths.append('../dataset1/7/7.png')
        list_of_paths.append('../dataset1/8/8_1.png')
        list_of_paths.append('../dataset1/8/8_2.png')
        list_of_paths.append('../dataset1/9/9_1.png')
        list_of_paths.append('../dataset1/9/9_2.png')
        p.train(list_of_paths)
        image_data = []
        img = Image.open('../dataset1/9/9_2.png')
        width = img.size[0]
        height = img.size[1]
        pix = img.load()
        img.close()
        s1 = []
        for w in range(width):
            for h in range(height):
                if pix[w, h] == (0, 0, 0, 255):  # черный
                    s1.append(1)
                elif pix[w, h] == (255, 255, 255, 255):  # белый
                    s1.append(0)
        result = p.get_result(s1)
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()
