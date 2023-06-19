#classes define developer-made types
#Even though numbers, strings etc are use ful we cannot always use them

class Point:
    #these are methods for the class
    def move(self):
        print("move")
    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

