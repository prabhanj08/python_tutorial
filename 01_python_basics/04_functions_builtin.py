"""
Python Basics - Functions and Built-in Functions
===============================================

This module covers basic function concepts and Python's built-in functions.
Functions are reusable blocks of code that perform specific tasks, making
programs more organized, readable, and maintainable.

Key Concepts Covered:
- Function definition and calling
- Parameters and arguments
- Return values
- Built-in functions
- Function scope basics
- Common built-in functions usage
"""

# ============================================================================
# 1. FUNCTION BASICS
# ============================================================================

print("Python Functions and Built-in Functions")
print("=" * 40)

# A function is defined using the 'def' keyword
def greet():
    """A simple function that prints a greeting."""
    print("Hello, World!")

# Call the function
print("1. Basic Function:")
greet()

# ============================================================================
# 2. FUNCTIONS WITH PARAMETERS
# ============================================================================

print("\n2. Functions with Parameters:")
print("-" * 30)

def greet_person(name):
    """Function with one parameter."""
    print(f"Hello, {name}!")

def greet_with_title(title, name):
    """Function with multiple parameters."""
    print(f"Hello, {title} {name}!")

# Call functions with arguments
greet_person("Alice")
greet_with_title("Dr.", "Smith")

# ============================================================================
# 3. FUNCTIONS WITH DEFAULT PARAMETERS
# ============================================================================

print("\n3. Default Parameters:")
print("-" * 30)

def greet_with_default(name, greeting="Hello"):
    """Function with default parameter value."""
    print(f"{greeting}, {name}!")

# Call with and without the optional parameter
greet_with_default("Bob")                    # Uses default greeting
greet_with_default("Charlie", "Hi")          # Uses custom greeting
greet_with_default("Diana", greeting="Hey")  # Named argument

# ============================================================================
# 4. FUNCTIONS WITH RETURN VALUES
# ============================================================================

print("\n4. Return Values:")
print("-" * 30)

def add_numbers(a, b):
    """Function that returns the sum of two numbers."""
    return a + b

def get_user_info(name, age):
    """Function that returns multiple values as a tuple."""
    status = "adult" if age >= 18 else "minor"
    return name, age, status

# Use return values
result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# Unpack multiple return values
name, age, status = get_user_info("Emma", 20)
print(f"User: {name}, Age: {age}, Status: {status}")

# ============================================================================
# 5. BUILT-IN FUNCTIONS - BASIC OPERATIONS
# ============================================================================

print("\n5. Built-in Functions - Basic Operations:")
print("-" * 30)

# 5.1 Mathematical functions
numbers = [1, 5, 3, 9, 2]
print(f"Numbers: {numbers}")
print(f"len(): {len(numbers)}")        # Length
print(f"sum(): {sum(numbers)}")        # Sum of all elements
print(f"min(): {min(numbers)}")        # Minimum value
print(f"max(): {max(numbers)}")        # Maximum value
print(f"abs(): {abs(-42)}")            # Absolute value
print(f"round(): {round(3.14159, 2)}") # Round to 2 decimal places

# 5.2 Type checking and conversion (covered earlier, but important)
value = "123"
print(f"\nType functions:")
print(f"type(): {type(value)}")
print(f"isinstance(): {isinstance(value, str)}")

# ============================================================================
# 6. BUILT-IN FUNCTIONS - ITERABLES
# ============================================================================

print("\n6. Built-in Functions for Iterables:")
print("-" * 30)

# 6.1 range() - Generate sequences of numbers
print("range() function:")
print(f"range(5): {list(range(5))}")           # 0 to 4
print(f"range(2, 8): {list(range(2, 8))}")     # 2 to 7
print(f"range(0, 10, 2): {list(range(0, 10, 2))}")  # Even numbers 0 to 8

# 6.2 enumerate() - Get index and value
print(f"\nenumerate() function:")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# 6.3 zip() - Combine multiple iterables
print(f"\nzip() function:")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"  {name} is {age} years old")

# 6.4 sorted() - Sort iterables
print(f"\nsorted() function:")
unsorted_numbers = [3, 1, 4, 1, 5, 9, 2]
print(f"Original: {unsorted_numbers}")
print(f"Sorted: {sorted(unsorted_numbers)}")
print(f"Reverse sorted: {sorted(unsorted_numbers, reverse=True)}")

