
class Questions:
    def __init__(self):
        self.user_goal = ""
        self.user_training = ""
        self.user_gender = ""
        self.user_weight = ""
        self.user_height = ""
        self.user_age = ""

    def greeting(self):
        print("Welcome to my calorie calculator!")
        print("----------------------------")

    def about_training(self):
        self.user_goal = input("Would you like to: \nLoose weight \nGain weight \nMaintain weight \nYour answer:")
        self.user_training = int(input("How many times per week do you train?:"))

    def about_user(self):
        self.user_gender = input("Please enter your gender here:")
        self.user_weight = (int(input("Please enter your weight:")))
        self.user_height = (int(input("Please enter your height:")))
        self.user_age = (int(input("Please enter your age:")))
