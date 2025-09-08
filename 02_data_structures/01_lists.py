"""
Python Data Structures - Lists
==============================

Lists are one of the most versatile and commonly used data structures in Python.
They are ordered, mutable collections that can store items of different data types.
Lists are perfect for storing sequences of related data.

Key Concepts Covered:
- List creation and initialization
- Accessing and modifying list elements
- List methods and operations
- List comprehensions
- Nested lists
- Common list patterns and use cases


"""

# ============================================================================
# 1. CREATING LISTS
# ============================================================================

print("Python Lists - Comprehensive Guide")
print("=" * 35)

# 1.1 Different ways to create lists
print("1. Creating Lists:")
print("-" * 20)

# Empty list
empty_list = []
empty_list2 = list()

# List with initial values
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry", "date"]
mixed_list = [1, "hello", 3.14, True, None]

# List from other iterables
string_to_list = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']
range_to_list = list(range(5))   # [0, 1, 2, 3, 4]

print(f"Empty list: {empty_list}")
print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed types: {mixed_list}")
print(f"From string: {string_to_list}")
print(f"From range: {range_to_list}")

# ============================================================================
# 2. ACCESSING LIST ELEMENTS
# ============================================================================

print("\n2. Accessing List Elements:")
print("-" * 30)

colors = ["red", "green", "blue", "yellow", "purple"]

# Positive indexing (0-based)
print(f"Colors list: {colors}")
print(f"First element (index 0): {colors[0]}")
print(f"Second element (index 1): {colors[1]}")
print(f"Last element (index {len(colors)-1}): {colors[len(colors)-1]}")

# Negative indexing (from the end)
print(f"Last element (index -1): {colors[-1]}")
print(f"Second to last (index -2): {colors[-2]}")

# List slicing [start:end:step]
print(f"\nSlicing examples:")
print(f"First three: {colors[:3]}")           # [start:end]
print(f"Last two: {colors[-2:]}")             # [start:]
print(f"Middle elements: {colors[1:4]}")      # [start:end]
print(f"Every second element: {colors[::2]}")  # [::step]
print(f"Reversed list: {colors[::-1]}")       # [::negative_step]

# ============================================================================
# 3. MODIFYING LISTS
# ============================================================================

print("\n3. Modifying Lists:")
print("-" * 20)

# Lists are mutable - we can change their contents
shopping_list = ["milk", "bread", "eggs"]
print(f"Original shopping list: {shopping_list}")

# Changing individual elements
shopping_list[0] = "almond milk"
print(f"After changing first item: {shopping_list}")

# Changing multiple elements with slicing
shopping_list[1:3] = ["whole grain bread", "organic eggs", "cheese"]
print(f"After changing multiple items: {shopping_list}")

# ============================================================================
# 4. LIST METHODS - ADDING ELEMENTS
# ============================================================================

print("\n4. Adding Elements to Lists:")
print("-" * 30)

# 4.1 append() - Add single element to the end
numbers = [1, 2, 3]
print(f"Original: {numbers}")

numbers.append(4)
print(f"After append(4): {numbers}")

numbers.append([5, 6])  # Adds the entire list as one element
print(f"After append([5, 6]): {numbers}")

# 4.2 extend() - Add multiple elements to the end
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(f"After extend([4, 5, 6]): {numbers}")

numbers.extend("abc")  # Extends with each character
print(f"After extend('abc'): {numbers}")

# 4.3 insert() - Add element at specific position
fruits = ["apple", "cherry"]
fruits.insert(1, "banana")  # Insert at index 1
print(f"After insert(1, 'banana'): {fruits}")

# ============================================================================
# 5. LIST METHODS - REMOVING ELEMENTS
# ============================================================================

print("\n5. Removing Elements from Lists:")
print("-" * 35)

# 5.1 remove() - Remove first occurrence of value
animals = ["cat", "dog", "bird", "cat", "fish"]
print(f"Original: {animals}")

animals.remove("cat")  # Removes first "cat"
print(f"After remove('cat'): {animals}")

# 5.2 pop() - Remove and return element at index (default: last)
removed_animal = animals.pop()  # Remove last element
print(f"Popped element: {removed_animal}")
print(f"After pop(): {animals}")

removed_first = animals.pop(0)  # Remove first element
print(f"Popped first element: {removed_first}")
print(f"After pop(0): {animals}")

# 5.3 clear() - Remove all elements
test_list = [1, 2, 3, 4, 5]
print(f"Before clear(): {test_list}")
test_list.clear()
print(f"After clear(): {test_list}")

# 5.4 del statement - Remove elements or slices
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original: {numbers}")

del numbers[0]      # Delete first element
print(f"After del numbers[0]: {numbers}")

