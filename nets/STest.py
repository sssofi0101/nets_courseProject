import unittest
from S import S


class MyTestCase(unittest.TestCase):
    def test_constr(self):
        e = [1, 2]
        w = [2, 1]
        c = 1
        n = S(e, w, c)
        self.assertEqual(isinstance(n, S), True)
        self.assertEqual(n.entries, None)
        self.assertEqual(n.weights, None)
        self.assertEqual(n.current_value, 1)


if __name__ == '__main__':
    unittest.main()
