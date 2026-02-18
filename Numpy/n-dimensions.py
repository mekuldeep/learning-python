import numpy as np

# Create array from Python list → np.array()

# 1D array
arr = np.array([1,2,3,4,5])
# print(type(arr))

#2D Array
arr2 = np.array([[1,2,3], [4,5,6]])
# print(arr2)

# 3D Array
arr3 = np.array([
                    [[1,2,3], [4,5,6]],
                    [[7,8,9], [0,4,5]]
                ])

# print(arr3)


"""
Basically 1D = use 1 square bracket
2D = use 2 square brackets
3D = use 3 square brackets
""" 

## Property	Meaning
# ndim	number of dimensions
# shape	size of array
# size	total elements


# print(arr3.ndim)
# print(arr3.shape)
# print(arr3.size)

### Create Arrays with Built-in Functions ⭐

# print(np.zeros((2,3)))
# print(np.ones((2,2)))

# print(np.full((4,4), 7))  

# print(np.arange(0,10))

# print(np.random.rand())

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('2nd element on 1st row: ', arr[0, 1])


# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[4:])


# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[:4])

# arr = np.array([1, 2, 3, 4])

# print(arr[2] + arr[3])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])



