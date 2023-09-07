'''
Part 2: Write a Python program to accept two command line arguments that are numbers, print their values and their sum within a single f-string

Remember this program must be run from the command line or a terminal emulator within your IDE

To launch program:  python3 lab_pt2.py <arg1> <arg2>
'''

import sys

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

print(f'Sum of {num1} and {num2} is {num1 + num2}')