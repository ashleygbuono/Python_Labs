'''
Part 2: Code a simple menu

Write a program that displays a menu for C (create), R (read), U(update), D(delete) or Q(quit). The output should resemble:
Enter:
    C to create,
    R to read,
    U to update,
    D to delete or
    Q to quit ==> c
Calling CREATE routine.....
Enter:
    C to create,
    R to read,
    U to update,
    D to delete or
    Q to quit ==> t
Your entry T is invalid - try again
Enter:
    C to create,
    R to read,
    U to update,
    D to delete or
    Q to quit ==> r
Calling READ routine.....
Enter:
    C to create,
    R to read,
    U to update,
    D to delete or
    Q to quit ==> q
Exiting program

'''

user_continue = True

while user_continue:
    menu_option = input(
    '\nEnter: \n\t C to create, \n\t R to read, \n\t U to update, \n\t D to delete or \n\t Q to quit ==>'
).lower()
    if menu_option == "q":
        print("Exiting program")
        user_continue = False 
    elif menu_option == "c":
        print("Calling CREATE routine....")
    elif menu_option == "r":
        print("Calling READ routine....")
    elif menu_option == "u":
        print("Calling UPDATE routine....")
    elif menu_option == "d":
        print("Calling DELETE routine....")
    else:
        print("Your entry is invalid. Try again")


