"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

numbers = set()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        numbers.add(text[0])
        numbers.add(text[1])
    

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        numbers.add(call[0])
        numbers.add(call[1])
    
print(f"There are {len(numbers)} different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
