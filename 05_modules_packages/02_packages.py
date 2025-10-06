"""
05. Modules and Packages - Creating and Using Packages
=====================================================

A package is a way of structuring Python's module namespace by using "dotted module names".
Packages are directories containing multiple modules with an __init__.py file.

Topics covered:
- What are packages?
- Creating package structure
- __init__.py files and their purpose
- Subpackages and nested packages
- Relative vs absolute imports
- Package distribution basics
"""

import os
import sys
import shutil
from pathlib import Path

print("=" * 60)
print("PYTHON PACKAGES - ORGANIZING MODULES")
print("=" * 60)

# =============================================================================
# 1. UNDERSTANDING PACKAGES
# =============================================================================

print("\n1. UNDERSTANDING PACKAGES")
print("-" * 30)

print("Package vs Module:")
print("- Module: A single .py file")
print("- Package: A directory containing modules with __init__.py")
print("- Subpackage: A package inside another package")

# =============================================================================
# 2. CREATING A SIMPLE PACKAGE STRUCTURE
# =============================================================================

print("\n2. CREATING A SIMPLE PACKAGE STRUCTURE")
print("-" * 30)

# Let's create a sample package structure
package_name = "my_utilities"

# Create the main package directory
if os.path.exists(package_name):
    shutil.rmtree(package_name)

os.makedirs(package_name)
print(f"Created package directory: {package_name}/")

# Create __init__.py (makes it a package)
init_content = '''"""
My Utilities Package
===================

A collection of utility functions for various tasks.
"""

# Package metadata
__version__ = "1.0.0"
__author__ = "Python Learner"

# Import key functions to package level
from .math_utils import add, multiply
from .string_utils import reverse_string, count_vowels

# Package-level variable
PACKAGE_INFO = "My Utilities Package v1.0.0"

print(f"Loaded {PACKAGE_INFO}")
'''

with open(f"{package_name}/__init__.py", "w") as f:
    f.write(init_content)

print(f"Created {package_name}/__init__.py")

# Create math_utils module
math_utils_content = '''"""
Math utilities module
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def power(base, exponent):
    """Calculate base raised to exponent"""
    return base ** exponent

def factorial(n):
    """Calculate factorial of n"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Module constants
PI = 3.14159
E = 2.71828
'''

with open(f"{package_name}/math_utils.py", "w") as f:
    f.write(math_utils_content)

print(f"Created {package_name}/math_utils.py")

# Create string_utils module
string_utils_content = '''"""
String utilities module
"""

def reverse_string(s):
    """Return reversed string"""
    return s[::-1]

def count_vowels(s):
    """Count vowels in string"""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def is_palindrome(s):
    """Check if string is palindrome (ignoring case and spaces)"""
    s = s.lower().replace(' ', '')
    return s == s[::-1]

def capitalize_words(s):
    """Capitalize first letter of each word"""
    return ' '.join(word.capitalize() for word in s.split())

def count_words(s):
    """Count words in string"""
    return len(s.split())
'''

with open(f"{package_name}/string_utils.py", "w") as f:
    f.write(string_utils_content)

print(f"Created {package_name}/string_utils.py")

print(f"\nPackage structure created:")
print(f"{package_name}/")
print(f"├── __init__.py")
print(f"├── math_utils.py")
print(f"└── string_utils.py")

# =============================================================================
# 3. USING THE PACKAGE
# =============================================================================

print("\n3. USING THE PACKAGE")
print("-" * 30)

# Add current directory to Python path so we can import our package
if '.' not in sys.path:
    sys.path.insert(0, '.')

