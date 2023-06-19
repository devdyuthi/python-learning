class Mammal:
    def walk(self):
        print("walking")


class Dog(Mammal):
    def fetch(self):
        print("fetch")


class Cat(Mammal):
    def lick_milk(self):
        print("Licking milk bowl")

Henry = Dog
Henry.fetch(Henry)

Henriettta = Cat
Henriettta.lick_milk(Henriettta)

Kaylo = Mammal
Kaylo.walk(Kaylo)
