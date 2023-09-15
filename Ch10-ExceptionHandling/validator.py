def enter_integer_in_range(prompt, low, high):
    pass

def enter_float_in_range(prompt, low, high):
    pass

def enter_an_integer(prompt):

    while True:
        try:
            entry = int(input(prompt))
            return entry

        except ValueError:        #this could also be TypeError, or Exception as a catch-all
            print(f'Value entered is not an integer -- try again')
            


def enter_a_float(prompt):
    while True:
        try:
            entry = float(input(prompt))
            return entry

        except ValueError:        #this could also be TypeError, or Exception as a catch-all
            print(f'Value entered is not a float -- try again')
            


an_int = enter_a_float("Please enter a decimal number value ==> ")
print(an_int)