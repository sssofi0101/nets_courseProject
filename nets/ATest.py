import unittest
from A import A
from S import S


class MyTestCase(unittest.TestCase):
    def test_func(self):
        w1 = [-1, 0, 1]
        n1 = S(None, None, 1)
        n2 = S(None, None, 0)
        n3 = S(None, None, 1)
        entries = []
        entries.append(n1)
        entries.append(n2)
        entries.append(n3)
        a = A(entries, w1)
        self.assertEqual(a.getValue(), 0)


if __name__ == '__main__':
    unittest.main()
