# Write a Python program to find all the values in a list is greater than a specified number.
def search(list, value):
    for x in list:
        if value >= x:
            return False
    return True

list =  [1, 2, 3, 4, 5, 6]

value = 1
if(search(list,value)):
    print('YES')
else:
    print('NO')

value = 15
if(search(list,value)):
    print('YES')
else:
    print('NO')

