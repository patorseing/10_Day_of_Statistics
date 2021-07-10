import unittest
import Solution


class SolveTestCase(unittest.TestCase):

    def testMeanCastI(self):
        X = list(map(float, "10 9.8 8 7.8 7.7 7 6 5 4 2".split()))
        actual = Solution.mean(X)
        excepted = 6.73
        self.assertEqual(actual, excepted)

    def testMeanCastII(self):
        X = list(map(float, "200 44 32 24 22 17 15 12 8 4".split()))
        actual = Solution.mean(X)
        excepted = 37.8
        self.assertEqual(actual, excepted)

    def testSDCastI(self):
        X = list(map(float, "10 9.8 8 7.8 7.7 7 6 5 4 2".split()))
        meanx = Solution.mean(X)
        actual = Solution.sd(X, meanx)
        excepted = 2.39251
        self.assertEqual(actual, excepted)

    def testSDCastII(self):
        X = list(map(float, "200 44 32 24 22 17 15 12 8 4".split()))
        meanx = Solution.mean(X)
        actual = Solution.sd(X, meanx)
        excepted = 55.19928
        self.assertEqual(actual, excepted)

    def testCastI(self):
        n = 10
        X = list(map(float, "10 9.8 8 7.8 7.7 7 6 5 4 2".split()))
        Y = list(map(float, "200 44 32 24 22 17 15 12 8 4".split()))
        actual = Solution.Cor(n, X, Y)
        excepted = 0.612
        self.assertEqual(actual, excepted)
