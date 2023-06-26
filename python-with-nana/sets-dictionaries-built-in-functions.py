# note: a set is basically a list but it doesnt allow duplicate elements


def day_to_unit(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} day(s) is/are {int(num_of_days) * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} day(s) is/are {int(num_of_days) * 24 * 60} minutes"
    else:
        return "unsupported unit"


def run_program():
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


user_input = str
while user_input != "stop":
    user_input = input(">>enter a number of days and conversion unit (type stop to terminate)\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dict = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dict)
    run_program()

# data types review
'''str = "hello im a string"
   int = 30
   float = 3.44
   list = [1,2,3,3,4] //has duplicates
   set = {1,2,3,4,5} //doesnt have duplicates
   boolean = True/False
   dictionary = {"key":"value"}'''
