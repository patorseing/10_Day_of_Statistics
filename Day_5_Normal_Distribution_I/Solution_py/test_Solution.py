import unittest
import Solution

mean = 20
sd = 2


class SolveTestCase(unittest.TestCase):

    def testCaseI(self):
        X = 19.5
        actual = "{:.3f}".format(Solution.cdf(mean, sd, X))
        excepted = "0.401"
        self.assertEqual(actual, excepted)

    def testCaseII(self):
        lower, upper = [20, 22]
        actual = "{:.3f}".format(Solution.cdf(
            mean, sd, upper) - Solution.cdf(mean, sd, lower))
        excepted = "0.341"
        self.assertEqual(actual, excepted)
