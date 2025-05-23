####################################################################
"""
1- Given a list of numbers, create a function that returns a list where all similar adjacent
        elements have been reduced to a single element, so [1,2,3,3] returns [1,2,3]
Note:
        You may create a new list or modify the passed in list.
"""

arr = [1, 2, 3, 3]


def unique_list(arr: list):
    # return list(set(arr))
    return list(dict.fromkeys(arr))


def unique_list_adjacent(arr: list):
    unique_list = []
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i - 1]:
            unique_list.append(arr[i])
    return unique_list


# print(unique_list_adjacent(arr))
####################################################################

####################################################################
"""
2- Consider dividing a string into two halves  
Case1:  
	The length is even, the front and back halves are the same length. 
Case2: 
	The length is odd, we’ll say that the extra char goes in the front half. 
	E.g. ‘abced’, the front half is ‘abc’, the back half’de. 
"""


def dividing_string(string: str):
    s, e = "", ""
    str_len = len(string)
    med_index = str_len // 2 - 1 if str_len % 2 == 0 else str_len // 2
    s, e = string[: med_index + 1], string[med_index + 1 :]
    return s, e


def dividing_strings(*strings):
    s, e = "", ""
    for string in strings:
        a, b = dividing_string(string)
        print(a, b)
        s, e = s + a, e + b
    print(s, e)
    return s, e


# dividing_strings("jjjjopkp", "ddddmmm", "sdfSDfs")
####################################################################


####################################################################
"""
3- Write a Python function that takes a sequence of numbers and determines  
whether all the numbers are different from each other. 
E.X.
	[1,5,7,9] -> True 
	[2,4,5,5,7,9] -> False
"""

arr = [1, 5, 5, 7, 9]


def is_unique_list(arr: list):
    return len(arr) == len(set(arr))


# print(is_unique_list(arr))

####################################################################

####################################################################
"""
4- Given unordered list, sort it using algorithm bubble sort 
( read about  bubble sort and try to implement it) 
"""


def bubble_sort(arr: list[int]):
    for i in range(len(arr)):
        j = 1
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]


arr = [5, 1, 4, 2, 3, 2, 5, 4, 54, 5443, 435, 34345, 34, 534, 5, 345, 435, 345, 3]
# bubble_sort(arr)
# print(arr)


####################################################################
