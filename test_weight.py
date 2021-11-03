import unittest
from person import Person
from questions import Questions


class TestWeight(unittest.TestCase):

    def test_weight(self):
        questions = Questions()
        questions.user_weight = 90
        questions.user_goal = "lose"
        questions.user_training = 5
        questions.user_gender = "male"
        questions.user_height = 190
        questions.user_age = 20

        user = Person(questions)
        result = user.weight()

        self.assertEqual(result, 810)


if __name__ == '__main__':
    unittest.main()
