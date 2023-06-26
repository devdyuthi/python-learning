from module import *

user_input = str
while user_input != "stop":
    user_input = input(">>enter a number of days and conversion unit (type stop to terminate)\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dict = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dict)
    run_program()
