# Python Fundamentals

A beginner-friendly collection of Python examples covering the core building blocks of the language. Each topic has short, runnable code you can read, run, and modify.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Data Types](#data-types)
3. [Variables](#variables)


---

## Getting Started

**Prerequisites:** Python 3.8 or higher.

Check your version:

```bash
python3 --version
```

## Variables

Variables store values. Python figures out the type automatically.

```python
name = "Asha"
age = 21
height = 5.6
is_student = True

print(name, age, height, is_student)
```

**Naming rules:**
- Start with a letter or underscore, not a number
- Use letters, numbers, and underscores only
- Names are case-sensitive (`age` and `Age` are different)
- Use `snake_case` by convention

---

## Data Types

| Type | Example | Description |
|------|---------|-------------|
| `int` | `10` | Whole numbers |
| `float` | `3.14` | Decimal numbers |
| `str` | `"Hello"` | Text |
| `bool` | `True` | True or False |
| `list` | `[1, 2, 3]` | Ordered, changeable collection |
| `tuple` | `(1, 2, 3)` | Ordered, unchangeable collection |
| `set` | `{1, 2, 3}` | Unordered, unique items |
| `dict` | `{"a": 1}` | Key-value pairs |
| `NoneType` | `None` | Represents "no value" |

```python
x = 10
print(type(x))        # <class 'int'>

# Type conversion
num = int("25")
text = str(100)
decimal = float("3.5")
```

---

## Operators

```python
a, b = 10, 3

# Arithmetic
print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.333...
print(a // b)   # 3  (floor division)
print(a % b)    # 1  (remainder)
print(a ** b)   # 1000 (power)

# Comparison
print(a > b)    # True
print(a == b)   # False
print(a != b)   # True

# Logical
print(a > 5 and b < 5)   # True
print(a < 5 or b < 5)    # True
print(not a > 5)         # False

# Assignment
a += 5          # same as a = a + 5
```

---

## Input and Output

```python
name = input("Enter your name: ")
print("Hello,", name)

# f-strings (recommended)
age = 20
print(f"{name} is {age} years old")

# Input is always a string, so convert when needed
number = int(input("Enter a number: "))
```

---

## Control Statements

### if / elif / else

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

### Ternary expression

```python
status = "Adult" if age >= 18 else "Minor"
```

### match-case (Python 3.10+)

```python
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Other day")
```

---

## Loops

### for loop

```python
for i in range(5):
    print(i)              # 0 1 2 3 4

for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
```

### while loop

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

### Loop control

```python
for i in range(10):
    if i == 3:
        continue          # skip this iteration
    if i == 7:
        break             # exit the loop
    print(i)
```

### Nested loops

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()
```

---

## Data Structures

### Lists

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
fruits.remove("banana")
print(fruits[0])          # apple
print(fruits[-1])         # last item
print(fruits[1:3])        # slicing
```

### Tuples

```python
point = (10, 20)
x, y = point              # unpacking
```

### Sets

```python
unique = {1, 2, 2, 3, 3}
print(unique)             # {1, 2, 3}
```

### Dictionaries

```python
student = {"name": "Asha", "age": 21}
student["grade"] = "A"
print(student["name"])
print(student.get("city", "Unknown"))

for key, value in student.items():
    print(key, value)
```

### Comprehensions

```python
squares = [x ** 2 for x in range(1, 6)]
evens = [x for x in range(10) if x % 2 == 0]
```

---

## Functions

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Asha"))
print(greet("Ravi", "Hi"))


def add(*numbers):
    return sum(numbers)

print(add(1, 2, 3, 4))    # 10


# Lambda (small anonymous function)
square = lambda x: x ** 2
print(square(5))          # 25
```

---

## Error Handling

```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ValueError:
    print("That is not a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("No errors occurred.")
finally:
    print("This always runs.")
```

---

## File Handling

```python
# Write
with open("notes.txt", "w") as file:
    file.write("Hello, Python!\n")

# Read
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

# Append
with open("notes.txt", "a") as file:
    file.write("Another line\n")
```

Using `with` closes the file automatically.

---

## Project Structure

```
.
├── 1_hello.py
├── 2-data_types.py
├── 3-variables.py
└── README.md
```

---

## Resources

- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [Python Documentation](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)

---

## Contributing

Suggestions and improvements are welcome. Open an issue or submit a pull request.

## License

This project is open source.
