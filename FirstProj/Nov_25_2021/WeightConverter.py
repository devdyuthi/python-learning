weight = float(input("Weight: "))
unit = input("[L]bs or [K]gs: ")

if unit.lower() == "l":
    convert_w = weight/2.205
    print(f"You are {convert_w} in KG")
elif unit.lower() == "k":
    convert_w = weight*2.205
    print(f"You are {convert_w} in LBS")
else:
    print("!ERROR!")