del numbers[2:5]    # Delete slice
print(f"After del numbers[2:5]: {numbers}")

# ============================================================================
# 6. LIST METHODS - SEARCHING AND COUNTING
# ============================================================================

print("\n6. Searching and Counting:")
print("-" * 25)

letters = ["a", "b", "c", "b", "d", "b", "e"]
print(f"Letters: {letters}")

# 6.1 index() - Find index of first occurrence
first_b_index = letters.index("b")
print(f"First 'b' at index: {first_b_index}")

# Find 'b' starting from index 2
second_b_index = letters.index("b", 2)
print(f"Next 'b' from index 2: {second_b_index}")

# 6.2 count() - Count occurrences
b_count = letters.count("b")
print(f"Number of 'b's: {b_count}")

# 6.3 in operator - Check if element exists
print(f"'c' in letters: {'c' in letters}")
print(f"'z' in letters: {'z' in letters}")

# ============================================================================
# 7. LIST METHODS - SORTING AND REVERSING
# ============================================================================

print("\n7. Sorting and Reversing:")
print("-" * 25)

# 7.1 sort() - Sort list in place
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original numbers: {numbers}")

numbers.sort()
print(f"After sort(): {numbers}")

numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")

# 7.2 reverse() - Reverse list in place
fruits = ["apple", "banana", "cherry"]
print(f"Original fruits: {fruits}")
fruits.reverse()
print(f"After reverse(): {fruits}")

# 7.3 sorted() - Return new sorted list (doesn't modify original)
original = [3, 1, 4, 1, 5]
sorted_copy = sorted(original)
print(f"Original: {original}")
print(f"Sorted copy: {sorted_copy}")

# ============================================================================
# 8. LIST COMPREHENSIONS
# ============================================================================

print("\n8. List Comprehensions:")
print("-" * 22)

# List comprehension syntax: [expression for item in iterable if condition]

# 8.1 Basic list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Numbers: {numbers}")
print(f"Squares: {squares}")

# 8.2 List comprehension with condition
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Even squares: {even_squares}")

# 8.3 List comprehension with string manipulation
words = ["hello", "world", "python", "programming"]
uppercase_words = [word.upper() for word in words]
long_words = [word for word in words if len(word) > 5]

print(f"Original words: {words}")
print(f"Uppercase: {uppercase_words}")
print(f"Long words (>5 chars): {long_words}")

# 8.4 Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Matrix: {matrix}")
print(f"Flattened: {flattened}")

# ============================================================================
# 9. PRACTICAL EXAMPLES
# ============================================================================

print("\n9. Practical Examples:")
print("-" * 22)

# 9.1 Grade management system
def manage_grades():
    """Demonstrate practical list usage with grades."""
    grades = []
    
    # Add grades
    grades.extend([85, 92, 78, 96, 88])
    print(f"Student grades: {grades}")
    
    # Calculate statistics
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    
    print(f"Average: {average:.2f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
    
    # Find grades above average
    above_average = [grade for grade in grades if grade > average]
    print(f"Grades above average: {above_average}")
    
    return grades

grades = manage_grades()

# ============================================================================
# 10. EXERCISES
# ============================================================================

print(f"\n{'='*50}")
print("EXERCISES - Practice with Lists!")
print("="*50)

# Exercise 1: List manipulation
def exercise_1():
    """Basic list operations exercise."""
    print("\nExercise 1: List Manipulation")
    
    # Create a list of numbers 1-10
    numbers = list(range(1, 11))
    print(f"Original list: {numbers}")
    
    # Remove even numbers
    odd_numbers = [num for num in numbers if num % 2 != 0]
    print(f"Odd numbers only: {odd_numbers}")
    
    # Square the remaining numbers
    squared_odds = [num**2 for num in odd_numbers]
    print(f"Squared odd numbers: {squared_odds}")
    
    return squared_odds

exercise_1()

# Exercise 2: Word processing
def exercise_2():
    """Word processing with lists."""
    print("\nExercise 2: Word Processing")
    
    sentence = "Python is a powerful programming language"
    words = sentence.split()
    
    print(f"Original sentence: {sentence}")
    print(f"Words: {words}")
    print(f"Number of words: {len(words)}")
    
    # Find longest word
    longest_word = max(words, key=len)
    print(f"Longest word: {longest_word} ({len(longest_word)} characters)")
    
    # Words longer than 4 characters
    long_words = [word for word in words if len(word) > 4]
    print(f"Words longer than 4 chars: {long_words}")
    
    # Reverse the word order
    reversed_words = words[::-1]
    reversed_sentence = " ".join(reversed_words)
    print(f"Reversed sentence: {reversed_sentence}")

exercise_2()

print(f"\n{'='*50}")
print("Lists - Complete!")
print("Next: Learn about Tuples")
print("="*50)
