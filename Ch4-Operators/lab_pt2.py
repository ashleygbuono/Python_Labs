'''
Part 2: Write a Python program that converts Celsius to Fahrenheit by using the following formula:
Faren = ( ( 9 * Cels) / 5 ) + 32

Prompt the user for a Celsius temperature. Remember that user input is returned
as a character string and must be converted! The program may be done in two lines
'''

cels = input('Enter a temperature in Celcius ---> ')

print(f'The temperature in Fahrenheit is {(9 * float(cels) / 5) + 32}')