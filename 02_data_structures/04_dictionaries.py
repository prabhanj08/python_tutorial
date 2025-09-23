"""
Python Data Structures - Dictionaries
=====================================

Dictionaries are ordered (as of Python 3.7+), mutable collections that store
key-value pairs. They are one of the most important and versatile data structures
in Python, perfect for mapping relationships and storing structured data.

Key Concepts Covered:
- Dictionary creation and initialization
- Accessing and modifying dictionary elements
- Dictionary methods and operations
- Dictionary comprehensions
- Nested dictionaries
- Dictionary views and iteration
- Practical use cases and patterns
"""

# ============================================================================
# 1. CREATING DICTIONARIES
# ============================================================================

print("Python Dictionaries - Comprehensive Guide")
print("=" * 42)

# 1.1 Different ways to create dictionaries
print("1. Creating Dictionaries:")
print("-" * 25)

# Empty dictionary
empty_dict = {}
empty_dict2 = dict()

# Dictionary with initial values
student = {"name": "Alice", "age": 20, "grade": "A"}
coordinates = {"x": 10, "y": 20, "z": 30}
mixed_dict = {"string": "hello", "number": 42, "boolean": True, "list": [1, 2, 3]}

# Dictionary from sequences
pairs = [("a", 1), ("b", 2), ("c", 3)]
dict_from_pairs = dict(pairs)

# Dictionary using keyword arguments
person = dict(name="Bob", age=25, city="New York")

# Dictionary from keys with default value
keys = ["apple", "banana", "cherry"]
fruit_dict = dict.fromkeys(keys, 0)

print(f"Empty dictionary: {empty_dict}")
print(f"Student: {student}")
print(f"Coordinates: {coordinates}")
print(f"Mixed types: {mixed_dict}")
print(f"From pairs: {dict_from_pairs}")
print(f"From keywords: {person}")
print(f"From keys with default: {fruit_dict}")

# ============================================================================
# 2. ACCESSING DICTIONARY ELEMENTS
# ============================================================================

print("\n2. Accessing Dictionary Elements:")
print("-" * 34)

book = {
    "title": "Python Programming",
    "author": "John Doe",
    "year": 2023,
    "pages": 450,
    "available": True
}

print(f"Book dictionary: {book}")

# 2.1 Access using square brackets
print(f"Title: {book['title']}")
print(f"Author: {book['author']}")
print(f"Year: {book['year']}")

# 2.2 Access using get() method (safer)
print(f"Pages: {book.get('pages')}")
print(f"ISBN (not exists): {book.get('isbn')}")  # Returns None
print(f"ISBN with default: {book.get('isbn', 'Not Available')}")

# 2.3 Check if key exists
print(f"'title' in book: {'title' in book}")
print(f"'isbn' in book: {'isbn' in book}")

# KeyError example (commented to avoid error)
# print(book['isbn'])  # This would raise KeyError

# ============================================================================
# 3. MODIFYING DICTIONARIES
# ============================================================================

print("\n3. Modifying Dictionaries:")
print("-" * 26)

# Dictionaries are mutable
inventory = {"apples": 50, "bananas": 30, "oranges": 25}
print(f"Original inventory: {inventory}")

# 3.1 Adding new key-value pairs
inventory["grapes"] = 40
print(f"After adding grapes: {inventory}")

# 3.2 Modifying existing values
inventory["apples"] = 60
print(f"After updating apples: {inventory}")

# 3.3 Using update() method
inventory.update({"bananas": 35, "strawberries": 20})
print(f"After update(): {inventory}")

# 3.4 Update with another dictionary
new_items = {"kiwi": 15, "mango": 25}
inventory.update(new_items)
print(f"After updating with dict: {inventory}")

# ============================================================================
# 4. REMOVING ELEMENTS FROM DICTIONARIES
# ============================================================================

print("\n4. Removing Elements:")
print("-" * 21)

scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 96, "Eve": 88}
print(f"Original scores: {scores}")

# 4.1 del statement - Remove key-value pair
del scores["Charlie"]
print(f"After del scores['Charlie']: {scores}")

# 4.2 pop() - Remove and return value
removed_score = scores.pop("Eve")
print(f"Removed Eve's score: {removed_score}")
print(f"After pop('Eve'): {scores}")

