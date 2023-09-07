#!/usr/bin/env python3
"""
Create a table of word and letter occurrences in the
Gettysburg address.
The below import brings in a string of the address.

Before counting words, remove punctuation
"""
from string import ascii_lowercase
from getty import abe_talking

def remove_punct( original_string ):
    punct_chars = "\"'.,?!_-"
    punct_chars_removed = original_string
    for a_punct_char in punct_chars:
        punct_chars_removed = punct_chars_removed.replace( a_punct_char, "")

    return punct_chars_removed

# Convert string of non-punctuated chars to a list of words
def convert_string_word_list(no_punct_string):
    return no_punct_string.split()

# Create a dictionary by iterating over key_iterable counting items
# in count_keys_in_iterable
def create_return_count_dictionary( key_iterable, count_keys_in_iterable):
    return {a_key: count_keys_in_iterable.count(a_key) for a_key in key_iterable}

# Print the table
# We kinda know that there are two headers
# and how they are justified, how large their
# fields/columns are, etc.
def print_count_table( headers, dict_to_be_printed):
    # Here's the header
    print(f'{headers[0]:<20}{headers[1]:>30}')
    # Now the line items
    for key, value in dict_to_be_printed.items():
        print(f'{key:<20}{value:>30}')


# Remove punctuation (this should be in the remove_punct function)
abe_no_punct = remove_punct( abe_talking )
# Convert string into list (a one-liner; function really not necessary, but why not?)
abe_no_punct_list = convert_string_word_list(abe_no_punct)
# No function used here....
unique_address_words = sorted( { a_word.lower() for a_word in abe_no_punct_list } )
# Call function to create the count dictionary
word_table = create_return_count_dictionary( unique_address_words, abe_no_punct_list )
# Call a function to do the printing
print_count_table(["Word", "Count"], word_table)
# Call same function to do the letter counting BUT pass string , NOT LIST
letter_table = create_return_count_dictionary( ascii_lowercase, abe_no_punct )
# Call a function to do the printing
print_count_table(["Letter", "Count"], letter_table)
