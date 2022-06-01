import math

class Consts:
    BASE_PRICE = {'worker': 100, 'teacher': 100, 'engineer': 200}
    BASE_COST = {'worker': 200, 'teacher': 150, 'engineer': 300}
    BASE_INCOME = {'worker': {'mine': 500}, 'teacher': {'mine': 200}, 'engineer': {'mine': 900}}
    MIN_AGE = 15
    AGE_MUL = 10

# task assigned to mahdi

class Person:
    instances = []

    def __init__(self, name, age):
        self.name = name
        self.age = int(age)
        self.level = 1
        self.work_place = None
        self.job = ""
        self.instances.append(self)

    def get_job(self):
        return self.job

    def upgrade(self):
        self.level += 1

    def do_level(self, income):
        return income * math.sqrt(self.level * self.work_place.level)

    def calc(self):
        def f(a):
            def g():
                return a

            return g

        self.calc_income = f(100)
        self.calc_life_cost = f(20)
        return self.do_level(self.calc_income()) - self.calc_life_cost()

    @staticmethod
    def calc_all():
        total_money = 0
        for it in Person.instances:
            total_money += it.calc()
        return total_money
