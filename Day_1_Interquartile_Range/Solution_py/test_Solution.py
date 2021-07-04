import unittest
import Solution

import sys
sys.path.append('../../Day_0_Mean_Median_and_Mode')
from Solution_py.Solution import convertInt


class SolveTestCase(unittest.TestCase):
    # Test Q1
    def test_Q1CaseI(self):
        values = [1, 2, 3, 4, 5, 6]
        freqs = [1, 1, 1, 1, 1, 1]
        arr = Solution.Seq(values, freqs)
        actual = Solution.Quartile(arr, 1)
        excepted = 2.0
        self.assertEqual(actual, excepted)

    def test_Q1CaseII(self):
        values = [1, 2, 3, 4, 5, 6, 7]
        freqs = [1, 1, 1, 1, 1, 1, 1]
        arr = Solution.Seq(values, freqs)
        actual = Solution.Quartile(arr, 1)
        excepted = 2.0
        self.assertEqual(actual, excepted)

    def test_Q1CaseIII(self):
        values = [1, 2, 3]
        freqs = [3, 2, 1]
        arr = Solution.Seq(values, freqs)
        actual = Solution.Quartile(arr, 1)
        excepted = 1.0
        self.assertEqual(actual, excepted)

    def test_Q1CaseIV(self):
        values = [6, 12, 8, 10, 20, 16]
        freqs = [5, 4, 3, 2, 1, 5]
        arr = Solution.Seq(values, freqs)
        actual = Solution.Quartile(arr, 1)
        excepted = 7.0
        self.assertEqual(actual, excepted)

    # Test Q2
    def test_Q2CaseI(self):
        values = [1, 2, 3, 4, 5, 6]
        freqs = [1, 1, 1, 1, 1, 1]
        arr = Solution.Seq(values, freqs)
        actual = Solution.Quartile(arr, 2)
        excepted = 3.5
        self.assertEqual(actual, excepted)

    def test_Q2CaseII(self):
        values = [1, 2, 3, 4, 5, 6, 7]
        freqs = [1, 1, 1, 1, 1, 1, 1]
        arr = Solution.Seq(values, freqs)
        actual = Solution.Quartile(arr, 2)
        excepted = 4.0
        self.assertEqual(actual, excepted)

    def test_Q2CaseIII(self):
        values = [1, 2, 3]
        freqs = [3, 2, 1]
        arr = Solution.Seq(values, freqs)
        actual = Solution.Quartile(arr, 2)
        excepted = 1.5
        self.assertEqual(actual, excepted)

    def test_Q2CaseIV(self):
        values = [6, 12, 8, 10, 20, 16]
        freqs = [5, 4, 3, 2, 1, 5]
        arr = Solution.Seq(values, freqs)
        actual = Solution.Quartile(arr, 2)
        excepted = 11.0
        self.assertEqual(actual, excepted)

    # Test Q3
    def test_Q3CaseI(self):
        values = [1, 2, 3, 4, 5, 6]
        freqs = [1, 1, 1, 1, 1, 1]
        arr = Solution.Seq(values, freqs)
        actual = Solution.Quartile(arr, 3)
        excepted = 5.0
        self.assertEqual(actual, excepted)

    def test_Q3CaseII(self):
        values = [1, 2, 3, 4, 5, 6, 7]
        freqs = [1, 1, 1, 1, 1, 1, 1]
        arr = Solution.Seq(values, freqs)
        actual = Solution.Quartile(arr, 3)
        excepted = 6.0
        self.assertEqual(actual, excepted)

    def test_Q3CaseIII(self):
        values = [1, 2, 3]
        freqs = [3, 2, 1]
        arr = Solution.Seq(values, freqs)
        actual = Solution.Quartile(arr, 3)
        excepted = 2.0
        self.assertEqual(actual, excepted)

    def test_Q3CaseIV(self):
        values = [6, 12, 8, 10, 20, 16]
        freqs = [5, 4, 3, 2, 1, 5]
        arr = Solution.Seq(values, freqs)
        actual = Solution.Quartile(arr, 3)
        excepted = 16.0
        self.assertEqual(actual, excepted)

    # full Test
    def test_CaseI(self):
        values = [1, 2, 3, 4, 5, 6]
        freqs = [1, 1, 1, 1, 1, 1]
        actual = Solution.interQuartile(values, freqs)
        excepted = '3.0'
        self.assertEqual(actual, excepted)

    def test_CaseII(self):
        values = [1, 2, 3, 4, 5, 6, 7]
        freqs = [1, 1, 1, 1, 1, 1, 1]
        actual = Solution.interQuartile(values, freqs)
        excepted = '4.0'
        self.assertEqual(actual, excepted)

    def test_CaseIII(self):
        values = [1, 2, 3]
        freqs = [3, 2, 1]
        actual = Solution.interQuartile(values, freqs)
        excepted = '1.0'
        self.assertEqual(actual, excepted)

    def test_CaseIV(self):
        values = [6, 12, 8, 10, 20, 16]
        freqs = [5, 4, 3, 2, 1, 5]
        actual = Solution.interQuartile(values, freqs)
        excepted = '9.0'
        self.assertEqual(actual, excepted)

    def test_CaseV(self):
        values = convertInt("10 40 30 50 20 10 40 30 50 20 1 2 3 4 5 6 7 8 9 10 20 10 40 30 50 20 10 40 30 50")
        freqs = convertInt("1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 10 40 30 50 20 10 40 30 50 20")
        actual = Solution.interQuartile(values, freqs)
        excepted = '30.0'
        self.assertEqual(actual, excepted)

    def test_CaseVI(self):
        values = convertInt("10 40 30 50 20 10 40 30 50 20 1 2 3 4 5 6 7 8 9 10")
        freqs = convertInt("1 2 3 4 5 6 7 8 9 10 10 40 30 50 20 10 40 30 50 20")
        actual = Solution.interQuartile(values, freqs)
        excepted = '5.0'
        self.assertEqual(actual, excepted)
