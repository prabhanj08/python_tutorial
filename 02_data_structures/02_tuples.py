"""
Python Data Structures - Tuples
===============================

Tuples are ordered, immutable collections in Python. Unlike lists, once created,
tuples cannot be modified. They are perfect for storing related data that shouldn't
change, such as coordinates, database records, or configuration settings.

Key Concepts Covered:
- Tuple creation and initialization
- Accessing tuple elements
- Tuple immutability
- Tuple methods and operations
- Tuple unpacking and packing
- Named tuples
- When to use tuples vs lists
"""

# ============================================================================
# 1. CREATING TUPLES
# ============================================================================

print("Python Tuples - Comprehensive Guide")
print("=" * 36)

# 1.1 Different ways to create tuples
print("1. Creating Tuples:")
print("-" * 20)

# Empty tuple
empty_tuple = ()
empty_tuple2 = tuple()

# Tuple with values
coordinates = (10, 20)
colors = ("red", "green", "blue")
mixed_tuple = (1, "hello", 3.14, True)

# Single element tuple (note the comma!)
single_element = (42,)  # Without comma, it's just parentheses for grouping
not_a_tuple = (42)      # This is just an integer

# Tuple without parentheses (tuple packing)
point = 5, 10
rgb = 255, 128, 0

print(f"Empty tuple: {empty_tuple}")
print(f"Coordinates: {coordinates}")
print(f"Colors: {colors}")
print(f"Mixed tuple: {mixed_tuple}")
print(f"Single element: {single_element} (type: {type(single_element)})")
print(f"Not a tuple: {not_a_tuple} (type: {type(not_a_tuple)})")
print(f"Point (no parentheses): {point}")
print(f"RGB (no parentheses): {rgb}")

# ============================================================================
# 2. ACCESSING TUPLE ELEMENTS
# ============================================================================

print("\n2. Accessing Tuple Elements:")
print("-" * 30)

fruits = ("apple", "banana", "cherry", "date", "elderberry")

# Positive indexing (0-based)
print(f"Fruits tuple: {fruits}")
print(f"First fruit (index 0): {fruits[0]}")
print(f"Second fruit (index 1): {fruits[1]}")
print(f"Last fruit (index {len(fruits)-1}): {fruits[len(fruits)-1]}")

# Negative indexing (from the end)
print(f"Last fruit (index -1): {fruits[-1]}")
print(f"Second to last (index -2): {fruits[-2]}")

# Tuple slicing [start:end:step]
print(f"\nSlicing examples:")
print(f"First three: {fruits[:3]}")           # [start:end]
print(f"Last two: {fruits[-2:]}")             # [start:]
print(f"Middle elements: {fruits[1:4]}")      # [start:end]
print(f"Every second element: {fruits[::2]}")  # [::step]
print(f"Reversed tuple: {fruits[::-1]}")      # [::negative_step]

# ============================================================================
# 3. TUPLE IMMUTABILITY
# ============================================================================

print("\n3. Tuple Immutability:")
print("-" * 22)

# Tuples are immutable - cannot be changed after creation
numbers = (1, 2, 3, 4, 5)
print(f"Original tuple: {numbers}")

# This would cause an error:
# numbers[0] = 10  # TypeError: 'tuple' object does not support item assignment

# However, if a tuple contains mutable objects, those can be modified
nested_data = ([1, 2, 3], "hello", {"key": "value"})
print(f"Nested data: {nested_data}")

# We can modify the list inside the tuple
nested_data[0].append(4)
print(f"After modifying list inside: {nested_data}")

# We can modify the dictionary inside the tuple
nested_data[2]["new_key"] = "new_value"
print(f"After modifying dict inside: {nested_data}")

# But we cannot reassign elements of the tuple itself
# nested_data[1] = "world"  # This would cause TypeError

# ============================================================================
# 4. TUPLE METHODS
# ============================================================================

print("\n4. Tuple Methods:")
print("-" * 17)

# Tuples have only two methods because they're immutable
letters = ("a", "b", "c", "b", "d", "b", "e")
print(f"Letters tuple: {letters}")

# 4.1 count() - Count occurrences of a value
b_count = letters.count("b")
print(f"Number of 'b's: {b_count}")

a_count = letters.count("a")
print(f"Number of 'a's: {a_count}")

# 4.2 index() - Find index of first occurrence
first_b_index = letters.index("b")
print(f"First 'b' at index: {first_b_index}")

# Find 'b' starting from index 2
second_b_index = letters.index("b", 2)
print(f"Next 'b' from index 2: {second_b_index}")

# ============================================================================
# 5. TUPLE OPERATIONS
# ============================================================================

print("\n5. Tuple Operations:")
print("-" * 20)

# 5.1 Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"Tuple1: {tuple1}")
print(f"Tuple2: {tuple2}")
print(f"Combined: {combined}")

# 5.2 Repetition
repeated = (0,) * 5
pattern = (1, 2) * 3
print(f"Repeated zeros: {repeated}")
print(f"Repeated pattern: {pattern}")

