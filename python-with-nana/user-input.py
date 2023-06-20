name_of_unit = "hours"
calc_to_units = 24


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calc_to_units} {name_of_unit}"


user_input = input("Hello user, enter a number of days and I will convert it to hours!\n")  # \n is newline
user_input_int = int(user_input)
final_value = days_to_units(user_input_int)

print(final_value)

