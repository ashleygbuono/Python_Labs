'''
Part2: Write a Python program that produces the following output:

    100 multiplied by 3.14159 = 314.15900
    The type of 100 is <class 'int'>
    The type of 3.14159 is <class 'float'>
    The unique object identifier of 100 is 140724642960128
    The unique object identifier of 3.14159 is 1637132560336

Use num1 = 100, num2 = 3.14159
'''
num1 = 100
num2 = 3.14159

print(f'{num1} multiplied by {num2} = {num1 * num2:.5f}')
print(f'The type of {num1} is {type(num1)}')
print(f'The type of {num2} is {type(num2)}')
print(f'The unique object identifier of {num1} is {id(num1)}')
print(f'The unique object identifier of {num2} is {id(num2)}')