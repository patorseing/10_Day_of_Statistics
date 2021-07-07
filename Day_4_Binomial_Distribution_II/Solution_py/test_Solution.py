import unittest
import Solution

'''
Task
A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:
case 1: No more than 2 rejects?
case 2: At least 2 rejects?
'''


class SolveTestCase(unittest.TestCase):
    # case 1: No more than 2 rejects?
    def testCaseI(self):
        p, n = [12, 10]
        actual = Solution.BinomialDistribution(p, n, 0, 3)
        excepted = 0.891
        self.assertEqual(actual, excepted)

    # case 2: At least 2 rejects?
    def testCaseII(self):
        p, n = [12, 10]
        actual = Solution.BinomialDistribution(p, n, 2, n+1)
        excepted = 0.342
        self.assertEqual(actual, excepted)
