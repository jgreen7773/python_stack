# 1
# Given a list, write a function that changes all positive numbers in the list to "big".
list_of_positive_and_negative_numbers = [5, -3, 3, -5, -6, 4, 1, 3, -9, -3]
# def biggiesize(inserted_list):
#     for x in range(0, len(inserted_list), 1):
#         if inserted_list[x] > 0:
#             inserted_list[x] = "big"
#     print(inserted_list)

# biggiesize(list_of_positive_and_negative_numbers)


# 2
# Given a list of numbers, create a function to replace the last value with the number of positive values.
# def countpositives(inserted_list):
#     a = 0
#     for x in range(0, len(inserted_list), 1):
#         if inserted_list[x] > 0:
#             a = a + 1
#     inserted_list.pop()
#     inserted_list.append(a)
#     print(inserted_list)

# countpositives(list_of_positive_and_negative_numbers)


# 3
# Create a function that takes a list and returns the sum of all the values in the array.
# def sumtotal(inserted_list):
#     sum = 0
#     for i in range(0, len(inserted_list), 1):
#         # print(inserted_list[i])
#         sum = sum + inserted_list[i]
#     print(inserted_list)
#     print(sum)
#     return sum



# sumtotal(list_of_positive_and_negative_numbers)


# 4
# Create a function that takes a list and returns the average of all the values.
# def average(inserted_list):
#     sum = 0
#     avg = 0
#     for i in range(0, len(inserted_list), 1):
#         sum = sum + inserted_list[i]
#         avg = sum / 2
#     print(inserted_list)
#     print(avg)
#     return avg

# average(list_of_positive_and_negative_numbers)


# 5
# Create a function that takes a list and returns the length of the list
# def length(inserted_list):
#     for i in range(0, len(inserted_list) + 1, 1):
#         length = [i]
#     print(length)

# length(list_of_positive_and_negative_numbers)


# 6
# Create a function that takes a list of numbers and returns the minimum
# value in the list. If the list is empty, have the function return false.
# def minimum(inserted_list):
#     if len(inserted_list) == 0:
#         return False
#     else:
#         min = inserted_list[0]
#         for i in range(0, len(inserted_list), 1):
#             if inserted_list[i] < min:
#                 min = inserted_list[i]
#         print(min)
#         return min


# minimum(list_of_positive_and_negative_numbers)


# 7
# Create a function that takes a list and returns the maximum value in the array.
# If the list is empty, have the function return False.
# def maximum(inserted_list):
#     if len(inserted_list) == 0:
#         return False
#     else:
#         max = inserted_list[0]
#         for i in range(0, len(inserted_list), 1):
#             if inserted_list[i] > max:
#                 max = inserted_list[i]
#         print(max)
#         return max

# maximum(list_of_positive_and_negative_numbers)


# 8
# Create a function that takes a list and returns a dictionary that has the sumTotal,
# average, minimum, maximum, and length of the list.
# def ultimateanalysis(inserted_list):
#     dic = {
#     'sum' : 0,
#     'avg' : 0,
#     'min' : inserted_list[0],
#     'max' : inserted_list[0],
#     'length' : 1
#     }
#     for i in range(0, len(inserted_list), 1):
#         dic['sum'] = dic['sum'] + inserted_list[i]
#         dic['avg'] = dic['sum'] / 2
#         dic['length'] = inserted_list[i]
#         if inserted_list[i] < dic['min']:
#             dic['min'] = inserted_list[i]
#         if inserted_list[i] > dic['max']:
#             dic['max'] = inserted_list[i]
#     print(dic)

new = [1,2,3,4]
# ultimateanalysis(list_of_positive_and_negative_numbers)


# 9
# Create a function takes a list and return that list with the values reversed.
# Do this without creating a second list.
# def reverselist(inserted_list):
#     half = len(inserted_list) / 2
#     beginning = inserted_list[0]
#     end = inserted_list[len(inserted_list) - 1]
#     for i in range(0, len(inserted_list), 1):
#         if inserted_list[i] < half:
#             end = inserted_list[i]
#         elif inserted_list[i] > half:
#             beginning = inserted_list[i]
#     print(inserted_list[i])
#         # inserted_list[len(inserted_list) - 1] = inserted_list[0]

# def reverselist(inserted_list):
#     for i in range(len(inserted_list) / 2, 0, -1):
#         inserted_list.insert(len(inserted_list), [i])
#     for x in range(len(inserted_list) / 2, len(inserted_list) - 1, 1):
#         inserted_list.append([x])
#     print(inserted_list)

def reverselist(inserted_list):
    end = inserted_list[len(inserted_list) - 1]
    for i in range(0, len(inserted_list), 1):
        inserted_list[i] = end
        end = end - 1
    print(inserted_list)

reverselist(new)