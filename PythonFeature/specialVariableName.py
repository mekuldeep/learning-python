import collections

# __name__ is the name of the module
# __name__
print("module name : ", __name__)

# it contains the path of the file from which the module was loaded
# __file__
print("File path : ", __file__)

# indicate the package that the module belongs to
# __package__
print("Package name : ", __package__)
print(collections.__package__)

if __name__ == "__main__":
    print('This code is being load directly')