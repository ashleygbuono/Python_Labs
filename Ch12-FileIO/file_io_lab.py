import os


# Part 1: Read abespeech.txt, strip newline, print out line numbers and the line backwards

with open('Ch12-FileIO/abespeech.txt') as file_ref:
    for line_no, line in enumerate(file_ref, 1):
        backwards = line[:-1][::-1]
        


# Part 2: Read smedleybutler.txt, copy all lines containing at least
# one word > 9 characters to another file named bigwords.txt

# Get a SET of all sentences that match the criteria.
# There may be duplicate lines - we need to get rid of the dupes!

#Reading file
with open('Ch12-FileIO/smedleybutler.txt') as smedley:
    smedley_set = {a_line for a_line in smedley for a_word in a_line.split(" ") if len(a_word) > 9}

#Writing to file
with open('Ch12-FileIO/bigwords.txt', "w") as big_words:
    big_words.writelines(smedley_set)

os.system('cat Ch12-FileIO/bigwords.txt')

# PART 2 with dictionary (OPTIONAL):

# There may be duplicate lines - we need to get rid of the dupes!
# Get a DICT of all sentences that match the criteria.
# The line is the key (that takes care of the duplicates)
# The long word is the value