# Data Types in python

#String- There is no character data type in python. 
#A single character is also considered as a string of length 1. 
#Strings are immutable in python.
print("Hello World")

#Integer - Represents whole numbers
print(308)
print(1e308)

#Float - Represents decimal numbers
print(3.14)
print(1.2e308)

#Complex numbers in python
#Complex numbers are represented as a + bj, where a is the real part and b is the imaginary part.
print(1 + 2j)

#Boolean - Represents true or false values
print(True)
print(False)

#List - Represents a collection of values.
#Lists are mutable in python.
print([1, 2, 3, 4, 5])

#Tuple - Represents a collection of values.
#Tuples are immutable in python.
print((1, 2, 3, 4, 5))

#Set - Represents a collection of unique values.
#Sets are mutable in python.
print({1, 2, 3, 4, 5})

#Dictionary - Represents a collection of key-value pairs.
#Dictionaries are mutable in python.
print({"name": "John", "age": 30, "city": "New York"})

#None - Represents the absence of a value.
print(None)


#String formatting in python
name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age))


#type() function in python, is used to get the data type of a variable or value.
print(type(5))
print(type(30.5))
print(type("Hello"))
print(type(True))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({1, 2, 3}))
print(type({"name": "John", "age": 30}))

#f-strings in python, is a way to format strings using expressions inside curly braces {}.
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")