# 5.3 Membership testing
colors = ("red", "green", "blue")
print(f"Colors: {colors}")
print(f"'red' in colors: {'red' in colors}")
print(f"'yellow' in colors: {'yellow' in colors}")

# 5.4 Length and other built-in functions
numbers = (5, 2, 8, 1, 9, 3)
print(f"Numbers: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Sum: {sum(numbers)}")

# ============================================================================
# 6. TUPLE UNPACKING AND PACKING
# ============================================================================

print("\n6. Tuple Unpacking and Packing:")
print("-" * 33)

# 6.1 Tuple packing (creating tuples)
person = "Alice", 25, "Engineer"  # Packing values into a tuple
print(f"Packed tuple: {person}")

# 6.2 Tuple unpacking (extracting values)
name, age, job = person  # Unpacking tuple into variables
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Job: {job}")

# 6.3 Swapping variables using tuple unpacking
a = 10
b = 20
print(f"Before swap: a={a}, b={b}")

a, b = b, a  # Swap using tuple unpacking
print(f"After swap: a={a}, b={b}")

# 6.4 Multiple assignment
coordinates = (100, 200, 300)
x, y, z = coordinates
print(f"Coordinates: {coordinates}")
print(f"x={x}, y={y}, z={z}")

# 6.5 Unpacking with * (extended unpacking)
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
first, second, *middle, second_last, last = numbers
print(f"Numbers: {numbers}")
print(f"First: {first}")
print(f"Second: {second}")
print(f"Middle: {middle}")
print(f"Second last: {second_last}")
print(f"Last: {last}")

# ============================================================================
# 7. NESTED TUPLES
# ============================================================================

print("\n7. Nested Tuples:")
print("-" * 17)

# 7.1 Creating nested tuples
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("Matrix (nested tuple):")
for row in matrix:
    print(row)

# 7.2 Accessing nested tuple elements
print(f"Element at row 1, column 2: {matrix[1][2]}")  # 6
print(f"First row: {matrix[0]}")
print(f"Last element of last row: {matrix[-1][-1]}")

# 7.3 Complex nested structure
student_records = (
    ("Alice", 85, ("Math", "Science", "English")),
    ("Bob", 92, ("History", "Art", "Music")),
    ("Charlie", 78, ("Math", "Physics", "Chemistry"))
)

print(f"\nStudent Records:")
for name, grade, subjects in student_records:
    print(f"{name}: Grade {grade}, Subjects: {subjects}")

# ============================================================================
# 8. NAMED TUPLES
# ============================================================================

print("\n8. Named Tuples:")
print("-" * 16)

from collections import namedtuple

# 8.1 Creating a named tuple class
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', ['name', 'age', 'city'])

# 8.2 Creating instances
p1 = Point(10, 20)
p2 = Point(x=30, y=40)

person1 = Person("Alice", 25, "New York")
person2 = Person(name="Bob", age=30, city="London")

print(f"Point 1: {p1}")
print(f"Point 2: {p2}")
print(f"Person 1: {person1}")
print(f"Person 2: {person2}")

# 8.3 Accessing named tuple elements
print(f"Point 1 - x: {p1.x}, y: {p1.y}")
print(f"Person 1 - Name: {person1.name}, Age: {person1.age}")

# 8.4 Named tuples are still tuples
print(f"Point 1 by index: x={p1[0]}, y={p1[1]}")
print(f"Person 1 is tuple: {isinstance(person1, tuple)}")

# 8.5 Named tuple methods
print(f"Person 1 as dict: {person1._asdict()}")
print(f"Person fields: {person1._fields}")

# Create new instance with some fields changed
person3 = person1._replace(age=26, city="Boston")
print(f"Person 3 (modified): {person3}")

# ============================================================================
# 9. TUPLES VS LISTS - WHEN TO USE WHICH
# ============================================================================

print("\n9. Tuples vs Lists - When to Use Which:")
print("-" * 40)

print("Use TUPLES when:")
print("- Data should not change (immutable)")
print("- Representing fixed collections (coordinates, RGB values)")
print("- Dictionary keys (tuples are hashable)")
print("- Function returns multiple values")
print("- Performance is critical (tuples are faster)")

print("\nUse LISTS when:")
print("- Data needs to be modified")
print("- Size of collection may change")
print("- Need list-specific methods (append, remove, etc.)")
print("- Working with homogeneous data that grows/shrinks")

# Example: Tuples as dictionary keys
locations = {
    (0, 0): "Origin",
    (10, 20): "Point A",
    (30, 40): "Point B"
}
print(f"\nLocations dict with tuple keys: {locations}")
print(f"Location at (10, 20): {locations[(10, 20)]}")

# ============================================================================
# 10. PRACTICAL EXAMPLES
# ============================================================================

print("\n10. Practical Examples:")
print("-" * 23)

# 10.1 Function returning multiple values
def get_name_parts(full_name):
    """Return first and last name as a tuple."""
    parts = full_name.split()
    if len(parts) >= 2:
        return parts[0], parts[-1]
    else:
        return parts[0], ""

first, last = get_name_parts("John Doe Smith")
print(f"Name parts: First='{first}', Last='{last}'")

