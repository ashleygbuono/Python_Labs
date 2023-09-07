#!/usr/bin/env python3
from validator import enter_integer_in_range, enter_float_in_range, enter_an_integer, enter_a_float

# Call functions in the validator module...
print(enter_integer_in_range("Enter integer between 1 and 5", 1, 5))
print(enter_float_in_range("Enter float between 1.5 and 5.5", 1.5, 5.5))

print(enter_an_integer('Enter integer'))
print(enter_a_float('Enter float'))
