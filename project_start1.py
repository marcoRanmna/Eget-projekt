# class Calories(cal):
# cal =


def weight(kg):
    kg *= 9
    return kg


def height(cm):
    cm *= 7
    return cm


def age(my_age):
    my_age *= 6

    if my_age <= 15:
        my_age += 6

    return my_age


def main():
    print("Welcome to my calorie calculator!")
    user_weight = (int(input("Please enter your weight:")))
    user_height = (int(input("Please enter your height:")))
    user_age = (int(input("Please enter your age:")))

    print("----------------------------")

    print("Maintain weight:", weight(user_weight) + height(user_height) + age(user_age))
    print("Calories/day")


if __name__ == "__main__":
    main()
