# Variables in Python are used to store data values.
# In Python, you do not need to declare the type of variable explicitly.
# The type is inferred from the value assigned to it.
x = 5
print(type(x))

y = "Hello"
print(type(y))

z = 3.14
print(type(z))

print(x + z)
#print(x +y) #TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Static typing vs Dynamic typing
#
# Static typing means that the type of a variable is known at compile time. 
# Meaning that the type of a variable is explicitly declared and cannot change during the execution of the program.
# 
# Dynamic typing means that the type of a variable is known at runtime. 
# Meaning that the type of a variable can change during the execution of the program.
# Dynamic typing allows for more flexibility in programming, but it can also lead to unexpected behavior if the type of a variable changes unexpectedly.

# Static typing Example:
# int x = 5; // x is an integer

# Dynamic typing Example:
x = 5 # x is an integer
print(type(x)) # Output: <class 'int'>

# Dynamic Binding
# Dynamic binding simple example:
x = 5
print(type(x)) # Output: <class 'int'>
x = "Hello"
print(type(x)) # Output: <class 'str'>

# variable declaration and assignment
a = 10 # a is an integer
b = 20.5 # b is a float
c = "Hello" # c is a string

x, y, z = 1, 2.5, "Hello" # multiple variable assignment

print(a, b, c)
print(x, y, z)

d=e=f=30 # multiple variable assignment with same value
print(d, e, f)