# ============================================================================
# 7. BUILT-IN FUNCTIONS - FILTERING AND MAPPING
# ============================================================================

print("\n7. Built-in Functions - Filtering and Mapping:")
print("-" * 30)

# 7.1 filter() - Filter elements based on condition
def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(is_even, numbers))
print(f"Original numbers: {numbers}")
print(f"Even numbers: {even_numbers}")

# 7.2 map() - Apply function to all elements
def square(n):
    """Return the square of a number."""
    return n ** 2

squared_numbers = list(map(square, [1, 2, 3, 4, 5]))
print(f"Squared numbers: {squared_numbers}")

# 7.3 all() and any() - Boolean operations on iterables
print(f"\nall() and any() functions:")
bool_list1 = [True, True, True]
bool_list2 = [True, False, True]
bool_list3 = [False, False, False]

print(f"all({bool_list1}): {all(bool_list1)}")  # True if all are True
print(f"all({bool_list2}): {all(bool_list2)}")  # False if any is False
print(f"any({bool_list2}): {any(bool_list2)}")  # True if any is True
print(f"any({bool_list3}): {any(bool_list3)}")  # False if all are False

# ============================================================================
# 8. BUILT-IN FUNCTIONS - STRING AND INPUT/OUTPUT
# ============================================================================

print("\n8. String and I/O Functions:")
print("-" * 30)

# 8.1 String functions
text = "  Hello, World!  "
print(f"Original: '{text}'")
print(f"strip(): '{text.strip()}'")           # Remove whitespace
print(f"upper(): '{text.upper()}'")           # Convert to uppercase
print(f"lower(): '{text.lower()}'")           # Convert to lowercase
print(f"replace(): '{text.replace('World', 'Python')}'")  # Replace substring

# 8.2 chr() and ord() - Character/ASCII conversion
print(f"\nCharacter functions:")
print(f"chr(65): '{chr(65)}'")    # ASCII code to character
print(f"ord('A'): {ord('A')}")    # Character to ASCII code

# 8.3 print() function variations
print(f"\nprint() function variations:")
print("Hello", "World", sep="-")              # Custom separator
print("Loading", end="...")                   # Custom end character
print(" Done!")                               # Continues on same line

# ============================================================================
# 9. PRACTICAL EXAMPLES WITH FUNCTIONS
# ============================================================================

print("\n9. Practical Examples:")
print("-" * 30)

def calculate_statistics(numbers):
    """Calculate basic statistics for a list of numbers."""
    if not numbers:  # Check if list is empty
        return None
    
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    minimum = min(numbers)
    maximum = max(numbers)
    
    return {
        'count': count,
        'sum': total,
        'average': average,
        'min': minimum,
        'max': maximum
    }

# Test the statistics function
test_numbers = [85, 92, 78, 96, 88, 76, 89, 94]
stats = calculate_statistics(test_numbers)

print(f"Numbers: {test_numbers}")
print(f"Statistics:")
for key, value in stats.items():
    if key == 'average':
        print(f"  {key}: {value:.2f}")
    else:
        print(f"  {key}: {value}")

# ============================================================================
# 10. FUNCTION SCOPE BASICS
# ============================================================================

print("\n10. Function Scope Basics:")
print("-" * 30)

# Global variable
global_var = "I'm global"

def demonstrate_scope():
    """Demonstrate variable scope in functions."""
    # Local variable
    local_var = "I'm local"
    
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")
    
    # Modifying global variable (not recommended)
    global global_var
    global_var = "Modified global"

print(f"Before function call - Global: {global_var}")
demonstrate_scope()
print(f"After function call - Global: {global_var}")

# ============================================================================
# 11. USEFUL BUILT-IN FUNCTIONS FOR DATA PROCESSING
# ============================================================================

print("\n11. Data Processing Functions:")
print("-" * 30)

# 11.1 Working with dictionaries
student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 96}

print("Dictionary processing:")
print(f"Keys: {list(student_grades.keys())}")
print(f"Values: {list(student_grades.values())}")
print(f"Items: {list(student_grades.items())}")

# Find student with highest grade
best_student = max(student_grades, key=student_grades.get)
print(f"Best student: {best_student} with grade {student_grades[best_student]}")

# 11.2 reversed() - Reverse an iterable
print(f"\nreversed() function:")
original_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(original_list))
print(f"Original: {original_list}")
print(f"Reversed: {reversed_list}")

