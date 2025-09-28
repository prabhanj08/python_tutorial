"""
Python Functions - Function Basics and Parameters
=================================================

Functions are reusable blocks of code that perform specific tasks. They are
fundamental to writing clean, modular, and maintainable Python code. This module
covers function definition, parameters, arguments, and return values.

Key Concepts Covered:
- Function definition and calling
- Parameters and arguments (positional, keyword, default)
- Return values and multiple returns
- Variable scope (local, global, nonlocal)
- Function documentation with docstrings
- Best practices for function design
"""

# ============================================================================
# 1. BASIC FUNCTION DEFINITION AND CALLING
# ============================================================================

print("Python Functions - Comprehensive Guide")
print("=" * 39)

# 1.1 Simple function definition
print("1. Basic Function Definition:")
print("-" * 28)

def greet():
    """A simple function that prints a greeting."""
    print("Hello, World!")

# Call the function
print("Calling greet():")
greet()

# 1.2 Function with parameters
def greet_person(name):
    """Greet a specific person."""
    print(f"Hello, {name}!")

print("\nCalling greet_person():")
greet_person("Alice")
greet_person("Bob")

# 1.3 Function with multiple parameters
def greet_with_title(title, name):
    """Greet a person with their title."""
    print(f"Hello, {title} {name}!")

print("\nCalling greet_with_title():")
greet_with_title("Dr.", "Smith")
greet_with_title("Ms.", "Johnson")

# ============================================================================
# 2. FUNCTION PARAMETERS AND ARGUMENTS
# ============================================================================

print("\n2. Parameters and Arguments:")
print("-" * 28)

# 2.1 Positional arguments
def calculate_area(length, width):
    """Calculate area of a rectangle."""
    area = length * width
    print(f"Area of {length} x {width} rectangle: {area}")
    return area

print("Positional arguments:")
area1 = calculate_area(5, 3)
area2 = calculate_area(10, 7)

# 2.2 Keyword arguments
print("\nKeyword arguments:")
area3 = calculate_area(length=8, width=4)
area4 = calculate_area(width=6, length=9)  # Order doesn't matter with keywords

# 2.3 Mixed positional and keyword arguments
print("\nMixed arguments:")
area5 = calculate_area(12, width=5)  # Positional first, then keyword

# ============================================================================
# 3. DEFAULT PARAMETERS
# ============================================================================

print("\n3. Default Parameters:")
print("-" * 21)

def greet_with_default(name, greeting="Hello", punctuation="!"):
    """Greet with customizable greeting and punctuation."""
    message = f"{greeting}, {name}{punctuation}"
    print(message)
    return message

print("Using default parameters:")
greet_with_default("Alice")  # Uses defaults
greet_with_default("Bob", "Hi")  # Custom greeting
greet_with_default("Charlie", "Hey", ".")  # Custom greeting and punctuation
greet_with_default("Diana", punctuation="?")  # Skip middle parameter

# 3.1 Mutable default arguments (common pitfall)
print("\nMutable default arguments - AVOID THIS:")

def bad_function(item, my_list=[]):  # DON'T DO THIS!
    """Example of problematic mutable default argument."""
    my_list.append(item)
    return my_list

# This causes problems because the same list is reused
result1 = bad_function("first")
result2 = bad_function("second")
print(f"Result 1: {result1}")  # ['first', 'second'] - unexpected!
print(f"Result 2: {result2}")  # ['first', 'second'] - same list!

# Better approach
def good_function(item, my_list=None):
    """Correct way to handle mutable default arguments."""
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

result3 = good_function("first")
result4 = good_function("second")
print(f"Good result 1: {result3}")  # ['first']
print(f"Good result 2: {result4}")  # ['second']

# ============================================================================
# 4. RETURN VALUES
# ============================================================================

print("\n4. Return Values:")
print("-" * 16)

# 4.1 Functions with return values
def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

def multiply_numbers(a, b):
    """Multiply two numbers and return the result."""
    result = a * b
    return result

print("Functions with return values:")
sum_result = add_numbers(5, 3)
product_result = multiply_numbers(4, 7)
print(f"5 + 3 = {sum_result}")
print(f"4 × 7 = {product_result}")

# 4.2 Multiple return values
def get_name_parts(full_name):
    """Split a full name into first and last name."""
    parts = full_name.split()
    if len(parts) >= 2:
        return parts[0], parts[-1]  # Returns a tuple
    else:
        return parts[0], ""

def calculate_circle_properties(radius):
    """Calculate area and circumference of a circle."""
    import math
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

print("\nMultiple return values:")
first, last = get_name_parts("John Doe Smith")
print(f"First name: {first}, Last name: {last}")

area, circumference = calculate_circle_properties(5)
print(f"Circle (radius 5): Area = {area:.2f}, Circumference = {circumference:.2f}")

# 4.3 Early returns
def check_age_category(age):
    """Categorize age with early returns."""
    if age < 0:
        return "Invalid age"
    
    if age < 13:
        return "Child"
    
    if age < 20:
        return "Teenager"
    
    if age < 65:
        return "Adult"
    
    return "Senior"

