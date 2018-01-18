'''
Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield
'''


def putNumbers(n):
    i = 0
    while i < n:
        j=i
        i += 1
        if j % 7 == 0:
            yield j


inputValue = input('Enter the range: ')

print(putNumbers(int(inputValue)))      # this program is not working.. need to fix it
