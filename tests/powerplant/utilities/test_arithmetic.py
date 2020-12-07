import powerplant
import unittest


class ArithmeticTest(unittest.TestCase):

    def test_add_positive(self):
        """
        Test that number properly add
        """
        cases = [
            ((1, 1), 2),
            ((3, 7), 10),
        ]
        for (a, b), c in cases:
            self.assertEquals(powerplant.add(a, b), c)
