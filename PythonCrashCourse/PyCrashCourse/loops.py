people = ['John', 'Paul', 'Sara', 'Susan']

# for loop
for person in people:
    print(f'Current Person: {person}')

# Break
for person in people:
    if person == 'Sara':
        break
    print(f"Current Person:{person}")

#Continue
for person in people:
    if person == 'Sara':
        continue
    print(f"Current Person:{person}")

# range
for i in range(len(people)):
    print(people[i])

for i in range(0,11):
    print(f'Number: {i}')

# while loop

count = 0

while count <= 10:
    print(f'Count: {count}')
    count += 1
