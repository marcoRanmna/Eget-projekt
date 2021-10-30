import unittest
from person import Person
from questions import Questions


class TestAge(unittest.TestCase):
    def test_age(self):
        questions = Questions()
        questions.user_age = 20
        questions.user_goal = "lose"
        questions.user_training = 5
        questions.user_gender = "male"
        questions.user_weight = 90
        questions.user_height = 190

        user = Person(questions)
        result = user.age()

        self.assertEqual(result, 220)


if __name__ == '__main__':
    unittest.main()
