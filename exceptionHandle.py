# try:
#     num = int(input("Enter number: "))
#     if num == 8:
#         raise('8 error')
#     print(10/num)
# except ZeroDivisionError:
#     print("this is ZeroDivisionError!")
# except ValueError:
#     print('this is value error')
# except:
#     print("nope this is any another error")
# else:
#     print("Success! No error")  # Runs only if no exception occurs.
    
## 2nd approch
# try:
#     x = int(input('Enter Value : '))
#     print(10/x)
# except(ZeroDivisionError, ValueError):
#     print('this is error')

"""
# Flow
try → exception? → except  
no exception → else
"""

"""
# finally Block
Always runs, whether error occurs or not.
Used for cleanup (closing files, DB etc.)
"""

# try:
#     x = int(input("Please Enter a Value : "))
#     if x == 8:
#         raise('this is general error')
#     print(10/x)
# except:
#     print("Error")
# else:
#     print('any other error')
# finally:
#     print("Program finished")

    