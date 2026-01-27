import pprint
values = ['one', 'two', 'three', 'four', 'five']

print(*values, sep=" -- ")

# for i in range(0, len(values)):
#     print(values[i], end=f"[line {i+1}] \n")


val = {'one': 1, 'Two': 2, 'Three': 3}
print(val)
pprint.pp(val, width=10, indent=5)