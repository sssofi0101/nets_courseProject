import unittest
from  Neuron import Neuron


class MyTestCase(unittest.TestCase):
    def test_default_constructor(self):
        n= Neuron()
        self.assertEqual(isinstance(n,Neuron), True)
        self.assertEqual(n.entries, None)
        self.assertEqual(n.weights, None)
        self.assertEqual(n.current_value, None)
    def test_constructor1(self):
        e=[1,2]
        w=[2,1]
        c=1
        n= Neuron(e,w,c)
        self.assertEqual(isinstance(n,Neuron), True)
        self.assertEqual(n.entries, [1,2])
        self.assertEqual(n.weights, [2,1])
        self.assertEqual(n.current_value, 1)
    def test_constructor2(self):
        e=[1,2]
        w=[2,1]
        n= Neuron(e,w)
        self.assertEqual(isinstance(n,Neuron), True)
        self.assertEqual(n.entries, [1,2])
        self.assertEqual(n.weights, [2,1])
        self.assertEqual(n.current_value, None)



if __name__ == '__main__':
    unittest.main()
