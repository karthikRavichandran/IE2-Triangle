import unittest
from isTriangle import Triangle

class MutationTest(unittest.TestCase):
    def testEquilateral(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def testIsocelesAB(self):
        actual = Triangle.classify(10, 10, 19)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def testIsocelesAC(self):
        actual = Triangle.classify(10, 19, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def testIsocelesBC(self):
        actual = Triangle.classify(19, 10, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def testScalene(self):
        actual = Triangle.classify(10, 9, 8)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def testScalene2(self):
        actual = Triangle.classify(8, 9, 10)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)
    
    def testScalene3(self):
        actual = Triangle.classify(9, 10, 8)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def testTriangleInequalityDiff(self):
        actual = Triangle.classify(5, 6, 11)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testTriangleInequalitySame(self):
        actual = Triangle.classify(5, 5, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testNegTriangleA(self):
        actual = Triangle.classify(-1, 5, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def testNegTriangleB(self):
        actual = Triangle.classify(1, -5, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testNegTriangleC(self):
        actual = Triangle.classify(1, 5, -5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testNegTriangleAllThree(self):
        actual = Triangle.classify(-1, -5, -5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testNegTriangleOnlyTwo(self):
        actual = Triangle.classify(-1, 5, -5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testZeroTriangleA(self):
        actual = Triangle.classify(0, 5, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def testZeroTriangleB(self):
        actual = Triangle.classify(5, 0, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def testZeroTriangleC(self):
        actual = Triangle.classify(5, 5, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testZeroTriangleAll(self):
        actual = Triangle.classify(0, 0, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testZeroTriangleOnlyTwo(self):
        actual = Triangle.classify(0, 5, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
if __name__ == '__main__':
    unittest.main()
