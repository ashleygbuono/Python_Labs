# Display a list of words with their count

# Naah = use an input string. Ask the user for a string to
# use to collect the letter counts
# Convert to lower-case
input_str = input("Enter a string here ==> ").lower()

# Create empty dictionary. The idea is that
# this dictionary has a letter in teh string as a key
# and the count of the letters as a Value
# # You will build the dictionary in the loop below

count_dict = {}

# Iterate over characters in string
# Inside loop if dictionary does not have an entry as that
# character as key, create an entry and assign a value of 1
# else add 1 to the (existing) dictionary entry
for a_char in input_str:
    if not count_dict.get(a_char):
        count_dict.setdefault(a_char, 1)
    else:
        count_dict[a_char] += 1

print(f'{count_dict = }')
# print the resultant dictionary
'''
g occurs 2 times
f occurs 1 times
h occurs 1 times
e occurs 1 times
l occurs 2 times
o occurs 1 times
'''