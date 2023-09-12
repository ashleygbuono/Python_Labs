'''
Write a program that accepts numeric inputs and adds them to a set.

Hit <enter> when done

After making entries, print the largest, smallest, sum, and average of all elements
'''
from statistics import mean

nums_set = set()
while True:
    num_input = int(input("Enter a numeric value here ==> "))

    nums_set.add(num_input)

    print(f'Current set: {nums_set = }')
    print(f'For this entry, the largest element is {max(nums_set)}, the smallest element is {min(nums_set)}, the sum of set entries is {sum(nums_set)} and the average of all elements is {mean(nums_set)}')