# ============================================================================
# 12. COMBINING FUNCTIONS FOR COMPLEX TASKS
# ============================================================================

print("\n12. Combining Functions:")
print("-" * 30)

def process_text_data(text_list):
    """Process a list of text data using multiple built-in functions."""
    # Filter out empty strings
    non_empty = list(filter(lambda x: x.strip(), text_list))
    
    # Convert to lowercase and strip whitespace
    cleaned = list(map(lambda x: x.strip().lower(), non_empty))
    
    # Sort alphabetically
    sorted_text = sorted(cleaned)
    
    # Get unique items (convert to set and back to list)
    unique_text = list(set(sorted_text))
    
    return {
        'original_count': len(text_list),
        'cleaned_count': len(non_empty),
        'unique_count': len(unique_text),
        'processed_data': unique_text
    }

# Test text processing
sample_text = ["  Apple  ", "banana", "", "Cherry", "apple", "  ", "Banana"]
result = process_text_data(sample_text)

print(f"Original data: {sample_text}")
print(f"Processing results:")
for key, value in result.items():
    print(f"  {key}: {value}")

# ============================================================================
# 13. EXERCISES
# ============================================================================

print(f"\n{'='*50}")
print("EXERCISES - Practice Functions!")
print("="*50)

# Exercise 1: Temperature conversion function
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

print("\nExercise 1: Temperature Conversion")
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f:.1f}°F")

temp_f = 77
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F = {temp_c:.1f}°C")

# Exercise 2: Grade analyzer
def analyze_grades(grades):
    """Analyze a list of grades and return statistics."""
    if not grades:
        return "No grades provided"
    
    # Use built-in functions for analysis
    total_students = len(grades)
    average_grade = sum(grades) / total_students
    highest_grade = max(grades)
    lowest_grade = min(grades)
    
    # Count grades by category
    a_grades = len(list(filter(lambda x: x >= 90, grades)))
    b_grades = len(list(filter(lambda x: 80 <= x < 90, grades)))
    c_grades = len(list(filter(lambda x: 70 <= x < 80, grades)))
    failing = len(list(filter(lambda x: x < 70, grades)))
    
    return {
        'total_students': total_students,
        'average': round(average_grade, 2),
        'highest': highest_grade,
        'lowest': lowest_grade,
        'grade_distribution': {
            'A (90+)': a_grades,
            'B (80-89)': b_grades,
            'C (70-79)': c_grades,
            'F (<70)': failing
        }
    }

print("\nExercise 2: Grade Analysis")
class_grades = [85, 92, 78, 96, 88, 76, 89, 94, 82, 90, 87, 93]
analysis = analyze_grades(class_grades)

print(f"Grades: {sorted(class_grades)}")
print(f"Analysis:")
print(f"  Total students: {analysis['total_students']}")
print(f"  Average: {analysis['average']}")
print(f"  Highest: {analysis['highest']}")
print(f"  Lowest: {analysis['lowest']}")
print(f"  Grade distribution:")
for grade_range, count in analysis['grade_distribution'].items():
    print(f"    {grade_range}: {count} students")

# Exercise 3: Word frequency counter
def count_word_frequency(text):
    """Count frequency of words in text using built-in functions."""
    # Convert to lowercase and split into words
    words = text.lower().split()
    
    # Remove punctuation (simple approach)
    cleaned_words = []
    for word in words:
        cleaned_word = ''.join(filter(str.isalnum, word))
        if cleaned_word:  # Only add non-empty words
            cleaned_words.append(cleaned_word)
    
    # Count frequencies
    word_freq = {}
    for word in cleaned_words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    # Sort by frequency (descending)
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    
    return {
        'total_words': len(cleaned_words),
        'unique_words': len(word_freq),
        'most_common': sorted_words[:5]  # Top 5 most common
    }

print("\nExercise 3: Word Frequency Analysis")
sample_text = "Python is great! Python is powerful. I love Python programming."
freq_analysis = count_word_frequency(sample_text)

print(f"Text: '{sample_text}'")
print(f"Total words: {freq_analysis['total_words']}")
print(f"Unique words: {freq_analysis['unique_words']}")
print(f"Most common words:")
for word, count in freq_analysis['most_common']:
    print(f"  '{word}': {count} times")

print(f"\n{'='*50}")
print("Functions and Built-in Functions - Complete!")
print("Next: Learn about Data Structures")
print("="*50)