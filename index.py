# def twoSum(List, target):
#     for (l, index) in List:
#         print(l, index)
#         # if l == target:
#         #     return l
#         # else
    
# twoSum([2,7,11,15], 9)

# a = 7800

# b = 7800

# print(a,b)
# print(id(a))
# print(id(b))


#set method 
# add
# update
# remove
# discard
# union
# intersection
# symmentric_diffrence
# diffrence

# a = {2,3,4,5}
# b = a.discard(8)
# print(b)

# list1 = [1,2,3,6,4,5]
# list2 = [7,8,9,6,4,5]

# newList = list(set(list1).intersection(set(list2)))
# newList.sort()
# print(newList) 

# a = 108
# b = 801

# a += b  #30
# b = a - b #10
# a = a - b #20

# print(a, b) 


# a = 10
# b = 20

# a,b = b,a

# print(a,b)

# my_details = {'name': 'Kuldeep', "number": "1234567890", "class": ["python","php", "SQL"]}

# print(my_details['last_name']?? 'test')

# copy_details = my_details.copy()

# print(id(my_details))
# print(id(copy_details))

# print('z' > 'A')
# print([] < [0])


# a = [1,2,3,'A','B']

# b = sorted(a)
# print(b)

# billAmount = float(input("Please Enter Total Bill Amount : "))

# tip = float(input("Please Enter Tip : "))

# people = int(input("Please Enter Number of People : "))

# splitedAmount = (billAmount + tip )/people 

# print("Splited amount is : ", splitedAmount)


# input1 = int(input("Please Enter First value : "))
# input2 = int(input("Please Enter Second valu : "))


# operation = input("Please Enter The Operation YOu want to performe : ")

# if operation == '+':
#     print(input1 + input2)
# elif operation == '-':
#     print(input1 - input2)
# elif operation == '*':
#     print(input1 * input2)
# elif operation == '/':
#     print(input1 / input2)
# else :
#     print('Please Enter a valid operation')

# count = 1
# value = int(input("Enter a value for : "))
# while count <= 10:
#     print(count * value)
#     count += 1

def testingFcuntion():
    yield 5
    yield 3
    yield 2
    yield 9

values = testingFcuntion()
my_list = []
my_list.extend(values)
print(my_list)
# print(next(values))
# print(next(values))
# values.close()
# print(next(values))
# print(next(values))
for i in values:
    print(i)
