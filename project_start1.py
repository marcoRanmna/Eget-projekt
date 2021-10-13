
from person import Person


def choice(user_choice):
    synonyms_loss = ["loose", "weight loss", "loose weight", "cut"]
    synonyms_gain = ["gain", "weight gain", "gain weight", "bulk"]
    synonyms_maintain = ["maintain", "stay the same", "keep", "maintain weight"]

    if user_choice in synonyms_loss:
        user_choice = "Weight loss"
        return user_choice

    elif user_choice in synonyms_gain:
        user_choice = "Weight gain"
        return user_choice

    else:
        if user_choice in synonyms_maintain:
            user_choice = "Maintain weight"
            return user_choice
        return "Invalid choice"



def activity(user_training):
    if user_training == 0:
        user_training = "Little to no exercise"
        return user_training

    elif user_training == 1 or user_training <= 3:
        user_training = "Light: exercise"
        return user_training

    elif user_training == 4 or user_training <= 5:
        user_training = "Moderate: exercise"
        return user_training

    elif user_training == 6 or user_training <= 7:
        user_training = "Very Active: Intense exercise"
        return user_training


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
