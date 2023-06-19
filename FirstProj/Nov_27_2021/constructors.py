# a constructor is a function that gets called at the time of naming an object
class Point:
    #these are methods for the class
    #__init__ is a constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")


point = Point(10,20)

#Excercise

class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f"Hi there, I'm {self.name}")

MoshHamedani = Person("Mosh")
MoshHamedani.talk()

CelesteHamedani = Person("Celeste")
CelesteHamedani.talk()
