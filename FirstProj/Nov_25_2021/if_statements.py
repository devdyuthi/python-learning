day = input("What type of day is it { it's hot, it's cold }: ")
if day.lower() == "it's hot":
    print("It's a hot day, "
          "Drink plenty of water")
elif day.lower() == "it's cold":
    print("It's a cold day, "
          "Wear warm clothes")
else:
    print ("It's a lovely day, "
           "Enjoy yourself")

if_hot = False
if_cold = True
if if_hot:
    print("It's a hot day, "
          "Drink plenty of water")
elif if_cold:
    print("It's a cold day, "
          "Wear warm clothes")
else:
    print("It's a lovely day, "
          "Enjoy yourself")