try:
    # Import the entire package
    import my_utilities
    
    print(f"Package info: {my_utilities.PACKAGE_INFO}")
    print(f"Package version: {my_utilities.__version__}")
    
    # Use functions imported at package level
    print(f"Using package-level imports:")
    print(f"add(5, 3) = {my_utilities.add(5, 3)}")
    print(f"multiply(4, 7) = {my_utilities.multiply(4, 7)}")
    print(f"reverse_string('hello') = {my_utilities.reverse_string('hello')}")
    
    # Import specific modules
    from my_utilities import math_utils, string_utils
    
    print(f"\nUsing specific modules:")
    print(f"math_utils.power(2, 3) = {math_utils.power(2, 3)}")
    print(f"string_utils.is_palindrome('racecar') = {string_utils.is_palindrome('racecar')}")
    
    # Import specific functions
    from my_utilities.math_utils import factorial
    from my_utilities.string_utils import capitalize_words
    
    print(f"\nUsing specific functions:")
    print(f"factorial(5) = {factorial(5)}")
    print(f"capitalize_words('hello world') = {capitalize_words('hello world')}")
    
except ImportError as e:
    print(f"Import error: {e}")

# =============================================================================
# 4. CREATING SUBPACKAGES
# =============================================================================

print("\n4. CREATING SUBPACKAGES")
print("-" * 30)

# Create a subpackage for file operations
subpackage_name = f"{package_name}/file_ops"
os.makedirs(subpackage_name)

# Create __init__.py for subpackage
subpackage_init = '''"""
File operations subpackage
"""

from .readers import read_text_file
from .writers import write_text_file

__all__ = ['read_text_file', 'write_text_file']
'''

with open(f"{subpackage_name}/__init__.py", "w") as f:
    f.write(subpackage_init)

# Create readers module
readers_content = '''"""
File reading utilities
"""

def read_text_file(filename):
    """Read text file and return contents"""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"File {filename} not found"
    except Exception as e:
        return f"Error reading file: {e}"

def read_lines(filename):
    """Read file and return list of lines"""
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        return []
    except Exception as e:
        return []
'''

with open(f"{subpackage_name}/readers.py", "w") as f:
    f.write(readers_content)

# Create writers module
writers_content = '''"""
File writing utilities
"""

def write_text_file(filename, content):
    """Write content to text file"""
    try:
        with open(filename, 'w') as f:
            f.write(content)
        return f"Successfully wrote to {filename}"
    except Exception as e:
        return f"Error writing file: {e}"

def append_to_file(filename, content):
    """Append content to text file"""
    try:
        with open(filename, 'a') as f:
            f.write(content)
        return f"Successfully appended to {filename}"
    except Exception as e:
        return f"Error appending to file: {e}"
'''

with open(f"{subpackage_name}/writers.py", "w") as f:
    f.write(writers_content)

print(f"Created subpackage: file_ops/")
print(f"Updated package structure:")
print(f"{package_name}/")
print(f"├── __init__.py")
print(f"├── math_utils.py")
print(f"├── string_utils.py")
print(f"└── file_ops/")
print(f"    ├── __init__.py")
print(f"    ├── readers.py")
print(f"    └── writers.py")

# =============================================================================
# 5. USING SUBPACKAGES
# =============================================================================

print("\n5. USING SUBPACKAGES")
print("-" * 30)

try:
    # Import from subpackage
    from my_utilities.file_ops import read_text_file, write_text_file
    
    # Test file operations
    test_content = "Hello from Python package!\nThis is a test file."
    result = write_text_file("test_file.txt", test_content)
    print(result)
    
    content = read_text_file("test_file.txt")
    print(f"File content: {content}")
    
    # Import specific module from subpackage
    from my_utilities.file_ops import readers
    lines = readers.read_lines("test_file.txt")
    print(f"File lines: {lines}")
    
except ImportError as e:
    print(f"Subpackage import error: {e}")

# =============================================================================
# 6. RELATIVE VS ABSOLUTE IMPORTS
# =============================================================================

print("\n6. RELATIVE VS ABSOLUTE IMPORTS")
print("-" * 30)

print("Import types:")
print("1. Absolute imports: from my_utilities.math_utils import add")
print("2. Relative imports: from .math_utils import add (within package)")
print("3. Relative imports: from ..parent_package import module (up one level)")

