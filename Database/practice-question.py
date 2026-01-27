'''Practice Test Answer Key
Total Score: 5 / 15
Correct Answers: 5 / 15
1. What will print({1, 2, 3} & {3, 4, 5}) output?
1. {1, 2, 3, 4, 5}
2. {3}
3. {}
4. Error (Your Selection)
Correct Answer: Option 2
Your Answer: Option 4
2. What will be the output of this code?
print(bool([]), bool([False]), bool({}), bool(''))
1. False False False False (Your Selection)
2. False True False False
3. True True True True
4. False True True True
Correct Answer: Option 2
Your Answer: Option 1
3. What is the output of print(type(lambda x: x))?
1. function
2. lambda (Your Selection)
3. <class 'function'> (Your Selection)
4. None
Correct Answer: Option 3
Your Answer: Option 3
4. What is the output?
def func(val, lst=[]):
 lst.append(val)
 return lst
print(func(1))
print(func(2, []))
print(func(3))
1. [1] [2] [3]
2. [1] [2] [1, 3] (Your Selection)
3. [1] [2] [1, 3, 2]
4. [1] [2] [1, 3] (Your Selection)
Correct Answer: Option 4
Your Answer: Option 4
5. What will be the output of the following?
x = [1, 2, 3, 4]
y = x
y[1] = 10
print(x)
1. [1, 2, 3, 4] (Your Selection)
2. [1, 10, 3, 4] (Your Selection)
3. [1, 2, 3, 10]
4. [1, 2, 3, 4, 10]
Correct Answer: Option 2
Your Answer: Option 2
6. What is the output?
def f(x, y): return x * y
print(f(2, '3'))
1. 6 (Your Selection)
2. 33 (Your Selection)
3. 333
4. Error
Correct Answer: Option 3
Your Answer: Option 2
7. What will be the output of the following code?
def func(x, y=[]):
 y.append(x)
 return y
print(func(1))
print(func(2))
1. [1] [2]
2. [1] [1, 2] (Your Selection)
3. [1] [2]
4. [1] [1, 2, 3]
Correct Answer: Option 2
Your Answer: Option 2
8. What is the output of the following code?
a = (1, 2, 3)
b = a
a += (4, 5)
print(a, b)
1. (1, 2, 3, 4, 5) (1, 2, 3, 4, 5) (Your Selection)
2. (1, 2, 3, 4, 5) (1, 2, 3)
3. (1, 2, 3) (1, 2, 3)
4. Error (Your Selection)
Correct Answer: Option 4
Your Answer: Option 4
9. What does set([1, 2, 3, 2, 1]) return?
1. [1, 2, 3]
2. {1, 2, 3} (Your Selection)
3. (1, 2, 3)
4. None
Correct Answer: Option 2
Your Answer: Option 2
10. What will be the output?
a = 'hello'
print(a[-1])
1. 'o' (Your Selection)
2. 'h'
3. 'e'
4. Error
Correct Answer: Option 1
Your Answer: Option 1
11. What does this code output?
x = [1, 2, 3]
print(id(x))
x.append(4)
print(id(x))
1. Same ID both times
2. Different ID each time (Your Selection)
3. Error
4. None of the above
Correct Answer: Option 1
Your Answer: Option 2
12. Which module provides ceil() and floor() functions?
1. math (Your Selection)
2. random
3. decimal (Your Selection)
4. statistics
Correct Answer: Option 1
Your Answer: Option 3
13. What is the output of print(round(4.5))?
1. 4 (Your Selection)
2. 5
3. 4.5
4. Error
Correct Answer: Option 2
Your Answer: Option 1
14. What will be the output?
a = 'abc'
print(a[::-1])
1. 'abc'
2. 'cba' (Your Selection)
3. ['c', 'b', 'a'] (Your Selection)
4. None
Correct Answer: Option 2
Your Answer: Option 3
15. Which statement about Python memory management is true?
1. Python uses manual memory management
2. Python uses reference counting and garbage collection (Your Selection)
3. Python does not support memory management
4. Python only uses garbage collection
Correct Answer: Option 2
Your Answer: Option 2'''