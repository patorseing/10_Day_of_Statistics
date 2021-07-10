import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def testGetRankI(self):
        X = list(map(float, "10 9.8 8 7.8 7.7 1.7 6 5 1.4 2".split()))
        actual = Solution.getRank(X, 10)
        excepted = [10, 9, 8, 7, 6, 2, 5, 4, 1, 3]
        self.assertEqual(excepted, actual)

    def testGetRankII(self):
        X = list(map(float, "200 44 32 24 22 17 15 12 8 4".split()))
        actual = Solution.getRank(X, 10)
        excepted = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(excepted, actual)

    def testCaseI(self):
        n = 10
        X = list(map(float, "10 9.8 8 7.8 7.7 1.7 6 5 1.4 2".split()))
        Y = list(map(float, "200 44 32 24 22 17 15 12 8 4".split()))
        actual = Solution.rxy(n, X, Y)
        excepted = 0.903
        self.assertEqual(actual, excepted)
