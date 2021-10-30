from activity import activity
from choice import choice
from question_class import Questions


class Person:

    def __init__(self, data: Questions):
        self.kg = data.user_weight
        self.cm = data.user_height
        self.my_age = data.user_age
        self.gender = data.user_gender
        self.weight_change = choice(data.user_goal)
        self.training_intensity = activity(data.user_training)
        self.calories()

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

    def train(self):
        if self.training_intensity == "Little to no exercise":
            self.calories()

        elif self.training_intensity == "Light: exercise":
            self.light_exercise()

        elif self.training_intensity == "Moderate: exercise":
            self.moderate_exercise()

        elif self.training_intensity == "Very Active: Intense exercise":
            self.very_active_exercise()

    def light_exercise(self):
        self.cal += 290

        if self.gender == 'male':
            self.cal += 229

        elif self.gender == "female":
            self.cal -= 229
        else:
            print("That's not an option")

        if self.weight == "Weight gain":
            self.cal += 250
        else:
            self.cal -= 250

    def moderate_exercise(self):
        self.cal += 439

        if self.gender == "male":
            self.cal += 244
        else:
            self.cal -= 244

        if self.weight == "Weight gain":
            self.cal += 500
        else:
            self.cal -= 500

    def very_active_exercise(self):
        self.cal += 869

        if self.gender == "male":
            self.cal += 286
        else:
            self.cal -= 286

        if self.weight == "Weight gain":
            self.cal += 1000
        else:
            self.cal -= 1000
