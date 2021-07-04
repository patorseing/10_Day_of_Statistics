import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def testConvertInt(self):
        x = "64630 11735 14216 99233 14470 4978 73429 38120 51135 67060"
        actual = Solution.convertInt(x)
        excepted = [64630, 11735, 14216, 99233,
                    14470, 4978, 73429, 38120, 51135, 67060]
        self.assertEqual(actual, excepted)

    def testMeanCaseI(self):
        N = 10
        x = "64630 11735 14216 99233 14470 4978 73429 38120 51135 67060"
        x = Solution.convertInt(x)
        actual = Solution.mean(N, x)
        excepted = 43900.6
        self.assertEqual(actual, excepted)

    def testMeanCaseII(self):
        N = 20
        x = "6392 51608 71247 14271 48327 50618 67435 47029 61857 22987 64858 99745 75504 85464 60482 30320 11342 48808 66882 40522"
        x = Solution.convertInt(x)
        actual = Solution.mean(N, x)
        excepted = 51284.9
        self.assertEqual(actual, excepted)

    def testFindPosCaseI(self):
        N = 10
        actual = Solution.findPosMed(N)
        excepted = 5
        self.assertEqual(actual, excepted)

    def testFindPosCaseII(self):
        N = 9
        actual = Solution.findPosMed(N)
        excepted = 5
        self.assertEqual(actual, excepted)

    def testMedianCaseI(self):
        N = 10
        x = "64630 11735 14216 99233 14470 4978 73429 38120 51135 67060"
        x = Solution.convertInt(x)
        actual = Solution.median(N, x)
        excepted = 44627.5
        self.assertEqual(actual, excepted)

    def testMedianCaseII(self):
        N = 9
        x = "64630 11735 14216 99233 14470 4978 73429 38120 51135"
        x = Solution.convertInt(x)
        actual = Solution.median(N, x)
        excepted = 38120
        self.assertEqual(actual, excepted)

    def testMedianCaseIII(self):
        N = 20
        x = "6392 51608 71247 14271 48327 50618 67435 47029 61857 22987 64858 99745 75504 85464 60482 30320 11342 48808 66882 40522"
        x = Solution.convertInt(x)
        actual = Solution.median(N, x)
        excepted = 51113.0
        self.assertEqual(actual, excepted)

    def testModeCaseI(self):
        x = "64630 11735 14216 99233 14470 4978 73429 38120 51135 67060"
        x = Solution.convertInt(x)
        actual = Solution.mode(x)
        excepted = 4978
        self.assertEqual(actual, excepted)

    def testModeCaseII(self):
        N = 20
        x = "6392 51608 71247 14271 48327 50618 67435 47029 61857 22987 64858 99745 75504 85464 60482 30320 11342 48808 66882 40522"
        x = Solution.convertInt(x)
        actual = Solution.mode(x)
        excepted = 6392
        self.assertEqual(actual, excepted)
