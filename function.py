def getLength(list):
    print(len(list))

cities = ['bikaner', 'jaipur', 'jodhpur', 'jaisalmer']

## Lambda function
## Example 1
# sum = lambda a,b: a+b
# print(sum(2,4))


## Example 2
# nums = [1,2,3,4,5]
# mul = list(map(lambda x: x*2, nums))

# print(add)


### Practice Question


#  - WAF to print the length of list.
# def findLength(a):
#     print(len(a))
    
# a = [1,2,3,4,5,6,7]
# findLength(a)

#  - WAF to print the element of a list in a single line.

# def printInOneLine(a):
#     for x in a:
#         print(x, end=" ")

# a = [1,2,3,4,5,6,7]
# printInOneLine(a)

#  - WAF to find the fatorial of n 

# def findFac(n):
#     fact = 1
#     for x in range(1, n+1):
#         fact *= x
#     print(fact)
    
# findFac(6)


#  - WAF to convert USD To INR

# current USD value is 92

# def converter(usd_val):
#     currentUsdValue = 92
#     print(f"{usd_val} USD = {usd_val * currentUsdValue} INR")
# converter(5)


#### Function Recursion

## write a recursive function to calculate the sum of first n natural numbers

# def calcu_sum(val):
#     if val == 1:
#         return 1
#     return val + calcu_sum(val-1)

# print(calcu_sum(10))


## Write a recursive funciton to print all elements in a list.
# Hint use list and index as parameters


def print_list(animals, index = 0):
    if index == len(animals):
        return
    print(animals[index])
    print_list(animals, index+1)

animals = ["cat", "dog", "cow", "bull", "elephant"]
print_list(animals)

