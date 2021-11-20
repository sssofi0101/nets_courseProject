import unittest
from R import R
from S import S


class MyTestCase(unittest.TestCase):
    def test_constr(self):
        e = [1, 2]
        w = [2, 1]
        c = 1
        n = R(e, w, c)
        self.assertEqual(isinstance(n, R), True)
        self.assertEqual(n.entries, [1,2])
        self.assertEqual(n.weights, None)
        self.assertEqual(n.current_value, 1)
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
        r=R(entries)
        self.assertEqual(r.getValue(2), 0)
        self.assertEqual(r.getValue(1), 1)
        self.assertEqual(r.getValue(0), -1)


if __name__ == '__main__':
    unittest.main()
