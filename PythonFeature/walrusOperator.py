# problem

# userInput = input("Enter a value : ")
# while userInput != 'exit':
#     print(userInput)
#     userInput = input("Enter a value : ")


# solution 
# while (userInput := input("Enter a value : ") != 'exit'):
#     print(userInput)


# usecase-2
# values = [2,4,5,87,94,6,51,7]
# l = len(values)
# s = sum(values)
# var_data = {
#     'length' : l,
#     'total': s,
#     'average': s/l
# }

# solution

values = [2,4,5,87,94,6,51,7]
var_data = {
    'length' : (l := len(values)),
    'total': (s := sum(values)),
    'average': s/l
}



print(var_data)
# pprint.pp(var_data)