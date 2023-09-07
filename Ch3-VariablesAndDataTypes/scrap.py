#IDs change
var1 = 100
var2 = var1
print(f"Id of var1 is {id(var1)} \tId of var2 is {id(var2)}")


var1 = var1 + 100
print(f"Id of var1 is {id(var1)} \tId of var2 is {id(var2)}")




#IDs do not change
list1 = [100]
list2 = list1
print(f"Id of list1 is {id(list1)} \tId of list2 is {id(list2)}")

list2.append(1000)
print(f"Id of list1 is {id(list1)} \tId of list2 is {id(list2)}")


'''
Why this behavior? 
    - Integers are immutable
        - In top example, when we reassign the value of var1 python disposes of the original value in order to attach the newly assigned one
        - The "disposing" is what triggers the change in variable and therefore the change in ID

    - Arrays are mutable
        - Still uses the existing [] structure/object, even if the content inside has changed
'''