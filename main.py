# String Manipulation

# This lesson explains how to organise code in a much efficient way

# 1.0 Line Management
# Output multiple lines in a single line of code using (\n) within the code. Note: use a backslash (\) not a frontslash (/)

print('Hello World!')
print('Hello World!')
print('Hello World!')

print('Hello World!\n Hello World!\n  Hello World!')

# Use three quotation marks to run multiple lines in input without the need for the print() function in each line

print('''Hello World 
  Hello World
    Hello World''')

# 2.0 Concatenation
# To combine different strings so that they can be added to another string by using the (+) sign between strings

print("Hello" + "Angela")
# to separate them, add a space after Hello or before Angela - all within each string
print("Hello " + "Angela")
print("Hello" + " Angela")
# or concatenate another string with an empty space (" ") in between the strings
print("Hello" + " " + "Angela")
#Note: If we think of Strings like a 'string' merging several characters together, then concatenation is the merging of several Strings together

#Spaces are important
# Take note of spaces not just within springs but the entire code
# start every code at the beginning of the line to avoid an Indentation Error
# print("Hello Angela")
#  File "main.py", line 34
#    print("Hello Angela")
#    ^
# IndentationError: unexpected indent
# notice the caret sign at the bottom of print


#Fix the code below 👇

#print(Day 1 - String Manipulation")
#print("String Concatenation is done with the "+" sign.")
#  print('e.g. print("Hello " + "world")')
#print(("New lines can be created with a backslash and n.")
