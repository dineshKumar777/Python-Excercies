'''
Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''


input_str = input("Enter a string: ")
d = {"UPPER": 0, "LOWER": 0}

for char in input_str:
    if char.isupper():
        d["UPPER"] += 1
    elif char.islower():
        d["LOWER"] += 1
    else:
        pass


print("UPPPER: ", d["UPPER"])
print("LOWER: ", d["LOWER"])
