#This calculator will tell you the remaining time you have left to live based on what you estimate your death date is: seconds, minutes, hours, days, weeks, and months remaining.

#user input
print("The average lifespan in the USA is 72-75 years old. ")
age = input("What is your current age? ")
death = input("How long do you think you will live? ")

#variables, multiplication
age_as_int = int(death)
years_remaining = age_as_int
years_remaining = int(death) - int(age)
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
hours_remaining = days_remaining * 24
minutes_remaining = hours_remaining * 60
seconds_remaining = minutes_remaining * 60

#time left
time_left = f"You have {seconds_remaining} seconds,\n {minutes_remaining} minutes, \n {hours_remaining} hours, \n {days_remaining} days, \n {weeks_remaining} weeks, \n {months_remaining} months, \n {years_remaining} years left."

print("Congratulations, you have lots of time left to live! ")
print()
print(time_left)
#end of code