# Create an example showing relative imports
relative_example = '''"""
Example of relative imports within a package
"""

# Absolute import (works from anywhere)
from my_utilities.math_utils import add as abs_add

# Relative import (only works within package)
# from .math_utils import multiply as rel_multiply

def demonstrate_imports():
    """Show different import types"""
    result1 = abs_add(10, 20)
    # result2 = rel_multiply(5, 6)  # Would work if this was inside the package
    return result1

# This would be in a module inside the package
'''

with open(f"{package_name}/import_example.py", "w") as f:
    f.write(relative_example)

print("Created import_example.py to demonstrate import types")

# =============================================================================
# 7. PACKAGE INTROSPECTION
# =============================================================================

print("\n7. PACKAGE INTROSPECTION")
print("-" * 30)

try:
    import my_utilities
    
    print(f"Package name: {my_utilities.__name__}")
    print(f"Package file: {my_utilities.__file__}")
    print(f"Package path: {my_utilities.__path__}")
    
    # List package contents
    print(f"Package contents: {dir(my_utilities)}")
    
    # Check if it's a package
    print(f"Is package: {hasattr(my_utilities, '__path__')}")
    
except Exception as e:
    print(f"Introspection error: {e}")

# =============================================================================
# 8. PACKAGE DISTRIBUTION BASICS
# =============================================================================

print("\n8. PACKAGE DISTRIBUTION BASICS")
print("-" * 30)

# Create a basic setup.py file
setup_content = '''"""
Setup script for my_utilities package
"""

from setuptools import setup, find_packages

setup(
    name="my_utilities",
    version="1.0.0",
    author="Python Learner",
    author_email="learner@example.com",
    description="A collection of utility functions",
    long_description="A comprehensive package with math, string, and file utilities",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # List dependencies here
    ],
)
'''

with open("setup.py", "w") as f:
    f.write(setup_content)

print("Created setup.py for package distribution")

# Create MANIFEST.in
manifest_content = '''include README.md
include LICENSE
recursive-include my_utilities *.py
'''

with open("MANIFEST.in", "w") as f:
    f.write(manifest_content)

print("Created MANIFEST.in for including additional files")

# =============================================================================
# EXERCISES
# =============================================================================

print("\n" + "=" * 60)
print("EXERCISES")
print("=" * 60)

print("""
Exercise 1: Create Your Own Package
- Create a package called 'data_tools' with modules:
  - analyzers.py (functions for data analysis)
  - formatters.py (functions for data formatting)
  - validators.py (functions for data validation)
- Include proper __init__.py with package-level imports

Exercise 2: Subpackage Creation
- Add a subpackage 'exporters' to your data_tools package
- Include modules for different export formats (csv, json, xml)
- Test importing from the subpackage

Exercise 3: Package Configuration
- Add configuration options to your package
- Create a config.py module with default settings
- Allow users to override settings

Exercise 4: Package Documentation
- Add comprehensive docstrings to all modules
- Create a README.md for your package
- Document the package structure and usage

Exercise 5: Distribution Preparation
- Create setup.py for your package
- Add proper metadata and dependencies
- Test local installation with pip install -e .
""")

# =============================================================================
# SOLUTIONS (Uncomment to see solutions)
# =============================================================================

print("\n" + "=" * 60)
print("EXERCISE SOLUTIONS")
print("=" * 60)

# Solution 1: Create data_tools package
print("\nSolution 1: Creating data_tools package")

data_tools_package = "data_tools"
if os.path.exists(data_tools_package):
    shutil.rmtree(data_tools_package)

os.makedirs(data_tools_package)

# Create __init__.py
data_tools_init = '''"""
Data Tools Package
================

A package for data analysis, formatting, and validation.
"""

__version__ = "1.0.0"

# Import key functions
from .analyzers import calculate_mean, find_outliers
from .formatters import format_currency, format_percentage
from .validators import is_email, is_phone

__all__ = [
    'calculate_mean', 'find_outliers',
    'format_currency', 'format_percentage',
    'is_email', 'is_phone'
]
'''