print("\nEarly returns:")
ages = [5, 16, 30, 70, -5]
for age in ages:
    category = check_age_category(age)
    print(f"Age {age}: {category}")

# ============================================================================
# 5. VARIABLE SCOPE
# ============================================================================

print("\n5. Variable Scope:")
print("-" * 18)

# 5.1 Global and local scope
global_var = "I'm global"

def demonstrate_scope():
    """Demonstrate local and global variable scope."""
    local_var = "I'm local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")

print("Before function call:")
print(f"Global variable: {global_var}")

demonstrate_scope()

print("After function call:")
print(f"Global variable: {global_var}")
# print(local_var)  # This would cause NameError

# 5.2 Modifying global variables
counter = 0

def increment_counter():
    """Increment global counter."""
    global counter
    counter += 1
    print(f"Counter incremented to: {counter}")

def reset_counter():
    """Reset global counter."""
    global counter
    counter = 0
    print("Counter reset to 0")

print("\nModifying global variables:")
print(f"Initial counter: {counter}")
increment_counter()
increment_counter()
reset_counter()

# 5.3 Nonlocal scope (nested functions)
def outer_function():
    """Demonstrate nonlocal scope with nested functions."""
    outer_var = "I'm in outer function"
    
    def inner_function():
        nonlocal outer_var
        outer_var = "Modified by inner function"
        print(f"Inner function: {outer_var}")
    
    print(f"Before inner call: {outer_var}")
    inner_function()
    print(f"After inner call: {outer_var}")

print("\nNonlocal scope:")
outer_function()

# ============================================================================
# 6. FUNCTION DOCUMENTATION
# ============================================================================

print("\n6. Function Documentation:")
print("-" * 26)

