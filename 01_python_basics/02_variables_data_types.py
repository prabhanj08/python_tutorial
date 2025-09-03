"""
Python Basics - Variables and Data Types
========================================

This module covers Python's fundamental data types and variable concepts.
Python is dynamically typed, meaning variables can hold different types of data
and their types can change during program execution.

Key Concepts Covered:
- Variable assignment and naming
- Basic data types (int, float, str, bool)
- Type checking and conversion
- Dynamic typing
- Variable scope basics
"""

# ============================================================================
# 1. VARIABLES IN PYTHON
# ============================================================================

# Variables in Python are created when you assign a value to them
# No need to declare the type explicitly - Python infers it

# Variable assignment
name = "Alice"
age = 25
height = 5.6
is_student = True

print("Variable Examples:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is Student: {is_student}")

# ============================================================================
# 2. VARIABLE NAMING RULES AND CONVENTIONS
# ============================================================================

# Valid variable names
user_name = "john_doe"          # Snake case (recommended for variables)
firstName = "John"              # Camel case (less common in Python)
_private_var = "hidden"         # Leading underscore (convention for private)
counter2 = 0                    # Can contain numbers (but not start with them)

# Constants (by convention, use ALL_CAPS)
MAX_USERS = 100
PI = 3.14159
DEFAULT_COLOR = "blue"

print(f"\nVariable naming examples:")
print(f"User name: {user_name}")
print(f"Max users: {MAX_USERS}")

# Invalid variable names (these would cause SyntaxError):
# 2counter = 0        # Cannot start with number
# user-name = "john"  # Cannot contain hyphens
# class = "MyClass"   # Cannot use Python keywords

# ============================================================================
# 3. BASIC DATA TYPES
# ============================================================================

# 3.1 INTEGERS (int)
# Whole numbers, positive or negative, without decimals

positive_int = 42
negative_int = -17
zero = 0
large_int = 1234567890123456789  # Python handles arbitrarily large integers

print(f"\nInteger Examples:")
print(f"Positive: {positive_int}, type: {type(positive_int)}")
print(f"Negative: {negative_int}, type: {type(negative_int)}")
print(f"Large integer: {large_int}")

# Integer operations
a = 10
b = 3
print(f"\nInteger Operations:")
print(f"{a} + {b} = {a + b}")      # Addition
print(f"{a} - {b} = {a - b}")      # Subtraction
print(f"{a} * {b} = {a * b}")      # Multiplication
print(f"{a} / {b} = {a / b}")      # Division (returns float)
print(f"{a} // {b} = {a // b}")    # Floor division (returns int)
print(f"{a} % {b} = {a % b}")      # Modulus (remainder)
print(f"{a} ** {b} = {a ** b}")    # Exponentiation

# ============================================================================
# 3.2 FLOATING-POINT NUMBERS (float)
# ============================================================================

# Numbers with decimal points
price = 19.99
temperature = -5.5
scientific = 1.5e-4  # Scientific notation: 1.5 × 10^-4

print(f"\nFloat Examples:")
print(f"Price: {price}, type: {type(price)}")
print(f"Temperature: {temperature}")
print(f"Scientific notation: {scientific}")

# Float operations
x = 10.5
y = 2.5
print(f"\nFloat Operations:")
print(f"{x} + {y} = {x + y}")
print(f"{x} / {y} = {x / y}")
print(f"Round {x}: {round(x)}")

# Floating-point precision issues
print(f"\nFloating-point precision:")
print(f"0.1 + 0.2 = {0.1 + 0.2}")  # Not exactly 0.3!
print(f"Is 0.1 + 0.2 == 0.3? {0.1 + 0.2 == 0.3}")

# ============================================================================
# 3.3 STRINGS (str)
# ============================================================================

# Text data enclosed in quotes
single_quote = 'Hello, World!'
double_quote = "Python is awesome!"
multiline = """This is a
multiline string
that spans several lines."""

