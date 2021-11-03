import unittest
import choice


class TestChoice(unittest.TestCase):
    def test_choice(self):
        result = choice.choice("lose" or "weight loss" or "lose weight" or "cut")
        result2 = choice.choice("gain" or "weight gain" or "gain weight" or "bulk")
        result3 = choice.choice("maintain" or "stay the same" or "keep" or "maintain weight")

        self.assertEqual(result, "Weight loss")
        self.assertEqual(result2, "Weight gain")
        self.assertEqual(result3, "Maintain weight")


if __name__ == '__main__':
    unittest.main()
