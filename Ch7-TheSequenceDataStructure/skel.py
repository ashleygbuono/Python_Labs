#!/usr/bin/env python3
from random import randint        # To generate random integers

# Find common elements for a pair of iterators
def find_common_unique_elements( iter1, iter2 ):
    list_with_common = []
    # Do something here to fill up the list
    for iter1_elem in iter1:
        if iter1_elem in iter2 and iter1_elem not in list_with_common:
            list_with_common.append( iter1_elem )

    return list_with_common
# This function calls the above for two lists
# We check if we have at least two lists
def find_common_elems_buncha_iters( buncha_iters ):
    
    # Need to know HOW MANY LISTS we have
    # Pass first two iterables; save common elements
    # How do we access the first two elements of the buncha_iters structure?
    common_elems = find_common_unique_elements(buncha_iters[0], buncha_iters[1])
    
    # Need an expression that ITERATES OVER REMAINING LISTS IN buncha_iters
    
    for an_iter in buncha_iters[2:]:
        common_elems = find_common_unique_elements( common_elems, an_iter )

    # In the block coded above, call find_common_unique_elements with arguments
    # common_elems and the NEXT LIST in the remaining lists in buncha_iters
        #??? = find_common_unique_elements( common_elems, ??? )

    # When done, this has ALL the common elements
    return common_elems

# Generate and return a random list of num_items items
# Each integer between 0 and 15
def gen_return_random_num_list( num_items ) :
    #return a LIST COMPREHENSION that creates a list of
    # num_items random integers between 0 and 20
    
    # The expression        randint(0, 20)      generates a random #
    return [randint(0, 20) for elem in range(0, num_items)]

def main( ):
    # Prompt user for num_iterators and num_each_iterator
    # Remember to coerce user input to an integer!
    num_iterators = int(input('Enter number of iterators (5-10) ==>'))
    num_each_iterator = int(input('Enter number for each iterator (15-20) ==>'))
    # Create buncha_iterator structure
    # Use a LIST COMPREHENSION to create a LIST OF LISTS (buncha_iters)
    # Each list (element) in buncha_iters is a LIST OF RANDOM INTEGERS
    #
    # You'll need to call gen_return_random_num_list, passing num_each_iterator
    # for num_iterators times
    buncha_iters = [gen_return_random_num_list(num_each_iterator) for row in range(0, num_iterators)]
    # Print the buncha_iters generated
    # One list per line - iterate over buncha_iters, print an element
    # Sort the 'per line' list - makes it easier to read
    for elem in buncha_iters:
        elem.sort()

    # OK - let's print out the common elements - this one's a gimme
    print(f'Elements common to all lists: {find_common_elems_buncha_iters( buncha_iters )}')

main()