# 10.2 Configuration settings
DATABASE_CONFIG = (
    "localhost",    # host
    5432,          # port
    "mydb",        # database name
    "user",        # username
    "password"     # password
)

host, port, db_name, username, password = DATABASE_CONFIG
print(f"Database config: {host}:{port}/{db_name}")

# 10.3 RGB color definitions
COLORS = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "white": (255, 255, 255),
    "black": (0, 0, 0)
}

def mix_colors(color1, color2):
    """Mix two RGB colors by averaging."""
    r1, g1, b1 = COLORS[color1]
    r2, g2, b2 = COLORS[color2]
    
    mixed_r = (r1 + r2) // 2
    mixed_g = (g1 + g2) // 2
    mixed_b = (b1 + b2) // 2
    
    return (mixed_r, mixed_g, mixed_b)

mixed = mix_colors("red", "blue")
print(f"Red + Blue = {mixed}")

# ============================================================================
# 11. PERFORMANCE COMPARISON
# ============================================================================

print("\n11. Performance Comparison:")
print("-" * 27)

import time

# Create large collections
size = 1000000
list_data = list(range(size))
tuple_data = tuple(range(size))

# Test access time
start = time.time()
for i in range(1000):
    _ = list_data[500000]
list_time = time.time() - start

start = time.time()
for i in range(1000):
    _ = tuple_data[500000]
tuple_time = time.time() - start

print(f"List access time: {list_time:.6f} seconds")
print(f"Tuple access time: {tuple_time:.6f} seconds")
print(f"Tuple is {list_time/tuple_time:.2f}x faster for access")

# Memory usage comparison
import sys
list_memory = sys.getsizeof(list_data)
tuple_memory = sys.getsizeof(tuple_data)

print(f"List memory: {list_memory:,} bytes")
print(f"Tuple memory: {tuple_memory:,} bytes")
print(f"Tuple uses {((list_memory - tuple_memory) / list_memory) * 100:.1f}% less memory")

# ============================================================================
# 12. EXERCISES
# ============================================================================

print(f"\n{'='*50}")
print("EXERCISES - Practice with Tuples!")
print("="*50)

# Exercise 1: Coordinate system
def exercise_1():
    """Working with coordinate tuples."""
    print("\nExercise 1: Coordinate System")
    
    # Define points
    points = [(0, 0), (3, 4), (6, 8), (1, 1)]
    
    def distance_from_origin(point):
        """Calculate distance from origin."""
        x, y = point
        return (x**2 + y**2)**0.5
    
    print(f"Points: {points}")
    
    # Calculate distances
    distances = [distance_from_origin(point) for point in points]
    
    for point, dist in zip(points, distances):
        print(f"Distance from {point} to origin: {dist:.2f}")
    
    # Find closest point to origin
    closest = min(points, key=distance_from_origin)
    print(f"Closest point to origin: {closest}")

exercise_1()

# Exercise 2: Student records with named tuples
def exercise_2():
    """Student management with named tuples."""
    print("\nExercise 2: Student Records")
    
    Student = namedtuple('Student', ['name', 'age', 'grade', 'subjects'])
    
    students = [
        Student("Alice", 20, 85, ("Math", "Physics", "Chemistry")),
        Student("Bob", 19, 92, ("History", "Literature", "Art")),
        Student("Charlie", 21, 78, ("Biology", "Chemistry", "Math")),
        Student("Diana", 20, 96, ("Physics", "Math", "Computer Science"))
    ]
    
    print("Student Records:")
    for student in students:
        print(f"{student.name} (Age {student.age}): Grade {student.grade}")
        print(f"  Subjects: {', '.join(student.subjects)}")
    
    # Find highest grade
    top_student = max(students, key=lambda s: s.grade)
    print(f"\nTop student: {top_student.name} with grade {top_student.grade}")
    
    # Find students taking Math
    math_students = [s.name for s in students if "Math" in s.subjects]
    print(f"Students taking Math: {', '.join(math_students)}")

exercise_2()

# Exercise 3: Data processing with tuple unpacking
def exercise_3():
    """Data processing using tuple unpacking."""
    print("\nExercise 3: Sales Data Processing")
    
    # Sales data: (product, quantity, price)
    sales_data = [
        ("Laptop", 5, 999.99),
        ("Mouse", 20, 25.50),
        ("Keyboard", 15, 75.00),
        ("Monitor", 8, 299.99),
        ("Headphones", 12, 89.99)
    ]
    
    print("Sales Data:")
    total_revenue = 0
    
    for product, quantity, price in sales_data:
        revenue = quantity * price
        total_revenue += revenue
        print(f"{product}: {quantity} units × ${price:.2f} = ${revenue:.2f}")
    
    print(f"\nTotal Revenue: ${total_revenue:.2f}")
    
    # Find best selling product by revenue
    best_product = max(sales_data, key=lambda x: x[1] * x[2])
    product, quantity, price = best_product
    print(f"Best selling product: {product} (${quantity * price:.2f} revenue)")

exercise_3()

print(f"\n{'='*50}")
print("Tuples - Complete!")
print("Next: Learn about Sets")
print("="*50)