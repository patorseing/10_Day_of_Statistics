import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def testCaseI(self):
        X = [[0.18, 0.89], [1.0, 0.26], [0.92, 0.11], [
            0.07, 0.37], [0.85, 0.16], [0.99, 0.41], [0.87, 0.47]]
        Y = [[109.85], [155.72], [137.66], [76.17], [139.75], [162.6], [151.77]]
        X_new = [[0.49, 0.18], [0.57, 0.83], [0.56, 0.64], [0.76, 0.18]]

        actual = Solution.predict(X_new, X, Y)
        excepted = [105.21, 142.67, 132.94, 129.7]
        self.assertEqual(actual, excepted)
