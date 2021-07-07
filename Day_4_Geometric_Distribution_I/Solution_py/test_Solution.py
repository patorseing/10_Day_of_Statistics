import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def testCase(self):
        numerator, denominator = list(map(int, "1 3".split()))
        n = int("5")
        actual = Solution.g(n, numerator/denominator)
        excepted = 0.066
        self.assertEqual(actual, excepted)
