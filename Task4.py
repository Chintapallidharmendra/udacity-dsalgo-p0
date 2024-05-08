"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

telemarketers = set()
non_telemarketers = set()


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        non_telemarketers.add(text[0])
        non_telemarketers.add(text[1])



with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        telemarketers.add(call[0])
        non_telemarketers.add(call[1])

print("These numbers could be telemarketers: ")


updated_telemarketers = telemarketers.difference(non_telemarketers)
numbers = list(updated_telemarketers)
numbers.sort()


for number in numbers:
    print(number)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