def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI).
    
    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        float: BMI value
        str: BMI category
    
    Example:
        >>> bmi, category = calculate_bmi(70, 1.75)
        >>> print(f"BMI: {bmi:.1f}, Category: {category}")
        BMI: 22.9, Category: Normal weight
    """
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return bmi, category

# Test the documented function
print("BMI Calculator:")
bmi_value, bmi_category = calculate_bmi(70, 1.75)
print(f"BMI: {bmi_value:.1f}, Category: {bmi_category}")

# Access function documentation
print(f"\nFunction docstring:")
print(calculate_bmi.__doc__)

# ============================================================================
# 7. PRACTICAL EXAMPLES
# ============================================================================

print("\n7. Practical Examples:")
print("-" * 22)

# 7.1 Temperature converter
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def convert_temperature(temp, from_unit, to_unit):
    """Convert temperature between Celsius and Fahrenheit."""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit == to_unit:
        return temp
    
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return celsius_to_fahrenheit(temp)
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return fahrenheit_to_celsius(temp)
    else:
        raise ValueError("Unsupported temperature units")

print("Temperature Converter:")
temp_c = 25
temp_f = convert_temperature(temp_c, "celsius", "fahrenheit")
print(f"{temp_c}°C = {temp_f:.1f}°F")

temp_f = 77
temp_c = convert_temperature(temp_f, "fahrenheit", "celsius")
print(f"{temp_f}°F = {temp_c:.1f}°C")

# 7.2 Password validator
def validate_password(password, min_length=8):
    """
    Validate password strength.
    
    Args:
        password (str): Password to validate
        min_length (int): Minimum required length
    
    Returns:
        tuple: (is_valid, list_of_issues)
    """
    issues = []
    
    if len(password) < min_length:
        issues.append(f"Password must be at least {min_length} characters long")
    
    if not any(c.islower() for c in password):
        issues.append("Password must contain at least one lowercase letter")
    
    if not any(c.isupper() for c in password):
        issues.append("Password must contain at least one uppercase letter")
    
    if not any(c.isdigit() for c in password):
        issues.append("Password must contain at least one digit")
    
    if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        issues.append("Password must contain at least one special character")
    
    return len(issues) == 0, issues

print("\nPassword Validator:")
test_passwords = ["weak", "StrongPass123!", "NoSpecial123", "noUPPER123!"]

for pwd in test_passwords:
    is_valid, issues = validate_password(pwd)
    print(f"Password '{pwd}': {'Valid' if is_valid else 'Invalid'}")
    if issues:
        for issue in issues:
            print(f"  - {issue}")

# ============================================================================
# 8. FUNCTION DESIGN BEST PRACTICES
# ============================================================================

print("\n8. Best Practices:")
print("-" * 17)

# 8.1 Single Responsibility Principle
def calculate_tax(income, tax_rate):
    """Calculate tax amount - does one thing well."""
    return income * tax_rate

def format_currency(amount):
    """Format amount as currency - separate concern."""
    return f"${amount:.2f}"

def display_tax_info(income, tax_rate):
    """Display tax information - combines other functions."""
    tax_amount = calculate_tax(income, tax_rate)
    formatted_income = format_currency(income)
    formatted_tax = format_currency(tax_amount)
    
    print(f"Income: {formatted_income}")
    print(f"Tax ({tax_rate:.1%}): {formatted_tax}")
    print(f"After tax: {format_currency(income - tax_amount)}")

print("Single Responsibility Example:")
display_tax_info(50000, 0.25)

# 8.2 Pure functions (no side effects)
def pure_function(x, y):
    """Pure function - same input always gives same output."""
    return x * 2 + y

def impure_function(x):
    """Impure function - has side effects."""
    print(f"Processing {x}")  # Side effect: printing
    global counter
    counter += 1  # Side effect: modifying global state
    return x * 2

print(f"\nPure function examples:")
print(f"pure_function(3, 4): {pure_function(3, 4)}")
print(f"pure_function(3, 4): {pure_function(3, 4)}")  # Same result

# ============================================================================
# 9. EXERCISES
# ============================================================================

print(f"\n{'='*50}")
print("EXERCISES - Practice with Functions!")
print("="*50)

# Exercise 1: Calculator functions
def exercise_1():
    """Create a set of calculator functions."""
    print("\nExercise 1: Calculator Functions")
    
    def add(a, b):
        """Add two numbers."""
        return a + b
    
    def subtract(a, b):
        """Subtract second number from first."""
        return a - b
    
    def multiply(a, b):
        """Multiply two numbers."""
        return a * b
    
    def divide(a, b):
        """Divide first number by second."""
        if b == 0:
            return "Error: Division by zero"
        return a / b
    
    def power(base, exponent):
        """Raise base to the power of exponent."""
        return base ** exponent
    
    # Test calculator functions
    operations = [
        (add, 10, 5),
        (subtract, 10, 5),
        (multiply, 10, 5),
        (divide, 10, 5),
        (divide, 10, 0),
        (power, 2, 3)
    ]
    
    for func, a, b in operations:
        result = func(a, b)
        print(f"{func.__name__}({a}, {b}) = {result}")

exercise_1()

# Exercise 2: Text processing functions
def exercise_2():
    """Create text processing functions."""
    print("\nExercise 2: Text Processing Functions")
    
    def count_words(text):
        """Count words in text."""
        return len(text.split())
    
    def count_characters(text, include_spaces=True):
        """Count characters in text."""
        if include_spaces:
            return len(text)
        else:
            return len(text.replace(" ", ""))
    
    def reverse_words(text):
        """Reverse the order of words in text."""
        return " ".join(text.split()[::-1])
    
    def capitalize_words(text):
        """Capitalize first letter of each word."""
        return " ".join(word.capitalize() for word in text.split())
    
    def get_text_stats(text):
        """Get comprehensive text statistics."""
        return {
            "word_count": count_words(text),
            "char_count": count_characters(text),
            "char_count_no_spaces": count_characters(text, False),
            "sentence_count": text.count('.') + text.count('!') + text.count('?')
        }
    
    # Test text processing functions
    sample_text = "python is a powerful programming language"
    
    print(f"Original text: '{sample_text}'")
    print(f"Word count: {count_words(sample_text)}")
    print(f"Character count: {count_characters(sample_text)}")
    print(f"Reversed words: '{reverse_words(sample_text)}'")
    print(f"Capitalized: '{capitalize_words(sample_text)}'")
    
    stats = get_text_stats(sample_text)
    print(f"Text statistics: {stats}")

exercise_2()

# Exercise 3: Grade management system
def exercise_3():
    """Create a grade management system with functions."""
    print("\nExercise 3: Grade Management System")
    
    def calculate_average(grades):
        """Calculate average of grades."""
        if not grades:
            return 0
        return sum(grades) / len(grades)
    
    def get_letter_grade(average):
        """Convert numeric average to letter grade."""
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'
    
    def analyze_grades(student_name, grades):
        """Analyze student grades and return comprehensive report."""
        if not grades:
            return f"No grades available for {student_name}"
        
        average = calculate_average(grades)
        letter_grade = get_letter_grade(average)
        highest = max(grades)
        lowest = min(grades)
        
        return {
            "name": student_name,
            "grades": grades,
            "average": round(average, 2),
            "letter_grade": letter_grade,
            "highest": highest,
            "lowest": lowest,
            "total_assignments": len(grades)
        }
    
    # Test grade management system
    students = [
        ("Alice", [85, 92, 78, 96, 88]),
        ("Bob", [76, 84, 91, 79, 87]),
        ("Charlie", [95, 89, 93, 97, 91])
    ]
    
    for name, grades in students:
        report = analyze_grades(name, grades)
        print(f"\nStudent Report for {report['name']}:")
        print(f"  Grades: {report['grades']}")
        print(f"  Average: {report['average']} ({report['letter_grade']})")
        print(f"  Highest: {report['highest']}, Lowest: {report['lowest']}")
        print(f"  Total assignments: {report['total_assignments']}")

exercise_3()

print(f"\n{'='*50}")
print("Function Basics - Complete!")
print("Next: Learn about Advanced Function Concepts")
print("="*50)