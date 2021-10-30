import unittest
import activity


class TestActivity(unittest.TestCase):
    def test_activity(self):
        result = activity.activity(0)
        result2 = activity.activity(1 or 2 or 3)
        result3 = activity.activity(4 or 5)
        result4 = activity.activity(6 or 7)

        self.assertEqual(result, "Little to no exercise")
        self.assertEqual(result2, "Light: exercise")
        self.assertEqual(result3, "Moderate: exercise")
        self.assertEqual(result4, "Very Active: Intense exercise")


if __name__ == '__main__':
    unittest.main()
