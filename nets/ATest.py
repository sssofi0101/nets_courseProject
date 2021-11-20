import unittest
from A import A
from S import S


class MyTestCase(unittest.TestCase):
    def test_func(self):
        w1=[-1,0,1]
        n1=S(None,w1,1)
        w2 = [1, 0, 0]
        n2 = S(None, w2, 0)
        w3 = [-1, 1, -1]
        n3 = S(None, w3, 1)
        entries=[]
        entries.append(n1)
        entries.append(n2)
        entries.append(n3)
        a=A(entries)
        self.assertEqual(a.getValue(2), 0)
        self.assertEqual(a.getValue(1), 1)
        self.assertEqual(a.getValue(0), -1)


if __name__ == '__main__':
    unittest.main()
