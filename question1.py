
'''
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method
'''

rangeStart = 2000
rangeEnd = 3200

result = []

for i in range(rangeStart, rangeEnd):
    if(i % 7 == 0) and (i % 5 != 0):
        result.append(str(i))

print(','.join(result))