# 4.3 pop() with default value
removed_score2 = scores.pop("Frank", "Not Found")
print(f"Tried to remove Frank: {removed_score2}")

# 4.4 popitem() - Remove and return last key-value pair
last_item = scores.popitem()
print(f"Removed last item: {last_item}")
print(f"After popitem(): {scores}")

# 4.5 clear() - Remove all elements
test_dict = {"a": 1, "b": 2}
print(f"Before clear(): {test_dict}")
test_dict.clear()
print(f"After clear(): {test_dict}")

# ============================================================================
# 5. DICTIONARY METHODS
# ============================================================================

print("\n5. Dictionary Methods:")
print("-" * 21)

data = {"name": "Alice", "age": 25, "city": "Boston", "job": "Engineer"}
print(f"Data dictionary: {data}")

# 5.1 keys() - Get all keys
keys = data.keys()
print(f"Keys: {list(keys)}")

# 5.2 values() - Get all values
values = data.values()
print(f"Values: {list(values)}")

# 5.3 items() - Get all key-value pairs
items = data.items()
print(f"Items: {list(items)}")

# 5.4 copy() - Create shallow copy
data_copy = data.copy()
print(f"Copy: {data_copy}")

# 5.5 setdefault() - Get value or set default if key doesn't exist
salary = data.setdefault("salary", 50000)
print(f"Salary (set default): {salary}")
print(f"Data after setdefault: {data}")

# ============================================================================
# 6. DICTIONARY ITERATION
# ============================================================================

print("\n6. Dictionary Iteration:")
print("-" * 24)

grades = {"Math": 85, "Science": 92, "English": 78, "History": 88}
print(f"Grades: {grades}")

# 6.1 Iterate over keys (default)
print("Iterating over keys:")
for subject in grades:
    print(f"  {subject}: {grades[subject]}")

# 6.2 Iterate over keys explicitly
print("Iterating over keys explicitly:")
for subject in grades.keys():
    print(f"  {subject}")

# 6.3 Iterate over values
print("Iterating over values:")
for grade in grades.values():
    print(f"  {grade}")

# 6.4 Iterate over key-value pairs
print("Iterating over items:")
for subject, grade in grades.items():
    print(f"  {subject}: {grade}")

# ============================================================================
# 7. DICTIONARY COMPREHENSIONS
# ============================================================================

print("\n7. Dictionary Comprehensions:")
print("-" * 27)

# Dictionary comprehension syntax: {key_expr: value_expr for item in iterable if condition}

# 7.1 Basic dictionary comprehension
numbers = [1, 2, 3, 4, 5]
squares = {x: x**2 for x in numbers}
print(f"Numbers: {numbers}")
print(f"Squares dict: {squares}")

# 7.2 Dictionary comprehension with condition
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print(f"Even squares: {even_squares}")

# 7.3 Transform existing dictionary
original_prices = {"apple": 1.0, "banana": 0.5, "cherry": 2.0}
discounted_prices = {fruit: price * 0.9 for fruit, price in original_prices.items()}
print(f"Original prices: {original_prices}")
print(f"Discounted prices: {discounted_prices}")

# 7.4 Dictionary from two lists
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "red"]
fruit_colors = {fruit: color for fruit, color in zip(fruits, colors)}
print(f"Fruit colors: {fruit_colors}")

# 7.5 Conditional dictionary comprehension
words = ["hello", "world", "python", "programming", "code"]
word_lengths = {word: len(word) for word in words if len(word) > 4}
print(f"Long words and lengths: {word_lengths}")

# ============================================================================
# 8. NESTED DICTIONARIES
# ============================================================================

print("\n8. Nested Dictionaries:")
print("-" * 22)

# 8.1 Creating nested dictionaries
students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "grades": {"math": 85, "science": 92, "english": 78}
    },
    "student2": {
        "name": "Bob",
        "age": 19,
        "grades": {"math": 78, "science": 85, "english": 90}
    },
    "student3": {
        "name": "Charlie",
        "age": 21,
        "grades": {"math": 92, "science": 88, "english": 85}
    }
}

print("Students database:")
for student_id, student_info in students.items():
    print(f"{student_id}: {student_info['name']} (age {student_info['age']})")
    for subject, grade in student_info['grades'].items():
        print(f"  {subject}: {grade}")

