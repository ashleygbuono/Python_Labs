#!/usr/bin/env python3
from string import ascii_lowercase
from getty import abe_talking
"""
Create a table of word and letter occurrences in the
Gettysburg address.
'import getty' brings in a string of the address.

Before counting words, remove punctuation
We'll do sorting, removing duplicates along the way
"""
# Use an import from the Python standard library that
# is a string of lower-case characters
# (yes - not difficult to type 'abc...' but there is something out there already!)

# Remove punctuation - not all punct chars included
# Assign the original string (abe_talking) to another string
# (abe_no_punct)


# Need to convert abe_no_punct which is a string into a list of words or the counting stuff
# used in the dictionaries counts 'sub-words' like 'be' in 'before', et. al.
# Might as well assign the list of words to abe_no_punct


# Iterate over each character in punct_chars using
# a string method to REPLACE the punct char with an
# empty string ('') and assign the replaced punct char string
# to itself. Idea is each time you remove a punct char you
# reassign the 'cleaner' string to itself so the effect is
# cumulative
punct_chars = "\"'.,?!_-"

# Code here to strip the punctuation from the original string
# and save the stripped string for later use

# Convert string to a list of words using split()

# Eventually you'll be iterating over the words in the punct-removed
# list of words created above, counting the words...
# The punct-removed list of words has duplicate words. When you iterate over
# these words, there's no use in counting the same words several times.
# Ergo, why not get the unique words in the no-punct list of words, ITERATE OVER
# THOSE WORDS but COUNT the words in the punct-removed list of words?
# ALSO convert words to lower-case - don't want separate words for different case
# Might as well sort this list here - as opposed to sorting a longer list of words that
# will contain duplicates in the punct-removed string.
#
# The sorting, converting to lower case and saving only unique words
# MAY BE DONE WITH ONE LINE OF CODE (feel free to use more, but...)

# Code that stuff here

# Time to create the table of words and word counts.
# Need a way of creating key/value pairs such that the
# KEY IS A UNIQUE WORD and the VALUE IS THE # TIMES UNIQUE
# WORD IS IN THE NO-PUNCT STRING (gonna be a dictionary, right?)
#
# Iterate over the UNIQUE WORD; COUNT the UNIQUE WORD in
# the no-punct string
#
# The dictionary creation and count may be
# CODED IN ONE LINE (usual disclaimer goes here...)

# Code dictionary creation with counting here


# Let's print them out....
# Want the first 20 characters of the table to
# contain the words left-justified;
# The next 30 to contain the counts right-justified.
# It'll look something like this:
'''
Word                                         Count
a                                              102
above                                            1
add                                              1
                *** Whole lotta words ***
work                                             1
world                                            1
years                                            1
'''
# Note how the headers are lined up with the words
# Recall there's a dictionary function that creates
# an ITERABLE of KEY/VALUE PAIRS
# Iterate over this iterable and print out a dictionary
# entry properly formatted
# Note the header is lined up as well
# Should take about 4-5 lines, depending

# Print out the word count table here


# Ok - now for the letter count
# We have a string imported above that contains the lower-case letters
# Iterate over this letter collection and count how many occurrences
# of the letter are in the no-punct string
# The ONE LINE (or whatever code you used) to do this is remarkably similar
# to that used for the word count (which makes sense - still counting
# characters in a sequence (which a string is))

# Code that here.....

# Print the letter/count table using code frighteningly similar
# to that used to print the word count table

# Do that here....

