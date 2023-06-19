# module is a file containing a set of functions to include in your application. There are core python modules,
# modules you can install using the pip package manager ( including Django) as well as custom modules

# importing the date time module
from datetime import date
from time import time

today = date.today()
timestamp = time()
print(today)
print(timestamp)
