import unittest
from person import Person
from questions import Questions


class TestHeight(unittest.TestCase):
    def test_height(self):
        questions = Questions()
        questions.user_height = 190
        questions.user_goal = "lose"
        questions.user_training = 5
        questions.user_gender = "male"
        questions.user_weight = 90
        questions.user_age = 20

        user = Person(questions)
        result = user.height()

        self.assertEqual(result, 1330)


if __name__ == '__main__':
    unittest.main()
