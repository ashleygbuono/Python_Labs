#!/usr/bin/env python3
"""
Create a table of word and letter occurrences in the
Gettysburg address.
The below import brings in a string of the address.

Before counting words, remove punctuation
"""
from string import ascii_lowercase
from getty import abe_talking

# Remove punctuation - not all punct chars included
punct_chars = "\"'.,?!-_"

abe_no_punct = abe_talking
for a_punct_char in punct_chars:
    abe_no_punct = abe_no_punct.replace(a_punct_char, "")

# Need to convert abe_no_punct which is a string into a list of words or the counting stuff
# used in the dictionaries counts 'sub-words' like 'be' in 'before', et. al.
abe_no_punct_list = abe_no_punct.split()

# Good idea to get the unique words...no need to iterate over the same words
# right?
# ALSO convert words to lower-case - don't want separate words for different case
# Might as well sort this list here - as opposed to sorting in the dictionary
# comprehension below...(should be faster - sort of a shorter collection?)
unique_address_words = sorted({a_word.lower() for a_word in abe_no_punct_list})
# Use a dictionary comprehension to count each word
# The count() method in the str class is useful here
# Remember we need to count the words in the list made from
# the original string stripped of punct chars
# BUT we pull the words (keys) from the set of unique strings
word_table = {word: abe_no_punct_list.count(word) for word in unique_address_words}
# Want the first 20 characters of the table to contain the words;
# The next 30 to contain the counts
# Rather than count out spaces we can assign variables and
# use f-string formatting
word_header = "Word"
count_header = "Count"
print(f'{word_header:<20}{count_header:>30}')
for word, word_count in word_table.items():
    print(f'{word:<20}{word_count:>30}')
# Ok - now for the letter count
# We still want a dictionary comprehension
# Use the imported ascii_lowercase from the string nodule
# I'll clue students in on how to use it
letter_table = {letter: abe_no_punct.count(letter) for letter in ascii_lowercase}
letter_header = "Letter"
count_header = "Count"
print(f'{letter_header:<20}{count_header:>30}')
for letter, letter_count in letter_table.items():
    print(f'{letter:<20}{letter_count:>30}')
