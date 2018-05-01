import unittest
from src.calculator import Calculator


class TestStringMethods(unittest.TestCase):

    def test_eq2(self):
        c = Calculator()
        r1 = c.resolve_eq(3, 4, 1)
        r2 = c.resolve_eq(1, -1, -1)
        r3 = c.resolve_eq(9, -5, 0)
        r4 = c.resolve_eq(5, 0, -4)
        self.assertAlmostEqual(r1[0], [-0.3333333333333333, -1.0][0])
        self.assertAlmostEqual(r2[0], [1.618033988749895, -0.6180339887498949][0])
        self.assertAlmostEqual(r3[0], [0.5555555555555556, 0.0][0])
        self.assertAlmostEqual(r4[0], [0.894427190999916, -0.894427190999916][0])


if __name__ == '__main__':
    unittest.main()
