import unittest
import Solution

mean = 70
sd = 10


class SolveTestCase(unittest.TestCase):

    def testCaseI(self):
        X = 80
        actual = "{:.2f}".format(Solution.cdf(mean, sd, X, True))
        excepted = "15.87"
        self.assertEqual(actual, excepted)

    def testCaseII(self):
        X = 60
        actual = "{:.2f}".format(Solution.cdf(mean, sd, X, True))
        excepted = "84.13"
        self.assertEqual(actual, excepted)

    def testCaseIII(self):
        X = 60
        actual = "{:.2f}".format(Solution.cdf(mean, sd, X, False))
        excepted = "15.87"
        self.assertEqual(actual, excepted)
