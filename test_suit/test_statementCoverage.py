import unittest
from isTriangle import Triangle

class StatementCoverageTest(unittest.TestCase):
    def testEquilateral(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def testIsocelesAB(self):
        actual = Triangle.classify(10, 10, 18)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def testIsocelesAC(self):
        actual = Triangle.classify(10, 18, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def testIsocelesBC(self):
        actual = Triangle.classify(10, 18, 18)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def testScalene(self):
        actual = Triangle.classify(10, 9, 8)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def testTriangleInequalityDiff(self):
        actual = Triangle.classify(5, 6, 20)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testTriangleInequalitySame(self):
        actual = Triangle.classify(5, 5, 20)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testNegTriangle(self):
        actual = Triangle.classify(-5, 5, 20)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
if __name__ == '__main__':
    unittest.main()
