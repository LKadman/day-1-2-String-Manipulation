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

# 3.0 Spaces are important
# Take note of spaces not just within springs but the entire code
# start every code at the beginning of the line to avoid an Indentation Error
# print("Hello Angela")
#  File "main.py", line 34
#    print("Hello Angela")
#    ^
# IndentationError: unexpected indent
# notice the caret sign at the bottom of print

# 4.0 Using Code Intelligence
# Text editors have some helpful features. 
# Using this setting allows the computer to autocomplete functions, provide hints, and prompt you about errors in your code. You will notice a change in color and prompt highlight whenever you hover around the part of the code. 
# Can be turned on or off in settings
# with code intelligence enabled, the computer highlights an error in the code anytime it occurs. This allows you to see any errors while typing the text without the need to execute the code

# 4.0 Common Errors
# Take note as these errors tend to occur often
# i - IndentationError: Space at beginning of code
    #  print("Hello Angela")
  #prompt = 'Unexpected Indent'     
# ii - SyntaxError: Not closing the print statment
    #print("Hello Angela"
  #prompt = 'unexpected EOF while parsing'   
# iii - NameError: Mispelling
    #prnt("Hello Angela")
  #prompt = undefined name 'prnt'     
# iv - IndentationError: Space at beginning of code
    #   print("Hello Angela")
  #prompt = 'Unexpected Indent'  

# 5.0 Fixing Issues
# When errors occur in multiple lines of code, the usually practice will be to 
#    run the code which only shows the first issue
#    find the error in the output
#    fix the error, and run the same sequence until all issues are fixed
# Avoid this by using code intelligence 

#Fix the code below 👇


