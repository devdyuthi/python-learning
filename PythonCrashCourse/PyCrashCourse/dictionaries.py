# a dictionary is a collection which is unordered, changeable and indexed. No duplicate members

# Create dict
person = {
    'first_name': 'john',
    'last_name': 'doe',
    'age': 30
}

# Use constructor
#person2 = dict(first_name='Sara', last_name='Williams')

# getvalue
print(person['first_name'])
print(person.get('last_name'))

#Add key value

person['phone'] = '520-424-6980'
print(person)
#Get keys
print(person.keys())
#Get items
print(person.items())

#Copy dict
person2 = person.copy()
person2['city'] = 'New York'
print(person2)

#Remove item
del(person['age'])
print(person)
person.pop('phone')

#clear
person.clear()

#getlength
print(len(person2))

#List of dict
people = [
    {'name': 'Martha', 'age':30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])