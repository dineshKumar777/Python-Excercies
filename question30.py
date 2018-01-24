'''
Question:
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

Hints:

Use % operator to check if a number is even or odd.
'''


def checkevenorodd(num):
    if num % 2 == 0:
        print("Given number is even")
    else:
        print("Given number is odd")


checkevenorodd(7)
