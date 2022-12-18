import unittest
from salary import Salary

class TestSalary(unittest.TestCase):
    def setUp(self):
        self.salary = Salary(2)

    def test_valid(self):
        a = self.salary.get('{"year": 2016, "month": "JULY", "salary": 1000000}')
        s1 = '{"year": 2016, "month": "JULY", "salary": 1000000, "hour_income": "6250.00"}'
        s2 = '{"year": 2016, "month": "JULY", "salary": 1000000, "hour_income": "5952.38"}'
        self.assertEqual(a in (s1+s2), True)

    def test_cah_size1(self):
        self.salary.get('{"year": 2016, "month": "JULY", "salary": 1000000}')
        self.salary.get('{"year": 2016, "month": "JULY", "salary": 1000000}')
        self.assertEqual(len(self.salary.cash.cash), 1)

    def test_cah_size3(self):
        self.salary.get('{"year": 2016, "month": "JULY", "salary": 1000000}')
        self.salary.get('{"year": 2016, "month": "JUNE", "salary": 1000000}')
        self.salary.get('{"year": 2017, "month": "JULY", "salary": 1000000}')
        self.assertEqual(len(self.salary.cash.cash), 2)
    
if __name__=="__main__":
    unittest.main()