"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

time_spent = dict()

def add_time_spent(number, duration):
    if number not in time_spent:
        time_spent[number] = int(duration)
    else:
        time_spent[number] += int(duration)


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        add_time_spent(call[0],call[3])
        add_time_spent(call[1],call[3])

max_number = None
max_value = 0
for number in time_spent.keys():
    if max_value < time_spent[number]:
        max_value = time_spent[number]
        max_number = number 
print(f"{max_number} spent the longest time, {max_value} seconds, on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

