from datetime import datetime, timedelta
from time import time
# Exercise 1: Print current date and time in Python
# # print (datetime.now())

# # Convert string into a datetime object
# date_string = "Feb 25 2020 4:20PM"
# dt=datetime.strptime(date_string, "%b %d %Y %I:%M%p")
# print(type(date_string))
# print(dt)

# 2020-02-25 16:20:00

# Exercise 3: Subtract a week (7 days)  from a given date in Python
# given_date = datetime(2020, 2, 25)
# delta=timedelta(days=7)
# new_date=given_date-delta
# print(new_date)

# Exercise 4: Print a date in a the following format
# given_date = datetime(2020, 2, 25)
# valid_date = given_date.strftime("%A %d %B %Y")
# print(valid_date)

# Exercise 5: Find the day of the week of a given date

# given_date = datetime(2020, 7, 26)
# print(given_date.strftime("%A"))

# Exercise 6: Add a week (7 days) and 12 hours to a given date

# given_date = datetime(2020, 3, 22, 10, 0, 0)
# new_date=given_date+timedelta(days=7, hours=12)
# print(new_date)

# Exercise 7: Print current time in milliseconds

# milliseconds = int(round(time() * 1000))
# print(milliseconds)

# Exercise 8: Convert the following datetime into a string


# given_date = datetime(2020, 2, 25)
# x=given_date.strftime("%Y-%m-%d %H:%M:%S")
# print(x)

# "2020-02-25 00:00:00"

# Exercise 9: Calculate the date 4 months from the current date
# given_date = datetime(2020, 2, 25).date()
# new_date=given_date + timedelta(days=30*4)
# print(new_date)

# Exercise 10: Calculate number of days between two given dates

# 2020-02-25
# date_1 = datetime(2020, 2, 25)

# # 2020-09-17
# date_2 = datetime(2020, 9, 17)

# result=date_2-date_1
# print(result)
# print(result.days//30)
# print(result.days%30)

