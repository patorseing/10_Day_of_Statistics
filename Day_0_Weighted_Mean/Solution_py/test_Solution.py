import unittest
import Solution

import sys
sys.path.append('../../Day_0_Mean_Median_and_Mode')
from Solution_py.Solution import convertInt

class SolveTestCase(unittest.TestCase):
  def testCaseI(self):
    X = [10, 40, 30, 50, 20]
    W = [1, 2, 3, 4, 5]
    actual = Solution.weightedMean(X, W)
    excepted = 32.0
    self.assertEqual(actual, excepted)

  def testCaseII(self):
    X = convertInt("10 40 30 50 20 10 40 30 50 20")
    W = convertInt("1 2 3 4 5 6 7 8 9 10")
    actual = Solution.weightedMean(X, W)
    excepted = 31.1
    self.assertEqual(actual, excepted)
