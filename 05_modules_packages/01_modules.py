"""
05. Modules and Packages - Working with Modules
==============================================

A module is a file containing Python definitions and statements. The file name is the module name 
with the suffix .py added. Modules help organize code and promote reusability.

Topics covered:
- What are modules?
- Creating custom modules
- Different ways to import modules
- Built-in modules
- Module search path
- The __name__ == "__main__" pattern
"""

import sys
import os
import math
import random
from datetime import datetime, timedelta
from collections import Counter

print("=" * 60)
print("PYTHON MODULES - ORGANIZING AND REUSING CODE")
print("=" * 60)

# =============================================================================
# 1. UNDERSTANDING MODULES
# =============================================================================

print("\n1. UNDERSTANDING MODULES")
print("-" * 30)

# A module is simply a Python file
# When you import a module, Python executes the entire file

print("Current module name:", __name__)
print("Module file location:", __file__)

# =============================================================================
# 2. BUILT-IN MODULES
# =============================================================================

print("\n2. BUILT-IN MODULES")
print("-" * 30)

# Python comes with many built-in modules
print("Available built-in modules (first 10):")
import builtins
builtin_names = dir(builtins)
print(builtin_names[:10])

# Math module examples
print(f"\nMath module examples:")
print(f"π = {math.pi}")
print(f"e = {math.e}")
print(f"sqrt(16) = {math.sqrt(16)}")
print(f"factorial(5) = {math.factorial(5)}")

# Random module examples
print(f"\nRandom module examples:")
print(f"Random integer 1-10: {random.randint(1, 10)}")
print(f"Random choice from list: {random.choice(['apple', 'banana', 'cherry'])}")

# Datetime module examples
print(f"\nDatetime module examples:")
now = datetime.now()
print(f"Current time: {now}")
print(f"Tomorrow: {now + timedelta(days=1)}")

# =============================================================================
# 3. DIFFERENT IMPORT METHODS
# =============================================================================

print("\n3. DIFFERENT IMPORT METHODS")
print("-" * 30)

# Method 1: Import entire module
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
print(f"Using json module: {json_string}")

# Method 2: Import specific functions
from json import loads, dumps
data_back = loads(json_string)
print(f"Using imported functions: {data_back}")

# Method 3: Import with alias
import json as js
print(f"Using alias: {js.loads(json_string)}")

# Method 4: Import all (not recommended for most cases)
# from math import *  # This imports all functions from math
# print(f"Direct access to pi: {pi}")  # No need for math.pi

# =============================================================================
# 4. MODULE SEARCH PATH
# =============================================================================

print("\n4. MODULE SEARCH PATH")
print("-" * 30)

print("Python searches for modules in these locations:")
for i, path in enumerate(sys.path, 1):
    print(f"{i}. {path}")

# =============================================================================
# 5. CREATING A SIMPLE MODULE (DEMONSTRATION)
# =============================================================================

print("\n5. CREATING A SIMPLE MODULE")
print("-" * 30)

# Let's create a simple module content as a string (normally this would be in a separate file)
module_content = '''
"""
my_math_utils.py - A simple math utilities module
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def factorial(n):
    """Calculate factorial of n"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Module-level variable
PI = 3.14159

# This code runs when module is imported
print("my_math_utils module loaded!")
'''

# Write the module to a file
with open("my_math_utils.py", "w") as f:
    f.write(module_content)

print("Created my_math_utils.py module")

# Now import and use our custom module
try:
    import my_math_utils
    
    print(f"Using custom module:")
    print(f"add(5, 3) = {my_math_utils.add(5, 3)}")
    print(f"multiply(4, 7) = {my_math_utils.multiply(4, 7)}")
    print(f"factorial(5) = {my_math_utils.factorial(5)}")
    print(f"PI constant = {my_math_utils.PI}")
    
except ImportError as e:
    print(f"Could not import custom module: {e}")

# =============================================================================
# 6. MODULE ATTRIBUTES AND INTROSPECTION
# =============================================================================

print("\n6. MODULE ATTRIBUTES AND INTROSPECTION")
print("-" * 30)

# Every module has built-in attributes
print(f"Math module attributes:")
print(f"__name__: {math.__name__}")
print(f"__file__: {math.__file__}")

# List all functions and variables in a module
print(f"\nFunctions in math module (first 10):")
math_functions = [item for item in dir(math) if not item.startswith('_')]
print(math_functions[:10])

# Get help on a module
print(f"\nGetting help on a function:")
help(math.sqrt)

# =============================================================================
# 7. THE __name__ == "__main__" PATTERN
# =============================================================================