with open(f"{data_tools_package}/__init__.py", "w") as f:
    f.write(data_tools_init)

# Create analyzers.py
analyzers_content = '''"""
Data analysis utilities
"""

def calculate_mean(data):
    """Calculate mean of numeric data"""
    return sum(data) / len(data) if data else 0

def find_outliers(data, threshold=2):
    """Find outliers using standard deviation"""
    if len(data) < 2:
        return []
    
    mean = calculate_mean(data)
    std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    
    return [x for x in data if abs(x - mean) > threshold * std_dev]

def calculate_median(data):
    """Calculate median of numeric data"""
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    return sorted_data[n//2]
'''

with open(f"{data_tools_package}/analyzers.py", "w") as f:
    f.write(analyzers_content)

# Create formatters.py
formatters_content = '''"""
Data formatting utilities
"""

def format_currency(amount, currency='$'):
    """Format number as currency"""
    return f"{currency}{amount:,.2f}"

def format_percentage(value, decimals=1):
    """Format decimal as percentage"""
    return f"{value * 100:.{decimals}f}%"

def format_phone(phone):
    """Format phone number"""
    digits = ''.join(filter(str.isdigit, phone))
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return phone

def truncate_string(text, max_length=50):
    """Truncate string with ellipsis"""
    return text[:max_length] + "..." if len(text) > max_length else text
'''

with open(f"{data_tools_package}/formatters.py", "w") as f:
    f.write(formatters_content)

# Create validators.py
validators_content = '''"""
Data validation utilities
"""

import re

def is_email(email):
    """Validate email address"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_phone(phone):
    """Validate phone number"""
    digits = ''.join(filter(str.isdigit, phone))
    return len(digits) == 10

def is_positive_number(value):
    """Check if value is a positive number"""
    try:
        return float(value) > 0
    except (ValueError, TypeError):
        return False

def is_in_range(value, min_val, max_val):
    """Check if value is within range"""
    try:
        num_value = float(value)
        return min_val <= num_value <= max_val
    except (ValueError, TypeError):
        return False
'''

with open(f"{data_tools_package}/validators.py", "w") as f:
    f.write(validators_content)

print(f"Created {data_tools_package} package with analyzers, formatters, and validators")

# Test the package
try:
    import data_tools
    
    # Test analyzers
    test_data = [1, 2, 3, 4, 5, 100]  # 100 is an outlier
    print(f"Mean: {data_tools.calculate_mean(test_data)}")
    print(f"Outliers: {data_tools.find_outliers(test_data)}")
    
    # Test formatters
    print(f"Currency: {data_tools.format_currency(1234.56)}")
    print(f"Percentage: {data_tools.format_percentage(0.1234)}")
    
    # Test validators
    print(f"Valid email: {data_tools.is_email('test@example.com')}")
    print(f"Valid phone: {data_tools.is_phone('123-456-7890')}")
    
except ImportError as e:
    print(f"Could not test data_tools package: {e}")

# Clean up created files and directories
cleanup_items = [
    "my_utilities",
    "data_tools", 
    "setup.py",
    "MANIFEST.in",
    "test_file.txt"
]

print(f"\nCleaning up created files and directories...")
for item in cleanup_items:
    try:
        if os.path.isdir(item):
            shutil.rmtree(item)
        elif os.path.isfile(item):
            os.remove(item)
    except:
        pass

print("\n" + "=" * 60)
print("PACKAGES MODULE COMPLETE!")
print("=" * 60)
print("Key takeaways:")
print("1. Packages organize related modules into directories")
print("2. __init__.py makes a directory a package")
print("3. Subpackages allow hierarchical organization")
print("4. Import functions at package level for easier access")
print("5. Use setup.py for package distribution")
print("6. Relative imports work within packages")