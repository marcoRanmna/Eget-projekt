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
