from datetime import datetime
user_input_goal = input(">> enter goal and deadline in separated by a colon\n")
input_list = user_input_goal.split(":")
goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")  # MUST BE A CAPITAL "Y"
today_date = datetime.today()
time_till = deadline_date - today_date
hours_till_deadline = int(time_till.total_seconds()/60/60)

print(f'Hey user! the time remaining for your goal: {goal} is {hours_till_deadline} hours!')
