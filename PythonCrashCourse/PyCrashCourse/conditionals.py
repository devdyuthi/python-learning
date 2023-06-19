# If/Else statement

x = 10
y = 5

# Simple if
if x > y:
    print(f'{x} is greater than {y}')

# If/else
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')

# elif
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')

# Nested if
if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')

# membership operators
#in
numbers = [1, 2, 3, 4, 5]

if x in numbers:
    print(x in numbers)
#not in
if x not in numbers:
    print(x not in numbers)

