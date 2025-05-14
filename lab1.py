# 1- Write a Python program which accepts the user's first and last name and print them in
# reverse order with a space between them.
# f_name = input("Enter your first name: ")
# l_name = input("Enter your last name: ")
# print(l_name + " " + f_name)


# 2- Write a Python program that accepts an integer (n) and computes the value of
# n+nn+nnn.
# n = 5
# value = n + (n * 11) + (n * 111)
# print(value)


# 3- Write a Python program to print the following here document.
# Sample string
# :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example

# print(
#     """
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
# """
# )


# 4- Write a Python program to get the volume of a sphere with radius 6.

# import math

# r = 6
# sphere_volume = (4 / 3) * math.pi * (r**3)
# print(sphere_volume)


# 5- Write a Python program that will accept the base and height of a triangle and compute
# the area.

# base,hight = 4,2
# triangle_area = (base * hight) / 2
# print(triangle_area)


# 6- Write a Python program to construct the following pattern, using a nested for loop.
# Search about method
# end=””

# depth = 10
# i = 1
# while depth > 0:
#     if i < depth:
#         for j in range(i):
#             print("*", end=" ")
#         print("")
#         i += 1
#     else:
#         for j in range(depth):
#             print("*", end=" ")
#         print("")
#         depth -= 1


# 7- Write a Python program that accepts a word from the user and reverse it.

# word = input("inter your word: ")
# print(word[::-1])


# 8- Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

# for i in range(7):
#     if i == 3 or i == 6:
#         continue


# 9-Write a Python program to get the Fibonacci series between 0 to 50
# fib_n = 0
# next_n = 1
# while True:
#     print(fib_n)
#     # fib_n, next_n = next_n, fib_n + next_n
#     cn = next_n + fib_n
#     fib_n = next_n
#     next_n = cn
#     if fib_n > 50:
#         break


# 10- Write a Python program that accepts a string and calculate the number of digits and
# letters.

text = "Python3"
letters = 0
digits = 0
for i in text:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1
print("Letters", letters)
print("Digits", digits)
