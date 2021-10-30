#  fix test1 class WeightLoss
from person import Person
from questions import Questions


def main():
    questions = Questions()
    questions.greeting()
    questions.about_user()
    questions.about_training()

    user = Person(questions)
    user.train()

    print("----------------------------")

    print(user.calories() - 100000)
    print("Calories/day")


if __name__ == "__main__":
    main()
