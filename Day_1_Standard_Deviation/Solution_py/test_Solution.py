import unittest
import Solution

# import sys
# sys.path.append('../../Day_0_Mean_Median_and_Mode/')
# from Solution_py.Solution import convertInt


class SolveTestCase(unittest.TestCase):
    def testMean(self):
        arr = [10, 40, 30, 50, 20]
        actual = Solution.mean(arr)
        experted = 30.0
        self.assertEqual(actual, experted)

    def testEachMean(self):
        arr = [10, 40, 30, 50, 20]
        x = arr[0]
        u =Solution.mean(arr)
        actual = Solution.EachMean(x, u)
        experted = 400
        self.assertEqual(actual, experted)

    def test_caseI(self):
        arr = [10, 40, 30, 50, 20]
        actual = Solution.stdDev(arr)
        experted = 14.1
        self.assertEqual(actual, experted)
