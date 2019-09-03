# 1
# create a function that accepts a number as an input. Return a new list that counts down by one, from the argument given.
def countdown(int):
    new_list1 = []
    for x in range(int, 0, -1):
        new_list1.append([x])
    print(new_list1)

countdown(10)


# 2
# Create a function that will receive a list with two numbers. Print the first value and return the second.
def printreturn(a,b):
    print("print", a)
    return b

printreturn(3,9)


# 3
# Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def firstpluslength(list1):
    r = int(len(list1))
    p = list1[0] + r
    print(p)

sample_list = [5,3,7,2,9]
firstpluslength(sample_list)


# 4
# Write a function that accepts a list and creates a new list containing only the values from the original list
# that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has
# less than 2 elements, have the function return False
def valuesgreaterthansecond(list2):
    new_list2 = []
    if new_list2 < 2:
        return False
    for i in range(0,len(list2),1):
        if list2[i]>(list2[1]):
            new_list2.append(list2[i])
    print(len(new_list2))
    print(new_list2)
    return new_list2


sample_list2 = [8,3,5,2,1,5]
valuesgreaterthansecond(sample_list2)
# 5
# Write a function that accepts two integers as parameters: size and value. The function should create and return
# a list whose length is equal to the given size and whose values are all the given value.
def thislengththatvalue(int1,int2):
    new_list3 = []
    for x in range(0, int1, 1):
        new_list3.append(int2)
    print(new_list3)
    return new_list3


thislengththatvalue(2,11)