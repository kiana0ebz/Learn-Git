import math
from person import Person, Consts

# task assigned to ali

class Engineer(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super(Engineer, self).__init__(name, age)
        self.job = "engineer"

    def get_price(self):
        return math.floor(Consts.BASE_PRICE[self.job] * math.sqrt(Consts.MIN_AGE / self.age))

    def calc_life_cost(self):
        return math.floor(Consts.BASE_COST[self.job] * math.sqrt(self.age / Consts.MIN_AGE))

    def calc_income(self):
        return math.floor(
            Consts.BASE_INCOME[self.job][self.work_place.get_expertise()] * math.sqrt(Consts.MIN_AGE / self.age))
