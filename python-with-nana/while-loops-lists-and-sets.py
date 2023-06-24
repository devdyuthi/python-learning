calc_to_units = 24
name_of_unit = "hours"


def day_to_unit(num_of_days):
    return f"{num_of_days} day(s) is/are {num_of_days * calc_to_units} {name_of_unit}"


def run_program():
    try:
        user_input_num = int(user_input)
        if user_input_num > 0:
            calc_value = day_to_unit(int(element))
            print(calc_value)
        elif user_input_num == 0:
            print("sorry! number of days cannot be 0 :(")
        else:
            print("sorry! number of days must be a positive value :(")

    except:
        print("sorry! your input is invalid :(")


user_input = ""
while user_input != "stop":
    user_input = input(">>enter a number of days to be converted to hours (type stop to terminate)\n")
    for element in user_input.split(","):
        run_program()


