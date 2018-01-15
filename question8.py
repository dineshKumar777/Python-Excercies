'''
Question 8
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
input_str = input(
    'Enter comma seperated words to seperate them alphabetically: ')
inputList = input_str.strip().split(',')
inputList.sort()
print(','.join(inputList))
