
class Person:

    def __init__(self, kg, cm, my_age):
        self.kg = kg
        self.cm = cm
        self.my_age = my_age
        self.cal = None

    def weight(self):
        self.kg *= 9
        return self.kg

    def height(self):
        self.cm *= 7
        return self.cm

    def age(self):
        self.my_age *= 6
        if self.my_age >= 15:
            self.my_age += 100
        return self.my_age

    def calories(self):
        self.cal = self.weight() + self.height() + self.age()
        return self.cal


def activity(user_training):
    if user_training == 0:
        user_training = "Little to no exercise"
        print(user_training)

    elif user_training == 1 or user_training <= 3:
        user_training = "Light exercise"
        print(user_training)

    elif user_training == 4 or user_training <= 5:
        user_training = "Moderate exercise"
        print(user_training)

    elif user_training == 6 or user_training <= 7:
        user_training = "Very Active: Intense exercise"
        print(user_training)


def main():
    print("Welcome to my calorie calculator!")
    user_training = int(input("How many time per week do you train?:"))
    user_weight = (int(input("Please enter your weight:")))
    user_height = (int(input("Please enter your height:")))
    user_age = (int(input("Please enter your age:")))
    user = Person(user_weight, user_height, user_age)

    print("----------------------------")

    print(activity(user_training))

    print("Maintain weight:", user.calories())
    print("Calories/day")


if __name__ == "__main__":
    main()
