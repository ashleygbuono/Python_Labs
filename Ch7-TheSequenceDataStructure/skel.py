#!/usr/bin/env python3
from random import randint           # To generate random integers

# Find common elements for a pair of iterators
def find_common_unique_elements( iter1, iter2 ):
    list_with_common = []
    # Do something here to fill up the list

    return list_with_common
# This function calls the above for two lists
# We check if we have at least two lists
def find_common_elems_buncha_iters( buncha_iters ):
    # Need to know HOW MANY LISTS we have

    # Pass first two iterables; save common elements
    # How do we access the first two elements of the buncha_iters structure?
    common_elems = find_common_unique_elements( ??? )
    # Need an expression that ITERATES OVER REMAINING LISTS IN buncha_iters

    # In the block coded above, call find_common_unique_elements with arguments
    # common_elems and the NEXT LIST in the remaining lists in buncha_iters
        ??? = find_common_unique_elements( common_elems, ??? )

    # When done, this has ALL the common elements
    return common_elems

# Generate and return a random list of num_items items
# Each integer between 0 and 15
def gen_return_random_num_list( num_items ) :
    #return a LIST COMPREHENSION that creates a list of
    # num_items random integers between 0 and 20
    # The expression        randint(0, 20)      generates a random #
    return [ ????? ]

def main( ):
    # Prompt user for num_iterators and num_each_iterator
    # Remember to coerce user input to an integer!
    num_iterators = ???
    num_each_iterator = ???
    # Create buncha_iterator structure
    # Use a LIST COMPREHENSION to create a LIST OF LISTS (buncha_iters)
    # Each list (element) in buncha_iters is a LIST OF RANDOM INTEGERS
    #
    # You'll need to call gen_return_random_num_list, passing num_each_iterator
    # for num_iterators times
    buncha_iters = [ ????? ]
    # Print the buncha_iters generated
    # One list per line - iterate over buuncha_items, print an element
    # Sort the 'per line' list - makes it easier to read


    # OK - let's print out the common elements - this one's a gimme
    print(f'Elements common to all lists: {find_common_elems_buncha_iters( buncha_iters )}')

main()
