import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):
    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)
        with self.assertRaises(ValueError):
            calculate_bmi(0, 70)

    def test_calculate_bmr(self):
        self.assertAlmostEqual(calculate_bmr(175, 70, 25, 'male'), 1724.05, places=2)
        self.assertAlmostEqual(calculate_bmr(160, 55, 30, 'female'), 1321.96, places=2)  
        with self.assertRaises(ValueError):
            calculate_bmr(175, 70, -5, 'male')

if __name__ == '__main__':
    unittest.main()