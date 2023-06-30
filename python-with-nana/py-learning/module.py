from modularization import *


def day_to_unit(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} day(s) is/are {int(num_of_days) * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} day(s) is/are {int(num_of_days) * 24 * 60} minutes"
    else:
        return "unsupported unit"


def run_program(days_and_unit_dict):
    try:
        user_input_num = int(days_and_unit_dict["days"])
        if user_input_num > 0:
            calc_value = day_to_unit(user_input_num, days_and_unit_dict["unit"])
            print(calc_value)
        elif user_input_num == 0:
            print("sorry! number of days cannot be 0 :(")
        else:
            print("sorry! number of days must be a positive value :(")

    except:
        if user_input != "stop":
            print("sorry your input is invalid")
