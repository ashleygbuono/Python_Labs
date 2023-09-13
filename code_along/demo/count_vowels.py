'''
Count lower-case vowels in input string, enter <your input string here> or <enter> to quit

'''
vowel_list = 'aeiou'

while True:
    vowel_count = 0
    my_string = input("Enter an input string, or hit <enter> to quit: ")
    if my_string == '':
        break
    for a_char in my_string:
        if a_char in vowel_list:
            vowel_count += 1

    print(f'Vowel count of : "{my_string}" = {vowel_count}')



'''
# Enter a string, count the lower case vowels. enter <enter> to quit

vowels = "aeiou"

while True:

    count_me = input("Enter a string or <enter> to quit ==> ")

    if len(count_me) == 0:

        break

    lc_vowel_count = 0

    for a_char in vowels:

        lc_vowel_count += count_me.count(a_char)

       

    print(f'Vowel count in "{count_me}" is {lc_vowel_count}')

   

print("All done!")

'''