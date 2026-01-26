import itertools

days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
days2 = ['1', '2', '3', '4', '5', '6', '7']

# # iter and next

# d = iter(days)
# print(next(d))
# print(next(d))
# print(next(d))

# # enumerate

# for i, d in enumerate(days):
#     print(i, d) 

# # zip

# for i in zip(days, days2):
#     print(i)


# # enumerate and zip

# for i,d in enumerate(zip(days, days2)):
#     print(i, d)


# # itertools zip longest
seq1 = ["a", "b" , "c", "d", "e", "f"]
seq2 = [1,2,3,4]
seq3 = "xyz"
result = itertools.zip_longest(seq1, seq2, seq3, fillvalue="blank")
for r in result:
    print(r)