import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def testFactorialCaseI(self):
        x = 0
        actual = Solution.factorial(x)
        excepted = 1
        self.assertEqual(actual, excepted)

    def testFactorialCaseII(self):
        x = 1
        actual = Solution.factorial(x)
        excepted = 1
        self.assertEqual(actual, excepted)

    def testFactorialCaseIII(self):
        x = 2
        actual = Solution.factorial(x)
        excepted = 2
        self.assertEqual(actual, excepted)

    def testFactorialCaseIV(self):
        x = 5
        actual = Solution.factorial(x)
        excepted = 120
        self.assertEqual(actual, excepted)

    def testCaseI(self):
        b, g = [1.09, 1]
        actual = Solution.BinomialDistribution(b, g)
        excepted = 0.696
        self.assertEqual(actual, excepted)
