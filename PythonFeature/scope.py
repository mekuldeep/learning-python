# x=1

# # Local
# def test():
#     x=10
#     print(x)

# # Global
# # def test():
# #     global x
# #     x=10
# #     print(x)

# print(x)
# test()
# print(x+10)

# nested function create inner scopes, These are called closure

def multiplier(fac):
    def multipy(num):
        return num * fac
    return multipy

doubler = multiplier(2)
tripler = multiplier(3)

print(doubler(10))
print(tripler(10))