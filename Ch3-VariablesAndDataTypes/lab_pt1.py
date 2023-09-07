'''
Part1: Write a Python program that produces the following output:

       A
     A   A
    AAAAAAA
   A       A
  A         A

using ONLY the following values in your print statements:
letter_a = "A" three_spaces = " "
Use string formatting options with the above two values; DO NOT pad with spaces!
You may use EOL characters so your print statements don’t stretch to over 80 characters.

'''

letter_a = "A"
three_spaces = "   "

print(f'{letter_a:^14} \n{three_spaces}{letter_a:>2}{three_spaces}{letter_a:>1} \n{three_spaces:>2}{letter_a:>1}{letter_a}{letter_a}{letter_a}{letter_a}{letter_a}{letter_a}\n{letter_a:>3}{three_spaces}{letter_a:>5}\n{letter_a:>2}{three_spaces}{letter_a:>7}')