# JSON is commonly used with data APIs. Here we will learn how to parse JSON into a Python dictionary

import json

# Sample JSON

userJSON = '{"firstName":"John", "lastName" : "Doe", "age":30}'

#parse to dict
user = json.loads(userJSON)
print(user['firstName'])
print(user)

car = {'make':'Ford','model':'Mustang','year':1970}

carJSON = json.dumps(car)

print(carJSON)