# Print the mea of the numbers given in a file

import sys

sum = 0
n = 0

# Sum input values
for num in open('data.txt'):
    sum += float(num)
    n += 1

print sum / n
