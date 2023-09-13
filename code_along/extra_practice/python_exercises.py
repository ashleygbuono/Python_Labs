'''
https://www.w3resource.com/python-exercises/python-functions-exercises.php

'''

#Write a Python function to find the maximum of three numbers.
def find_max(num1, num2, num3):
    #list() constructor works with either strings or iterables -- passed "tuple" of args to work with nums
    return max(list((num1, num2, num3)))

print(f'The find_max function returns: {find_max(3, 60, 233)} for arguments 3, 60, 233')


#Write a Python function to sum all the numbers in a list.
def sum_numbers(list_1):
    return sum(list_1)

print(f'The sum_numbers function returns: {sum_numbers([3, 60, 233])} for arguments 3, 60, 233')


# Write a Python function to multiply all the numbers in a list.
def multiply_nums(list_1):
    result = 1
    for num in list_1:
        result *= num
    
    return result

print(f'The multiply_nums function returns: {multiply_nums([3, 60, 233])} for arguments 3, 60, 233')


#Write a Python program to reverse a string.
def reverse_string(str):
    return str[::-1]
    
print(f'The reverse_string function returns: {reverse_string("Hello World")} for argument "Hello World"')


#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(num):
    result = 1
    for step in range(num, 1, -1):
        result *= step
    return result

print(f'The factorial function returns: {factorial(6)} for argument 6')


#Write a Python function to check whether a number falls within a given range.
def in_range(num, low, high):
    if low <= num <= high:
        return True
    else:
        return False
    
print(f'The in_range function returns: {in_range(43, 22, 100)} for arguments 43, 22, 100')
print(f'The in_range function returns: {in_range(30, 32, 34)} for arguments 30, 32, 34')


#Write a Python function that accepts a string and counts the number of upper and lower case letters.
def count_case(str):
    upper_count = 0
    lower_count = 0

    for char in str:
        if char.isupper():
            upper_count += 1
        else:
            lower_count += 1

    return upper_count, lower_count

print(f'The count_case function returns: (uppercase count, lowercase count) of {count_case("This iS a MiXed case sTrinG")}')


#Write a Python function that takes a list and returns a new list with distinct elements from the first list.
def unique_list(list_1):
    return list(set(list_1))

print(f'The unique_list function returns: {unique_list([3, 4, 5, 4, 3, 1, 8, 29, 5, 4, 1, 2])} for argument [3, 4, 5, 4, 3, 1, 8, 29, 5, 4, 1, 2]')


#Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
def is_prime(num):
    from math import sqrt, floor

    for n in range(2, floor(sqrt(num))):
        if num % n == 0:
            return False
        else:
            return True
        
print(f'The is_prime function returns: {is_prime(19)} for argument 19')
print(f'The is_prime function returns: {is_prime(2064)} for argument 2064')



#Write a Python function to check whether a number is "Perfect" or not.
#According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). 
#Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).


#Write a Python function that checks whether a passed string is a palindrome or not.
def is_palindrome(str):
    reversed_str = str[::-1]
    if str == reversed_str:
        return True
    else: 
        return False

print(f'The is_palindrome function returns: {is_palindrome("This is a palindrome")} for argument "This is a palindrome"')
print(f'The is_palindrome function returns: {is_palindrome("racecar")} for argument "racecar"')

#Write a Python function to check whether a string is a pangram or not.
#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
def is_panagram(str):
    alpha_chars = "abcdefghijklmnopqrstuvwxyz"

    for char in alpha_chars:
        if char not in str.lower():
            return False
        
    return True

print(f'The is_panagram function returns: {is_panagram("The quick brown fox jumps over the lazy dog")} for argument "The quick brown fox jumps over the lazy dog"')


#Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
def sorted_hyphen(seq):
    split_seq = seq.split("-")
    split_seq.sort()
    joined_seq = "-".join(split_seq)
    return joined_seq

print(f'The sorted_hyphen function returns: {sorted_hyphen("red-green-blue")} for argument "red-green-blue"')


#Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included).
def list_sqrt():
    from math import sqrt
    list_1 = [sqrt(num) for num in range(1, 31)]
    print(f'The list_sqrt function returns: {list_1}')
list_sqrt()


#Write a Python program to execute a string containing Python code.



#Write a Python program to access a function inside a function.



#Write a Python program to detect the number of local variables declared in a function.



# Write a Python program that invokes a function after a specified period of time.
#Sample Output:
#Square root after specific miliseconds:
#4.0
#158.42979517754858
def timeout(num):
    from time import sleep
    from math import sqrt
    
    seconds = 4
    print(f'The square root of {num}, performed after {seconds} seconds, is {sqrt(num)}')
    sleep(seconds)

timeout(4341321)

