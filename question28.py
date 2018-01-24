'''
Question:
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

Hints:

Use len() function to get the length of a string
'''


def printValue(s1, s2):
    len1 = len(s1)
    len2 = len(s2)

    if len1 > len2:
        print(len1)
    elif len1 < len2:
        print(len2)
    else:
        print(len1)
        print(len2)


printValue("one", "three")
