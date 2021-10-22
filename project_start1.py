#  fix test1 class WeightLoss
from person import Person
from choice import choice
from activity import activity

def main():
    print("Welcome to my calorie calculator!")

    user_goal = input("Do you like to loose weight or gain weight?:")
    user_training = int(input("How many times per week do you train?:"))

    user_weight = (int(input("Please enter your weight:")))
    user_height = (int(input("Please enter your height:")))
    user_age = (int(input("Please enter your age:")))

    user = Person(user_weight, user_height, user_age)

    print("----------------------------")

    print(choice(user_goal))
    print(activity(user_training))

    print("----------------------------")

    print("Maintain weight:", user.calories())
    print("Calories/day")


if __name__ == "__main__":
    main()
