import unittest
from R import R
from A import A
from S import S


class MyTestCase(unittest.TestCase):
    def test_func(self):
        s1 = S(None, None, 1)
        s2 = S(None, None, 0)
        s3 = S(None, None, 1)
        e1 = []
        e1.append(s1)
        e2 = []
        e2.append(s2)
        e3 = []
        e3.append(s3)
        w1 = [0]
        w2 = [1]
        w3 = [-1]
        w = [1, 0, 1]
        n1 = A(e1, w1)
        n1.current_value = n1.getValue()
        n2 = A(e2, w2)
        n2.current_value = n2.getValue()
        n3 = A(e3, w3)
        n3.current_value = n3.getValue()
        entries = []
        entries.append(n1)
        entries.append(n2)
        entries.append(n3)
        r = R(entries, w)
        self.assertEqual(r.getValue(), -1)


if __name__ == '__main__':
    unittest.main()
