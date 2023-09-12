import random

'''
Pick a student name at random. After the student is picked, display the student name, then "Press <enter> for another student".
Grab another student, repeat process until ALL students have been selected.

Ensure that once a student is picked, they cannot be picked again until all the names have been exhausted.

Make a list out of the student names:
    Erin Ashley Janira Shaquille Nate Leonora Val Laura Debbie Jordan Seiku

Shuffle your list using a function in the random module.
Select a student by using a list method that returns and removes that element from the list
    random.shuffle()
    pop()

'''

student_list = "Erin Ashley Janira Shaquille Nate Leonora Val Laura Debbie Jordan Seiku".split(" ")

while len(student_list) != 0:
    random.shuffle(student_list)
    print(f'Selected student is: {student_list.pop()}')
    _ = input("Press <enter> to select another name... ")
        

print("All done!")