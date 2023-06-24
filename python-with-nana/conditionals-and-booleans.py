calc_to_units = 24
name_of_unit = "hours"


def day_to_unit(num_of_days):
    return f"{num_of_days} days are {num_of_days * calc_to_units} {name_of_unit}"


user_input = input(">>enter a number of days to be converted to hours (type stop to terminate)\n")


# using conditionals

def validate_and_execute(user_input):
    try:
        if int(user_input) > 0:
            calc_value = day_to_unit(int(user_input))
            print(calc_value)
        elif int(user_input) == 0:
            print("sorry! number of days cannot be 0 :(")
        else:
            print("sorry! number of days must be a positive value :(")

    except:
        print("sorry! your input is invalid ")


user_input = ""
while user_input != "stop":
    user_input = input(">>enter a number of days to be converted to hours (type 'stop' to quit)\n")

    validate_and_execute(user_input)
