import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def testCaseI(self):
        mean = 0.88
        X = 160
        actual = Solution.C(X, mean)
        excepted = 226.176
        self.assertEqual(actual, excepted)

    def testCaseII(self):
        mean = 1.55
        X = 128
        actual = Solution.C(X, mean)
        excepted = 286.1
        self.assertEqual(actual, excepted)
