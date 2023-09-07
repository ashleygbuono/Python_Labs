#!/usr/bin/env python3
"""
Read the file 'abespeech.txt' one line at a time
Rearrange the words by length
Write out the rearranged lines to a file 'aberearranged.txt'

Do a bit of type hinting here
"""

from string import punctuation

abe_file = "../../../../TechEd Training (India)/Python Apr18-24 2022/Advanced content delivered this offering/lambda-sorting/abespeech.txt"
abe_rearranged = "abrrearranged.txt"


# Remove the punctuation from the line
def remove_punctuation(a_line: str) -> str:
    return a_line.translate(str.maketrans(punctuation, ' ' * len(punctuation)))


def rearrange_line(a_line: str) -> str:
    # Remove punctuation
    a_line_no_punct = remove_punctuation(a_line)
    # Sort the words by length
    list_words = a_line_no_punct.split(" ")
    # Remove blank words from the list
    list_words = [a_word for a_word in list_words if len(a_word) > 0]
    # Sort the words...
    list_words.sort(key=lambda word: (len(word), str(word)))
    # Back into a string of blank delimited words
    return " ".join(list_words)


with open(abe_file) as abe_in, open(abe_rearranged, "w") as abe_out:
    for a_line in abe_in:
        # Don't want the newline.....
        rearranged_line = rearrange_line(a_line[:-1])
        # OK - write it out
        abe_out.write(rearranged_line + '\n')