# 8.2 Accessing nested dictionary elements
print(f"\nAlice's math grade: {students['student1']['grades']['math']}")
print(f"Bob's name: {students['student2']['name']}")

# 8.3 Modifying nested dictionaries
students['student1']['grades']['history'] = 88
students['student2']['age'] = 20
print(f"Updated Alice's grades: {students['student1']['grades']}")
print(f"Updated Bob's age: {students['student2']['age']}")

# ============================================================================
# 9. DICTIONARY VIEWS
# ============================================================================

print("\n9. Dictionary Views:")
print("-" * 19)

colors = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}
print(f"Colors dictionary: {colors}")

# 9.1 Dictionary views are dynamic
keys_view = colors.keys()
values_view = colors.values()
items_view = colors.items()

print(f"Keys view: {keys_view}")
print(f"Values view: {values_view}")
print(f"Items view: {items_view}")

# 9.2 Views update when dictionary changes
colors["yellow"] = "#FFFF00"
print(f"After adding yellow:")
print(f"Keys view: {keys_view}")  # Automatically updated
print(f"Values view: {values_view}")  # Automatically updated

# 9.3 Set operations on views
color_names = {"red", "blue", "purple"}
common_colors = colors.keys() & color_names
print(f"Common colors: {common_colors}")

# ============================================================================
# 10. PRACTICAL EXAMPLES
# ============================================================================

print("\n10. Practical Examples:")
print("-" * 23)

# 10.1 Word frequency counter
def count_word_frequency(text):
    """Count frequency of words in text."""
    words = text.lower().split()
    frequency = {}
    
    for word in words:
        # Remove punctuation (simple approach)
        clean_word = ''.join(char for char in word if char.isalnum())
        if clean_word:
            frequency[clean_word] = frequency.get(clean_word, 0) + 1
    
    return frequency

sample_text = "Python is great. Python is powerful. I love Python programming."
word_freq = count_word_frequency(sample_text)
print(f"Text: {sample_text}")
print(f"Word frequency: {word_freq}")

# 10.2 Group data by category
def group_by_category(items):
    """Group items by their category."""
    grouped = {}
    
    for item in items:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item)
    
    return grouped

products = [
    {"name": "Laptop", "category": "Electronics", "price": 999},
    {"name": "Book", "category": "Education", "price": 25},
    {"name": "Phone", "category": "Electronics", "price": 699},
    {"name": "Pen", "category": "Education", "price": 2},
    {"name": "Tablet", "category": "Electronics", "price": 399}
]

grouped_products = group_by_category(products)
print(f"\nGrouped products:")
for category, items in grouped_products.items():
    print(f"{category}:")
    for item in items:
        print(f"  {item['name']}: ${item['price']}")

# 10.3 Configuration management
def load_config():
    """Example configuration using nested dictionaries."""
    config = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "myapp",
            "credentials": {
                "username": "admin",
                "password": "secret"
            }
        },
        "api": {
            "base_url": "https://api.example.com",
            "timeout": 30,
            "retries": 3
        },
        "features": {
            "debug_mode": True,
            "cache_enabled": True,
            "max_users": 1000
        }
    }
    return config

config = load_config()
print(f"\nConfiguration:")
print(f"Database host: {config['database']['host']}")
print(f"API timeout: {config['api']['timeout']}")
print(f"Debug mode: {config['features']['debug_mode']}")

# ============================================================================
# 11. DICTIONARY PERFORMANCE AND BEST PRACTICES
# ============================================================================

print("\n11. Performance and Best Practices:")
print("-" * 36)

import time

# 11.1 Dictionary vs list for lookups
size = 100000
test_dict = {i: f"value_{i}" for i in range(size)}
test_list = [(i, f"value_{i}") for i in range(size)]

search_key = size - 1

# Dictionary lookup (O(1) average)
start = time.time()
for _ in range(1000):
    _ = search_key in test_dict
dict_time = time.time() - start

# List lookup (O(n))
start = time.time()
for _ in range(1000):
    _ = any(key == search_key for key, value in test_list)
list_time = time.time() - start

print(f"Dictionary lookup time: {dict_time:.6f} seconds")
print(f"List lookup time: {list_time:.6f} seconds")
print(f"Dictionary is {list_time/dict_time:.0f}x faster for lookups")

