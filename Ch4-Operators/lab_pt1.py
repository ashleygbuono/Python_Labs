'''
Part 1: Write a Python program that produces the following outputs:

100 times 2.71828 = 271.828
100 divided by 2.71828 = 36.787968862663156
2.71828 raised to the power of 3.14159 to 6 decimals is 23.140582
100 plus 200 THEN multiplied by 2.71828 is 815.484
100 plus 200 THEN divided by 2.71828 plus 3.14159 is 51.1956749893769 
100 divided by 2.71828 plus 200 divided by 3.14159 is 100.44999987243847
Is 100 less than 200? True
Is 100 greater than 2.71828 OR 3.14159 equal to 200? True 
Is 100 cubed greater than 200 squared? True
Is true greater than false? True
The letter "f" in "abcdef" ? True
The letter "K" is not in "abcdef" ? True
100 equals 100.0 ? True
100 is the same object as 100.0 ? False

Use the following variable declarations if you like:
an_int = 100 
another_int = 200 
a_float = 2.71828 
another_float = 3.14159 
num1 = 100
num2 = 100.0

'''

one_int = 100
another_int = 200
a_float = 2.71828
another_float = 3.14159
num1 = 100
num2 = 100.0

print(f'{one_int} times {a_float} = {one_int * a_float}')
print(f'{one_int} divided by {a_float} = {one_int / a_float}')
print(f'{a_float} raised to the power of {another_float} to 6 decimals is {a_float ** another_float:.6f}')
print(f'{one_int} plus {another_int} THEN multiplied by {a_float} is {(one_int + another_int) * a_float} ')
print(f'{one_int} plus {another_int} THEN divided by {a_float} plus {another_float} is {(one_int + another_int) / (a_float + another_float)}')
print(f'{one_int} divided by {a_float} plus {another_int} divided by {another_float} is {(one_int / a_float) + (another_int / another_float)}')
print(f'Is {one_int} less than {another_int}? {one_int < another_int}')
print(f'Is {one_int} greater than {a_float} OR {another_float} equal to {another_int}? {one_int > a_float or another_float == another_int}')
print(f'Is {one_int} cubed greater than {another_int} squared? {one_int**3 > another_int**2}')
print(f'Is true greater than false? {True > False}')
print(f'The letter "f" in "abcdef"? {"f" in "abcdef"}')
print(f'The letter "K" is not in "abcdef"? {"K" not in "abcdef"}')
print(f'{num1} equals {num2}? {num1 == num2}')
print(f'{num1} is the same object as {num2}? {num1 is num2}')