print("\n7. THE __name__ == '__main__' PATTERN")
print("-" * 30)

# This pattern allows a module to be both imported and run as a script
print(f"Current __name__ value: {__name__}")

def main():
    """Main function - runs when script is executed directly"""
    print("This script is being run directly!")
    print("Performing main script operations...")

# This is the standard Python idiom
if __name__ == "__main__":
    main()

# =============================================================================
# 8. WORKING WITH MODULE DOCUMENTATION
# =============================================================================

print("\n8. MODULE DOCUMENTATION")
print("-" * 30)

# Modules can have docstrings
print(f"This module's docstring:")
print(__doc__)

# Access function docstrings
print(f"\nrandom.choice docstring:")
print(random.choice.__doc__)

# =============================================================================
# 9. PRACTICAL EXAMPLES
# =============================================================================

print("\n9. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Using collections module
from collections import Counter, defaultdict

text = "hello world hello python world"
word_count = Counter(text.split())
print(f"Word count: {word_count}")

# Example 2: Using os module for system operations
print(f"Current working directory: {os.getcwd()}")
print(f"Environment PATH exists: {'PATH' in os.environ}")

# Example 3: Using sys module for system-specific parameters
print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")

# =============================================================================
# EXERCISES
# =============================================================================

print("\n" + "=" * 60)
print("EXERCISES")
print("=" * 60)

print("""
Exercise 1: Module Exploration
- Import the 'statistics' module
- Use it to calculate mean, median, and mode of [1, 2, 2, 3, 4, 4, 4, 5]
- Print the results

Exercise 2: Custom Module Creation
- Create a module called 'string_utils.py' with functions:
  - reverse_string(s): returns reversed string
  - count_vowels(s): counts vowels in string
  - is_palindrome(s): checks if string is palindrome
- Import and test your module

Exercise 3: Module Introspection
- Import any built-in module of your choice
- List all its attributes using dir()
- Find and use 3 functions from that module
- Print their docstrings

Exercise 4: Import Variations
- Practice all 4 import methods with the 'datetime' module
- Create examples showing when each method is most appropriate

Exercise 5: Module Search Path
- Add a custom directory to sys.path
- Create a module in that directory
- Import and use the module
""")

# =============================================================================
# SOLUTIONS (Uncomment to see solutions)
# =============================================================================

print("\n" + "=" * 60)
print("EXERCISE SOLUTIONS")
print("=" * 60)

# Solution 1: Module Exploration
print("\nSolution 1: Statistics Module")
import statistics
data = [1, 2, 2, 3, 4, 4, 4, 5]
print(f"Data: {data}")
print(f"Mean: {statistics.mean(data)}")
print(f"Median: {statistics.median(data)}")
print(f"Mode: {statistics.mode(data)}")

# Solution 2: Custom Module (create the file)
string_utils_content = '''
def reverse_string(s):
    """Return reversed string"""
    return s[::-1]

def count_vowels(s):
    """Count vowels in string"""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def is_palindrome(s):
    """Check if string is palindrome"""
    s = s.lower().replace(' ', '')
    return s == s[::-1]
'''

with open("string_utils.py", "w") as f:
    f.write(string_utils_content)

print("\nSolution 2: Custom String Utils Module")
try:
    import string_utils
    test_string = "A man a plan a canal Panama"
    print(f"Original: {test_string}")
    print(f"Reversed: {string_utils.reverse_string(test_string)}")
    print(f"Vowel count: {string_utils.count_vowels(test_string)}")
    print(f"Is palindrome: {string_utils.is_palindrome(test_string)}")
except ImportError:
    print("Could not import string_utils module")

# Solution 3: Module Introspection
print("\nSolution 3: Module Introspection (using 'string' module)")
import string
print(f"String module attributes: {len(dir(string))} total")
print(f"Some functions: {[attr for attr in dir(string) if not attr.startswith('_')][:5]}")
print(f"ASCII letters: {string.ascii_letters}")
print(f"Digits: {string.digits}")
print(f"Punctuation: {string.punctuation}")

# Clean up created files
try:
    os.remove("my_math_utils.py")
    os.remove("string_utils.py")
    print("\nCleaned up temporary module files")
except:
    pass

print("\n" + "=" * 60)
print("MODULE COMPLETE!")
print("=" * 60)
print("Key takeaways:")
print("1. Modules organize code and promote reusability")
print("2. Python has many built-in modules for common tasks")
print("3. Multiple import methods serve different purposes")
print("4. Use __name__ == '__main__' for executable modules")
print("5. Module introspection helps understand available functionality")