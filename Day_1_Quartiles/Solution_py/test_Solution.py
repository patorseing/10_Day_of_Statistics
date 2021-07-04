import unittest
import Solution
import sys
sys.path.append('../../')
from Day_0_Mean_Median_and_Mode.Solution_py.Solution import convertInt
from Day_1_Interquartile_Range.Solution_py.Solution import Seq

class SolveTestCase(unittest.TestCase):

    def test_CaseI(self):
        data = [3, 7, 8, 5, 12, 14, 21, 13,18]
        actual = Solution.quartiles(data)
        excepted = [6, 12, 16]
        self.assertEqual(actual, excepted)

    def test_CaseII(self):
        data = convertInt('4 17 7 14 18 12 3 16 10 4 4 12')
        actual = Solution.quartiles(data)
        excepted = [4, 11, 15]
        self.assertEqual(actual, excepted)
