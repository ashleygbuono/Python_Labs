'''
Find elements common to two lists
This wil be used to find common list elements to > 2 lists later on
For now, let's just do two

'''
from random import randint

#Get the number of elements for both lists; ask for a number between 10 and 20
num_in_list = int(input("Enter a number between 10 and 20 ==> "))

#Generate a list of num_in_list random integers between 1 and num_in_list
list_1 = [randint(1, num_in_list) for i in range(num_in_list)]

#Generate another list of num_in_list random integers between 1 and num_in_list
list_2 = [randint(1, num_in_list) for i in range(num_in_list)]

#Find common elements for a pair of iterators. Do not include duplicates.

#Init an empty list to hold the common elements
common_list = []

#Iterate over elements of list_1 (but doesn't matter which list we start with)
# Inside the loop, determine if the element in list_1 is in list_2 AND we did not already find this element
#If so, add the element to the list of common elements
for elem in list_1:
    if elem in list_2 and elem not in common_list:
        common_list.append(elem)


#Print a sorted version of both lists and the list of common elements
list_1.sort()
list_2.sort()
common_list.sort()

print(f'sorted list_1 = {list_1} \n sorted list_2 = {list_2} \n sorted common_list = {common_list}')