# Replace several characters in a string with other characters
# E.G. Replace "a" with "AA", "e" with "EE", "i" with "II"

# This string:
# 'This is just a string with chars to be replaced'

# becomes:
# 'Th  II  s   II  s just   AA   str  II  ng w  II  th ch  AA  rs to b  EE   r  EE  pl  AA  c  EE  d'

# When 'i' is replaced by '  II  ', 'e' is replaced by '  EE  ', 'a' is replaced by '  AA  '
# 
# # Replaced chars key:
# a => 4     b =>  8     e => 3    l => 7      s => 5

def replace_chars(str):
    replace_dict = {
        "a": "4",
        "b": "8",
        "e": "3",
        "l": "7",
        "s": "5"
    }
    #Chaining methods
    replaced = str.replace("a", replace_dict["a"]).replace("b", replace_dict["b"]).replace("e", replace_dict["e"]).replace("l", replace_dict["l"]).replace("s", replace_dict["s"])


    #List comprehension
    new_str = "".join([replace_dict["a"] if char == "a" else replace_dict["b"] if char == "b" else replace_dict["e"] if char == "e" else replace_dict["l"] if char == "l" else replace_dict["s"] if char == "s" else char for char in str])

    print(f'{replaced=}')
    print(f'{new_str=}')


replace_chars("this string has very blue chars")