print(f"\nString Examples:")
print(f"Single quotes: {single_quote}")
print(f"Double quotes: {double_quote}")
print(f"Multiline:\n{multiline}")

# String operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Concatenation
print(f"\nString Operations:")
print(f"Full name: {full_name}")
print(f"Length: {len(full_name)}")
print(f"Uppercase: {full_name.upper()}")
print(f"Lowercase: {full_name.lower()}")

# String formatting
age = 30
formatted = f"My name is {full_name} and I am {age} years old."
print(f"F-string formatting: {formatted}")

# String indexing and slicing
text = "Python"
print(f"\nString indexing:")
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")
print(f"Slice [1:4]: {text[1:4]}")

# ============================================================================
# 3.4 BOOLEANS (bool)
# ============================================================================

# True or False values
is_sunny = True
is_raining = False

print(f"\nBoolean Examples:")
print(f"Is sunny: {is_sunny}, type: {type(is_sunny)}")
print(f"Is raining: {is_raining}")

# Boolean operations
print(f"\nBoolean Operations:")
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")

# Comparison operations (return booleans)
num1 = 10
num2 = 20
print(f"\nComparison Operations:")
print(f"{num1} == {num2}: {num1 == num2}")  # Equal
print(f"{num1} != {num2}: {num1 != num2}")  # Not equal
print(f"{num1} < {num2}: {num1 < num2}")    # Less than
print(f"{num1} > {num2}: {num1 > num2}")    # Greater than
print(f"{num1} <= {num2}: {num1 <= num2}")  # Less than or equal
print(f"{num1} >= {num2}: {num1 >= num2}")  # Greater than or equal

# ============================================================================
# 4. TYPE CHECKING AND CONVERSION
# ============================================================================

# Check the type of a variable
value = 42
print(f"\nType Checking:")
print(f"Value: {value}, Type: {type(value)}")
print(f"Is integer? {isinstance(value, int)}")
print(f"Is string? {isinstance(value, str)}")

# Type conversion (casting)
print(f"\nType Conversion:")
num_str = "123"
num_int = int(num_str)          # String to integer
num_float = float(num_str)      # String to float
print(f"String '{num_str}' to int: {num_int}")
print(f"String '{num_str}' to float: {num_float}")

# Convert numbers to strings
number = 456
str_number = str(number)
print(f"Number {number} to string: '{str_number}'")

# Convert to boolean
print(f"\nBoolean Conversion:")
print(f"bool(1): {bool(1)}")        # True
print(f"bool(0): {bool(0)}")        # False
print(f"bool(''): {bool('')}")      # False (empty string)
print(f"bool('hello'): {bool('hello')}")  # True (non-empty string)

# ============================================================================
# 5. DYNAMIC TYPING
# ============================================================================

# Variables can change types during execution
dynamic_var = 42
print(f"\nDynamic Typing:")
print(f"Initial: {dynamic_var}, type: {type(dynamic_var)}")

dynamic_var = "Now I'm a string!"
print(f"Changed: {dynamic_var}, type: {type(dynamic_var)}")

dynamic_var = [1, 2, 3]
print(f"Changed again: {dynamic_var}, type: {type(dynamic_var)}")

# ============================================================================
# 6. MULTIPLE ASSIGNMENT
# ============================================================================

# Assign multiple variables at once
x, y, z = 1, 2, 3
print(f"\nMultiple Assignment:")
print(f"x={x}, y={y}, z={z}")

# Swap variables
a, b = 10, 20
print(f"Before swap: a={a}, b={b}")
a, b = b, a  # Pythonic way to swap
print(f"After swap: a={a}, b={b}")

# Assign same value to multiple variables
p = q = r = 100
print(f"Same value assignment: p={p}, q={q}, r={r}")

# ============================================================================
# 7. CONSTANTS AND NAMING CONVENTIONS
# ============================================================================

