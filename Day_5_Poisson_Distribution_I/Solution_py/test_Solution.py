import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def testCaseI(self):
        mean = 2.5
        X = 5
        actual = Solution.P(mean, X)
        excepted = 0.067
        self.assertEqual(actual, excepted)
