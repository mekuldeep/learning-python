"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"""

### Simple read the file
# we can pass he number of character in the read method 
file = open('demo.txt', 'r')
# print(file.read(5)) #This will only return 5 character 

#We can also read a file line by line 
# print(file.readline())
# print(file.readlines())

### Simple write in a file this will lcear the complete prev. content of file 
# file  = open("demo.txt", "w")
# file.write("Yup, the file is updated")

### Apeend means add more content in existing file use 'a' for this
# file = open('demo.txt', 'a')
# file.write("i'm learning python")
# file.write("\nthen i'll learn flask")
# file.write("\nthen i'll work on a project")

### IF we write any of the file name with 'w' and 'a' and that file does not exist then they create a new one
# file = open('sample.py', 'a')
# data = '''print('This is file file handling code and if the sample.txt is not exist then this code will create a new one')'''
# file.write(data)

### "r+" help to read and write file this does not truncate the data and
### if we write content using this then this will be overwrite the content from the beginning
# file = open('demo.txt', 'r+')
# file.write('Learn this')
# file.seek(0)
# print(file.read())
# file.close()

### seek() method help to read the file from where we want and currently 
### we have pass 0 in it so this will again start from the starting 
 
 
### w+ when we open a file usign this, this will truncate the compelte file data
# file = open('demo.txt', 'w+')
# print(file.read())
 
### Create a new file and put content in that








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

# with open('test.txt', 'r') as f:
#     print(f.read())
