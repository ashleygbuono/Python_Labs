'''
Part3: Complete the following Python program that answers the questions stated in the comments:

'''


# Part 3: Are strings the same?
string1 = "Hello"
string2 = "Hello"
# Verify these are the same object...Are these strings the same?
print('Is string1 the same as string2 on assignment?: ', end="")
print(id(string1) == id(string2))   #returns true
## Code something here that answers the above question ## 
string1 = string1 + " There"
string2 = string2 + " There"
# How about now? Are these the same string now?
# Are they the same string as their previous values when defined?
print('Is string1 the same as string2 after concat?: ', end="")
print(id(string1) == id(string2))
## Code something here that answers the above question ## # Are these numbers the same?
num1 = 10
num2 = 10.0

print('Is num1 the same as num2 on assignment?: ', end="")
print(id(num1) == id(num2))
## Code something here that answers the above question ## 
# Verify that Python assigns a different object reference to
# num1 and num2 than it had before the arithmetic
num1 = num1 + 100 ;
num2 = num2 - 5

print('Is num1 the same as num2 after arithmetic?: ', end="")
print(id(num1) == id(num2))
## Code something here that answers the above question ##