'''
Question:
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

Hints:

Use if statement to judge condition.
'''

inp_str = input("Enter yes or no: ")

if inp_str == "yes" or inp_str == "Yes" or inp_str=="YES":
    print("Yes")
else:
    print("No")