# 11.2 Best practices
print(f"\nBest Practices:")
print("- Use get() instead of [] for safe access")
print("- Use setdefault() for default values")
print("- Use dict comprehensions for transformations")
print("- Use collections.defaultdict for automatic defaults")
print("- Keys must be immutable (hashable)")

# ============================================================================
# 12. EXERCISES
# ============================================================================

print(f"\n{'='*50}")
print("EXERCISES - Practice with Dictionaries!")
print("="*50)

# Exercise 1: Student grade management
def exercise_1():
    """Manage student grades using dictionaries."""
    print("\nExercise 1: Student Grade Management")
    
    # Student data
    students = {
        "Alice": {"math": 85, "science": 92, "english": 78},
        "Bob": {"math": 78, "science": 85, "english": 90},
        "Charlie": {"math": 92, "science": 88, "english": 85}
    }
    
    print("Student Grades:")
    for name, grades in students.items():
        average = sum(grades.values()) / len(grades)
        print(f"{name}: {grades} (Average: {average:.1f})")
    
    # Find best student in each subject
    subjects = ["math", "science", "english"]
    for subject in subjects:
        best_student = max(students.items(), key=lambda x: x[1][subject])
        print(f"Best in {subject}: {best_student[0]} ({best_student[1][subject]})")
    
    # Overall best student
    overall_best = max(students.items(), 
                      key=lambda x: sum(x[1].values()) / len(x[1]))
    overall_avg = sum(overall_best[1].values()) / len(overall_best[1])
    print(f"Overall best student: {overall_best[0]} (Average: {overall_avg:.1f})")

exercise_1()

# Exercise 2: Inventory management
def exercise_2():
    """Manage inventory using dictionaries."""
    print("\nExercise 2: Inventory Management")
    
    inventory = {
        "laptops": {"quantity": 50, "price": 999.99},
        "mice": {"quantity": 200, "price": 25.50},
        "keyboards": {"quantity": 150, "price": 75.00},
        "monitors": {"quantity": 80, "price": 299.99}
    }
    
    print("Current Inventory:")
    total_value = 0
    for item, details in inventory.items():
        item_value = details["quantity"] * details["price"]
        total_value += item_value
        print(f"{item.capitalize()}: {details['quantity']} units @ ${details['price']:.2f} = ${item_value:.2f}")
    
    print(f"Total inventory value: ${total_value:.2f}")
    
    # Simulate sales
    sales = {"laptops": 5, "mice": 20, "keyboards": 10}
    
    print(f"\nProcessing sales: {sales}")
    for item, sold_quantity in sales.items():
        if item in inventory:
            if inventory[item]["quantity"] >= sold_quantity:
                inventory[item]["quantity"] -= sold_quantity
                revenue = sold_quantity * inventory[item]["price"]
                print(f"Sold {sold_quantity} {item} for ${revenue:.2f}")
            else:
                print(f"Insufficient stock for {item}")
    
    print(f"\nUpdated inventory:")
    for item, details in inventory.items():
        print(f"{item.capitalize()}: {details['quantity']} units")

exercise_2()

# Exercise 3: Text analysis with dictionaries
def exercise_3():
    """Analyze text using dictionaries."""
    print("\nExercise 3: Text Analysis")
    
    text = """
    Python is a high-level programming language. Python is easy to learn.
    Python has simple syntax. Many developers love Python for its simplicity.
    Python is used in web development, data science, and automation.
    """
    
    # Clean and split text
    words = text.lower().replace('\n', ' ').split()
    clean_words = [''.join(c for c in word if c.isalnum()) for word in words]
    clean_words = [word for word in clean_words if word]
    
    # Word frequency analysis
    word_freq = {}
    for word in clean_words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    print(f"Text analysis results:")
    print(f"Total words: {len(clean_words)}")
    print(f"Unique words: {len(word_freq)}")
    
    # Most common words
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    print(f"Most common words:")
    for word, count in sorted_words[:5]:
        print(f"  '{word}': {count} times")
    
    # Words by length
    length_groups = {}
    for word in word_freq:
        length = len(word)
        if length not in length_groups:
            length_groups[length] = []
        length_groups[length].append(word)
    
    print(f"Words grouped by length:")
    for length in sorted(length_groups.keys()):
        print(f"  {length} letters: {length_groups[length]}")

exercise_3()

print(f"\n{'='*50}")
print("Dictionaries - Complete!")
print("Data Structures section finished!")
print("="*50)