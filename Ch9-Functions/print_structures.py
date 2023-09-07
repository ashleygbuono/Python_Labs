#!/usr/bin/env python3

# Part 2: Print the first N elements of a structure
# based on its data type

def print_first_n_set_values( set_tb_printed, num_to_print  ):
    print(f'First {num_to_print} SET values:')
    print(f'  { {list_elem for list_elem in list(set_tb_printed)[:num_to_print]  } }')

def print_first_n_list_values( list_tb_printed, num_to_print ):
    print(f'First {num_to_print} LIST values:')
    print(f'  {[list_elem for list_elem in list_tb_printed[:num_to_print] ] }')

def print_first_n_dict_values(dict_tb_printed, num_to_print):
    print(f'First {num_to_print} DICTIONARY values:')
    num_items = 0
    # There be walrus in the house!
    print( f'  { {key: value for (key, value) in dict_tb_printed.items() if (num_items := num_items + 1) <= num_to_print} }')
    #first_n_values = {key: value for (key, value) in dict_tb_printed.items() if (num_items := num_items + 1) <= num_to_print}
    #print( first_n_values )
# Version 1: Use a dictionary of functions; call the correct
# one based on the argument data type
# If no arg passed print entire structure
def print_first_n_values( structure_tb_printed, num_to_print= "all" ):
    if num_to_print == "all":
        num_to_print = len(structure_tb_printed)
    # Set up dictionary to call appropriate function
    # based on the data type of the structure
    #
    # Accessing set elements same as accessing list elements;
    # Use same function for both
    dict_for_print_structures = { type(list()) :print_first_n_list_values,
                                  type(dict()) :print_first_n_dict_values,
                                  type(set())  :print_first_n_set_values,
                                }
    # call the appropriate helper function
    if type(structure_tb_printed ) in dict_for_print_structures:
       dict_for_print_structures[ type( structure_tb_printed )](structure_tb_printed, num_to_print )
    else:
        print( f'{type(structure_tb_printed)} has no special print function')
#
# Here's a version with if/elsif/else stuff
def print_first_n_values_if_elif( structure_tb_printed, num_to_print='all' ):
    if num_to_print == "all":
        num_to_print = len(structure_tb_printed)
    # Determine type of argument; call appropriate function
    if type( structure_tb_printed ) == type( list() ):
        print_first_n_list_values( structure_tb_printed, num_to_print )
    elif type( structure_tb_printed ) == type( set() ):
        print_first_n_set_values(structure_tb_printed, num_to_print)
    elif type( structure_tb_printed ) == type( dict() ):
        print_first_n_dict_values(structure_tb_printed, num_to_print)
    else:
        print( f'{type(structure_tb_printed)} has no special print function')

# Let's try it out!!!
a_list = [1, 2, 'a', 'b', 4.5, '5']
a_set = {1, 2, 'd', 'll', 23}
a_dict = { 1: "a", 2: "BB", 3: "cc", "X": "Some text"}
a_tuple = (1, 'a', 3)

list_o_structs = [ a_list, a_set, a_dict, a_tuple ]
for a_struct in list_o_structs:
    print_first_n_values( a_struct, 3 )
# Now with default argument
list_o_structs = [ a_list, a_set, a_dict, a_tuple ]
for a_struct in list_o_structs:
    print_first_n_values( a_struct )