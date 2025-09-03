"""
Python Basics - Basic Syntax
============================

This module covers the fundamental syntax rules and conventions in Python.
Python is known for its clean, readable syntax that emphasizes code readability.

Key Concepts Covered:
- Python syntax rules
- Indentation and code blocks
- Comments and documentation
- Python keywords
- Case sensitivity
- Line structure
"""

# ============================================================================
# 1. PYTHON SYNTAX FUNDAMENTALS
# ============================================================================

"""
Python Syntax Rules:
1. Python uses indentation to define code blocks (not braces like other languages)
2. Statements typically end with a newline (no semicolons required)
3. Python is case-sensitive
4. Variables don't need explicit declaration
5. Dynamic typing - variables can change types
"""

# ============================================================================
# 2. INDENTATION - THE HEART OF PYTHON
# ============================================================================

"""
Indentation in Python:
- Python uses indentation (spaces or tabs) to group statements
- Standard is 4 spaces per indentation level
- All lines at the same indentation level belong to the same block
- Mixing tabs and spaces causes IndentationError
"""

# Example of proper indentation
def demonstrate_indentation():
    """Function demonstrating proper indentation."""
    print("This is inside the function")  # 4 spaces indentation
    
    if True:
        print("This is inside the if block")  # 8 spaces indentation
        
        for i in range(3):
            print(f"Loop iteration: {i}")  # 12 spaces indentation
    
    print("Back to function level")  # 4 spaces indentation

# Call the function to see indentation in action
demonstrate_indentation()

# ============================================================================
# 3. COMMENTS AND DOCUMENTATION
# ============================================================================

# Types of Comments in Python:
# 1. Single-line comments: Start with #
# 2. Multi-line comments: Use triple quotes (''' or """)
# 3. Docstrings: Special comments for documenting functions, classes, modules

# This is a single-line comment
print("Hello, World!")  # Comment at the end of a line

"""
This is a multi-line comment.
It can span multiple lines.
Useful for longer explanations.
"""

def example_function():
    """
    This is a docstring.
    It documents what the function does.
    
    Returns:
        str: A greeting message
    """
    return "Hello from the function!"

# ============================================================================
# 4. PYTHON KEYWORDS
# ============================================================================

# Python Keywords (Reserved Words):
# These words have special meaning in Python and cannot be used as variable names.

import keyword

print("Python Keywords:")
print(keyword.kwlist)
print(f"Total keywords: {len(keyword.kwlist)}")

# Examples of keywords in use:
# if, else, elif, for, while, def, class, import, from, as, try, except, etc.

# ============================================================================
# 5. CASE SENSITIVITY
# ============================================================================

# Python is case-sensitive:
# - Variable names, function names, and keywords are case-sensitive
# - 'Variable' and 'variable' are different identifiers

# These are all different variables
name = "John"
Name = "Jane"
NAME = "Bob"

print(f"name: {name}")
print(f"Name: {Name}")
print(f"NAME: {NAME}")

# ============================================================================
# 6. LINE STRUCTURE AND CONTINUATION
# ============================================================================

# Line Structure:
# - Statements typically end with a newline
# - Long lines can be continued using backslash (\)
# - Implicit line continuation inside parentheses, brackets, or braces

# Single line statement
message = "This is a simple statement"

# Line continuation with backslash
long_message = "This is a very long message that " + \
               "continues on the next line"

# Implicit line continuation (preferred method)
fruits = ["apple", "banana", "cherry",
          "date", "elderberry", "fig"]

# Function call with multiple parameters
result = max(10, 20, 30,
            40, 50, 60)

print(f"Long message: {long_message}")
print(f"Fruits: {fruits}")
print(f"Maximum: {result}")

# ============================================================================
# 7. MULTIPLE STATEMENTS ON ONE LINE
# ============================================================================

# Multiple statements can be placed on one line using semicolons,
# but this is generally discouraged for readability.

# Not recommended (poor readability)
x = 1; y = 2; z = 3

# Preferred approach (better readability)
a = 1
b = 2
c = 3

print(f"x={x}, y={y}, z={z}")
print(f"a={a}, b={b}, c={c}")

# ============================================================================
# 8. PYTHON IDENTIFIERS
# ============================================================================

# Identifier Rules:
# - Must start with a letter (a-z, A-Z) or underscore (_)
# - Can contain letters, digits (0-9), and underscores
# - Case-sensitive
# - Cannot be a Python keyword
# - No special characters (@, #, $, %, etc.)

# Valid identifiers
variable_name = "valid"
_private_var = "valid"
Variable2 = "valid"
myVar = "valid"

# Invalid identifiers (these would cause SyntaxError):
# 2variable = "invalid"  # Cannot start with digit
# my-var = "invalid"     # Cannot contain hyphen
# class = "invalid"      # Cannot use keyword

print(f"Valid identifier examples: {variable_name}, {_private_var}")

# ============================================================================
# 9. PYTHON CODING STYLE (PEP 8)
# ============================================================================

# PEP 8 Style Guidelines:
# - Use 4 spaces for indentation
# - Limit lines to 79 characters
# - Use lowercase with underscores for variable and function names
# - Use CamelCase for class names
# - Use UPPERCASE for constants
# - Add blank lines around function and class definitions

# Good style examples
MAX_CONNECTIONS = 100  # Constant
user_name = "john_doe"  # Variable

def calculate_total(price, tax_rate):  # Function
    """Calculate total price including tax."""
    return price * (1 + tax_rate)

class UserAccount:  # Class
    """Represents a user account."""
    pass

# ============================================================================
# 10. PRACTICAL EXAMPLES
# ============================================================================

def syntax_examples():
    """Demonstrate various syntax concepts together."""
    
    # Variable assignment
    greeting = "Hello"
    name = "Python"
    
    # String formatting
    message = f"{greeting}, {name}!"
    
    # Conditional with proper indentation
    if len(message) > 10:
        print("Long message:", message)
    else:
        print("Short message:", message)
    
    # Loop with proper indentation
    for char in "Python":
        if char in "aeiou":
            print(f"Vowel found: {char}")
    
    return message

# Call the example function
result = syntax_examples()
print(f"Function returned: {result}")

# ============================================================================
# EXERCISES
# ============================================================================

# Practice Exercises:
#
# 1. Create a function that demonstrates proper indentation with nested if-else
# 2. Write a multi-line comment explaining what your favorite Python feature is
# 3. Create variables following PEP 8 naming conventions
# 4. Use line continuation to create a long string
# 5. Write a function with a proper docstring
#
# Try these exercises to reinforce your understanding of Python syntax!

# Exercise 1: Nested indentation example
def check_number(num):
    """Check if a number is positive, negative, or zero with nested conditions."""
    if num > 0:
        if num > 100:
            print(f"{num} is a large positive number")
        else:
            print(f"{num} is a small positive number")
    elif num < 0:
        print(f"{num} is negative")
    else:
        print("The number is zero")

# Test the function
check_number(150)
check_number(50)
check_number(-10)
check_number(0)

print("\n" + "="*50)
print("Python Basic Syntax - Complete!")
print("Next: Learn about Variables and Data Types")
print("="*50)