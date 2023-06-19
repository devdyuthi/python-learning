# create function
def sayhello(name='sam'):
    print(f'Hello {name}')


# returning values
def getSum(num1, num2):
    total = num1 + num2
    return total


# LAMBDA FUNCTION!!!!!!

getSum = lambda num1, num2: num1 + num2

print(getSum(10, 3))