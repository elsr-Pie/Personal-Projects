from datetime import datetime

user_input = input("enter your desired project and the deadline separated by a :\n")
input_list = user_input.split(":")

project = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()
# calculate the number of days till the deadline
days_remaining = deadline_date - today_date

print (f"Dear User! You have {days_remaining.days} to meet your goal {project}")