# Python doesn't have true constants, but convention is to use ALL_CAPS
MAX_CONNECTIONS = 100
DATABASE_URL = "localhost:5432"
DEBUG_MODE = True

print(f"\nConstants (by convention):")
print(f"Max connections: {MAX_CONNECTIONS}")
print(f"Database URL: {DATABASE_URL}")
print(f"Debug mode: {DEBUG_MODE}")

# ============================================================================
# 8. PRACTICAL EXAMPLES
# ============================================================================

def demonstrate_data_types():
    """Demonstrate various data types in a practical context."""
    
    # User information
    username = "alice_smith"
    user_id = 12345
    account_balance = 1250.75
    is_premium = True
    
    # Display user info
    print(f"\n--- User Information ---")
    print(f"Username: {username}")
    print(f"User ID: {user_id}")
    print(f"Balance: ${account_balance:.2f}")
    print(f"Premium Member: {is_premium}")
    
    # Calculations
    tax_rate = 0.08
    purchase_amount = 100.00
    total_with_tax = purchase_amount * (1 + tax_rate)
    
    print(f"\n--- Purchase Calculation ---")
    print(f"Purchase Amount: ${purchase_amount:.2f}")
    print(f"Tax Rate: {tax_rate * 100}%")
    print(f"Total with Tax: ${total_with_tax:.2f}")
    
    # String manipulation
    welcome_message = f"Welcome back, {username.replace('_', ' ').title()}!"
    print(f"\n--- Welcome Message ---")
    print(welcome_message)

# Call the demonstration function
demonstrate_data_types()

# ============================================================================
# 9. COMMON PITFALLS AND BEST PRACTICES
# ============================================================================

print(f"\n--- Common Pitfalls ---")

# Pitfall 1: Floating-point comparison
print("Pitfall 1: Floating-point comparison")
result = 0.1 + 0.2
print(f"0.1 + 0.2 = {result}")
print(f"Is it equal to 0.3? {result == 0.3}")
print(f"Better comparison: {abs(result - 0.3) < 1e-10}")

# Pitfall 2: Integer division in older Python versions
print("\nPitfall 2: Division behavior")
print(f"10 / 3 = {10 / 3} (float division)")
print(f"10 // 3 = {10 // 3} (floor division)")

# Best Practice: Use descriptive variable names
print("\nBest Practice: Descriptive names")
# Bad
d = 86400
# Good
seconds_per_day = 86400
print(f"Seconds per day: {seconds_per_day}")

# ============================================================================
# EXERCISES
# ============================================================================

print(f"\n{'='*50}")
print("EXERCISES - Try these to practice!")
print("="*50)

# Exercise 1: Variable assignment and type checking
print("\nExercise 1: Create variables of different types")
student_name = "Emma Watson"
student_age = 20
student_gpa = 3.85
is_enrolled = True

print(f"Student: {student_name}")
print(f"Age: {student_age} (type: {type(student_age).__name__})")
print(f"GPA: {student_gpa} (type: {type(student_gpa).__name__})")
print(f"Enrolled: {is_enrolled} (type: {type(is_enrolled).__name__})")

# Exercise 2: Type conversion
print("\nExercise 2: Type conversion practice")
str_number = "42"
converted_int = int(str_number)
converted_float = float(str_number)
print(f"Original: '{str_number}' (type: {type(str_number).__name__})")
print(f"To int: {converted_int} (type: {type(converted_int).__name__})")
print(f"To float: {converted_float} (type: {type(converted_float).__name__})")

# Exercise 3: String operations
print("\nExercise 3: String manipulation")
first = "Python"
second = "Programming"
combined = f"{first} {second}"
print(f"Combined: {combined}")
print(f"Length: {len(combined)}")
print(f"Uppercase: {combined.upper()}")

print(f"\n{'='*50}")
print("Python Variables and Data Types - Complete!")
print("Next: Learn about Control Flow")
print("="*50)