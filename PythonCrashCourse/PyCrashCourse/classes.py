# Create class

class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f"My name is {self.name} and I'm {age}"

    def has_birthday(self):
        self.age += 1


# Extend class
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    @property
    def greeting(self):
        return f"My name is {self.name} and I'm {self.age} and my balance is {self.balance}"


# init user object

harshil = User('Harshil Bandarupalli', 'hmb8838@gmail.com', 6)

# Init customer
janet = Customer('Janet Johnson', "jj@yahoo.com", 19)

janet.set_balance(500)
print(janet.greeting)
harshil.has_birthday()
print(harshil.age)
