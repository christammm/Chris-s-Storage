import random
import sys
import os

__author__ = 'Jabari'

'''
    Multiline comment

'''

# single comment
print("Hello World")

# Variables

name = "Jabari"
print(name)

age = 20

# Main data types, Numbers, Strings, List, Tuples, Dictionaries


# Math operators: + - * / % **(exponent), // (division, no remainder)

print("5  + 2 =", 5 + 2)
print("5  - 2 =", 5 - 2)
print("5  * 2 =", 5 * 2)
print("5  / 2 =", 5 / 2)
print("5  % 2 =", 5 % 2)
print("5  ** 2 =", 5 ** 2)
print("5  // 2 =", 5 // 2)

# ORDER OF OPERATION MATTERS

print("Order of operation matters:")
print("1 + 2 - 3 * 2 = ", 1 + 2 -3 * 2)
print("(1 + 2 - 3) * 2 = ", (1 + 2 -3) * 2)

# Strings

quote = "\"Always use escape characters to use special chars\""

multi_line_quote = '''This String extends
two lines'''

new_string = quote + multi_line_quote

print(quote)
print(multi_line_quote)
print(new_string)

# Formatting print statements
print("%s %s %s" % ('Strings formatted via formatting', quote, multi_line_quote))

# Without new line

print("Stay on this line", end = "")
print("so that I can continue here")

# New line breaks
print("Skip 5 lines via \"\\n * 5\"")
print("\n" * 5)
print("And resume here")

# Lists (Can be of any data type)

grocery_list = ["Juice", "Tomatoes", "Corn"]
print("First item", grocery_list[0])

new_first_item = "Water"
print("Changing first value from %s to %s", grocery_list, new_first_item)
grocery_list[0] = new_first_item
print("first item", grocery_list[0])

# Print subset of a list (End index not included)
print(grocery_list[0:2])

# Store subset of list as string
sub_set = (grocery_list[0:2])

print("subset as string: %s", sub_set)


