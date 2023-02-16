import unittest
from complex import MyComplex

class TestComplex(unittest.TestCase):
    complex1=MyComplex(4, 3)
    complex2=MyComplex(2, -5)
    complex_sum=MyComplex(6, -2)
    complex_mult=MyComplex(23, -14)

    def test_eq(self):
        self.assertEqual(self.complex1, self.complex1)

    def test_not_eq(self):
        self.assertNotEqual(self.complex1, self.complex2)

    def test_sum(self):
        self.assertEqual(self.complex1.sum(self.complex2), self.complex_sum)
    
    def test_minus(self):
        self.assertEqual(self.complex1.minus(self.complex2), MyComplex(2, 8))

    def test_mult(self):
        self.assertEqual(self.complex1.mult(self.complex2), self.complex_mult)

    def test_abs(self):
        self.assertEqual(self.complex1.abs(), 5)

if __name__=="__main__":
    unittest.main()