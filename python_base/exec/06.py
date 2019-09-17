# class Student:
#     school = 'uplooking'
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def learn(self):
#         print('{0} is learning'.format(self.name))
#
#     def eat(self):
#         print('{0} is eating'.format(self.name))
#
#     def sleep(self):
#         print('{0} is sleeping'.format(self.name))
#
#
# superman = Student('superman', 10, 'male')
# batman = Student('batman', 19, 'male')
#
# superman.learn()
# batman.learn()
#
# Student.learn(superman)
# Student.learn(batman)


# class Superman:
#     def __init__(self, life_value=100, aggressivity=10):
#         self.life_value = life_value
#         self.aggressivity = aggressivity
#
#     def attack(self, enemy):
#         enemy.life_value -= self.aggressivity
#
#
# class Batman:
#     def __init__(self, life_value=100, aggressivity=10):
#         self.life_value = life_value
#         self.aggressivity = aggressivity
#
#     def attack(self, enemy):
#         enemy.life_value -= self.aggressivity
#
#
# print("创建超人和蝙蝠侠")
# s1 = Superman()
# b1 = Batman()
# print("超人当前生命值：")
# print(s1.life_value)
# print("超人被蝙蝠侠打了一拳")
# b1.attack(s1)
# print("超人被打后的什么值：")
# print(s1.life_value)


class JusticeLeague:
    def __init__(self, life_value=100, aggressivity=10):
        self.life_value = life_value
        self.aggressivity = aggressivity

    def attack(self, enemy):
        enemy.life_value -= self.aggressivity


class Superman(JusticeLeague):
    pass


class Batman(JusticeLeague):
    pass


print("创建超人和蝙蝠侠")
s1 = Superman()
b1 = Batman()
print("超人当前生命值：")
print(s1.life_value)
print("超人被蝙蝠侠打了一拳")
b1.attack(s1)
print("超人被打后的什么值：")
print(s1.life_value)