import random
class Nazarij:
    def __init__(self,name='Human', school=None, dog=None):
        self.name=name
        self.money=100
        self.gladness=50
        self.satiety=50
        self.school=school
        self.dog=dog

    def get_school(self):
        self.school=Study()
    def get_dog(self):
        self.dog=Dog()
    def go_to_academy(self):
        self.study.progress+=0.4
        self.satiety-=4
    def chill(self):
        self.gladness+=30
        self.study.progress-=1
        self.satiety+=5
    def do_homework(self):
        self.gladness-=15
        self.study.progress+=0.3
    def go_for_a_walk_with_dog(self):
        self.gladness+=40
        self.dog.gladness+=100
    def give_food_for_dog(self):
        self.dog.satiety+=50
    def go_to_school(self):
        self.study.progress=0.5
        self.gladness-=10
        self.money+=50
        self.
    def do_something(self):
        pass
    def day_indexes(self):
        pass
    def is_alive(self):
        pass
    def live(self,day):
        pass
class Dog:
    def __init__(self,name1='Dog'):
        self.name=name1
        self.gladness=50
        self.satiety=50
class Study:
    def __init__(self):
        self.progress=0
class Parents:
    def __init__(self):