"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"""

# testFile = open('test.txt')
# testFile.write('Hey this is dummy text for this file')
# text = testFile.read()
# print(text)


# To open a file for reading it is enough to specify the name of the file:
# f = open("test.txt", 'w')
# f.write("Yes.. this is working")
# f.write("Yes.. still")
# file = open('test.txt', 'w')
# file.write("This is dummy text and yes it is working fine..")


# Using the with statement
# You can also use the with statement when opening a file:
#### using with keyword

with open('test.txt', 'r') as f:
    print(f.read())





# Because "r" for read, and "t" for text are the default values, you do not need to specify them.
# Note: Make sure the file exists, or else you will get an error.

