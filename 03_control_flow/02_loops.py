"""
Python Control Flow - Loops
===========================

Loops allow programs to execute code repeatedly based on certain conditions.
Python provides two main types of loops: for loops (for iterating over sequences)
and while loops (for repeating while a condition is true).

Key Concepts Covered:
- for loops and iteration
- while loops and conditions
- Loop control statements (break, continue, pass)
- Nested loops
- Loop with else clause
- Enumerate, zip, and range functions
- List comprehensions as loop alternatives
"""

# ============================================================================
# 1. FOR LOOPS - BASIC ITERATION
# ============================================================================

print("Python Loops - Comprehensive Guide")
print("=" * 36)

# 1.1 Basic for loop with lists
print("1. Basic For Loops:")
print("-" * 19)

fruits = ["apple", "banana", "cherry", "date"]
print("Iterating over a list:")
for fruit in fruits:
    print(f"  I like {fruit}")

# 1.2 For loop with strings
print("\nIterating over a string:")
word = "Python"
for letter in word:
    print(f"  Letter: {letter}")

# 1.3 For loop with range()
print("\nUsing range() function:")
print("range(5):")
for i in range(5):
    print(f"  Number: {i}")

print("range(2, 8):")
for i in range(2, 8):
    print(f"  Number: {i}")

print("range(0, 10, 2):")
for i in range(0, 10, 2):
    print(f"  Even number: {i}")

# ============================================================================
# 2. WHILE LOOPS
# ============================================================================

print("\n2. While Loops:")
print("-" * 15)

# 2.1 Basic while loop
print("Basic while loop (countdown):")
count = 5
while count > 0:
    print(f"  Count: {count}")
    count -= 1
print("  Blast off!")

# 2.2 While loop with user input simulation
print("\nWhile loop with condition:")
password_attempts = 0
max_attempts = 3
correct_password = "secret123"

# Simulate password attempts
test_passwords = ["wrong1", "wrong2", "secret123"]
attempt_index = 0

while password_attempts < max_attempts:
    # Simulate user input
    if attempt_index < len(test_passwords):
        entered_password = test_passwords[attempt_index]
        attempt_index += 1
    else:
        break
    
    password_attempts += 1
    print(f"  Attempt {password_attempts}: Trying '{entered_password}'")
    
    if entered_password == correct_password:
        print("  Access granted!")
        break
    else:
        remaining = max_attempts - password_attempts
        if remaining > 0:
            print(f"  Wrong password. {remaining} attempts remaining.")
        else:
            print("  Access denied. Too many failed attempts.")

# ============================================================================
# 3. LOOP CONTROL STATEMENTS
# ============================================================================

print("\n3. Loop Control Statements:")
print("-" * 28)

# 3.1 break statement
print("Using break statement:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num == 6:
        print(f"  Found {num}, breaking out of loop")
        break
    print(f"  Processing: {num}")

# 3.2 continue statement
print("\nUsing continue statement:")
for num in range(1, 11):
    if num % 2 == 0:  # Skip even numbers
        continue
    print(f"  Odd number: {num}")

# 3.3 pass statement
print("\nUsing pass statement (placeholder):")
for num in range(1, 6):
    if num == 3:
        pass  # Placeholder - do nothing for now
    else:
        print(f"  Processing: {num}")

# ============================================================================
# 4. NESTED LOOPS
# ============================================================================

print("\n4. Nested Loops:")
print("-" * 16)

# 4.1 Multiplication table
print("Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"  {i} x {j} = {result}")
    print()  # Empty line after each row

# 4.2 Pattern printing
print("Pattern printing:")
for row in range(1, 6):
    for col in range(row):
        print("*", end=" ")
    print()  # New line after each row

# 4.3 Matrix processing
print("\nMatrix processing:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix elements:")
for row_index, row in enumerate(matrix):
    for col_index, element in enumerate(row):
        print(f"  matrix[{row_index}][{col_index}] = {element}")

# ============================================================================
# 5. ENUMERATE FUNCTION
# ============================================================================

print("\n5. Enumerate Function:")
print("-" * 21)

# 5.1 Basic enumerate usage
colors = ["red", "green", "blue", "yellow"]
print("Using enumerate to get index and value:")
for index, color in enumerate(colors):
    print(f"  Index {index}: {color}")

# 5.2 Enumerate with custom start
print("\nEnumerate with custom start value:")
for index, color in enumerate(colors, start=1):
    print(f"  Color #{index}: {color}")

# 5.3 Practical example: Processing with line numbers
print("\nProcessing text with line numbers:")
text_lines = ["First line", "Second line", "Third line"]
for line_num, line in enumerate(text_lines, start=1):
    print(f"  Line {line_num}: {line}")

# ============================================================================
# 6. ZIP FUNCTION
# ============================================================================

print("\n6. Zip Function:")
print("-" * 16)

# 6.1 Basic zip usage
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Tokyo"]

print("Using zip to combine multiple lists:")
for name, age, city in zip(names, ages, cities):
    print(f"  {name} is {age} years old and lives in {city}")

# 6.2 Zip with different length lists
print("\nZip stops at shortest list:")
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [10, 20, 30]
for a, b in zip(numbers1, numbers2):
    print(f"  {a} + {b} = {a + b}")

# 6.3 Creating dictionaries with zip
print("\nCreating dictionary with zip:")
keys = ["name", "age", "city"]
values = ["Diana", 28, "Paris"]
person_dict = dict(zip(keys, values))
print(f"  Person dictionary: {person_dict}")

# ============================================================================
# 7. LOOP WITH ELSE CLAUSE
# ============================================================================

print("\n7. Loop with Else Clause:")
print("-" * 25)

# 7.1 For loop with else
print("For loop with else (no break):")
for num in range(1, 4):
    print(f"  Processing: {num}")
else:
    print("  Loop completed normally (no break)")

print("\nFor loop with else (with break):")
for num in range(1, 6):
    print(f"  Processing: {num}")
    if num == 3:
        print("  Breaking at 3")
        break
else:
    print("  This won't print because of break")

# 7.2 While loop with else
print("\nWhile loop with else:")
count = 3
while count > 0:
    print(f"  Count: {count}")
    count -= 1
else:
    print("  While loop completed normally")

# ============================================================================
# 8. PRACTICAL EXAMPLES
# ============================================================================

print("\n8. Practical Examples:")
print("-" * 22)

# 8.1 Finding prime numbers
def find_primes(limit):
    """Find all prime numbers up to the given limit."""
    primes = []
    
    for num in range(2, limit + 1):
        is_prime = True
        
        # Check if num is divisible by any number from 2 to sqrt(num)
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(num)
    
    return primes

print("Prime numbers up to 20:")
primes = find_primes(20)
print(f"  {primes}")

# 8.2 Word frequency counter
def count_word_frequency(text):
    """Count frequency of words in text."""
    words = text.lower().split()
    word_count = {}
    
    for word in words:
        # Remove punctuation (simple approach)
        clean_word = ''.join(char for char in word if char.isalnum())
        if clean_word:
            if clean_word in word_count:
                word_count[clean_word] += 1
            else:
                word_count[clean_word] = 1
    
    return word_count

sample_text = "Python is great. Python is powerful. I love Python programming."
word_freq = count_word_frequency(sample_text)
print(f"\nWord frequency in: '{sample_text}'")
for word, count in word_freq.items():
    print(f"  '{word}': {count}")

# 8.3 Menu-driven program
def menu_driven_calculator():
    """Simple calculator with menu loop."""
    print("\nSimple Calculator Menu:")
    
    operations = {
        "1": ("Addition", lambda x, y: x + y),
        "2": ("Subtraction", lambda x, y: x - y),
        "3": ("Multiplication", lambda x, y: x * y),
        "4": ("Division", lambda x, y: x / y if y != 0 else "Cannot divide by zero")
    }
    
    # Simulate user choices
    test_choices = ["1", "2", "5", "4"]
    test_numbers = [(10, 5), (15, 3), (0, 0), (20, 4)]
    
    for i, choice in enumerate(test_choices):
        print(f"\nMenu Options:")
        for key, (name, _) in operations.items():
            print(f"  {key}. {name}")
        print("  5. Exit")
        
        print(f"User choice: {choice}")
        
        if choice == "5":
            print("Goodbye!")
            break
        elif choice in operations:
            if i < len(test_numbers):
                num1, num2 = test_numbers[i]
                operation_name, operation_func = operations[choice]
                result = operation_func(num1, num2)
                print(f"  {operation_name}: {num1} and {num2} = {result}")
            else:
                print("  No test numbers available")
        else:
            print("  Invalid choice. Please try again.")

menu_driven_calculator()

# ============================================================================
# 9. LOOP OPTIMIZATION AND BEST PRACTICES
# ============================================================================

print("\n9. Loop Optimization:")
print("-" * 21)

import time

# 9.1 List comprehension vs traditional loop
print("Performance comparison:")

# Traditional loop
start_time = time.time()
squares_loop = []
for i in range(1000):
    squares_loop.append(i ** 2)
loop_time = time.time() - start_time

# List comprehension
start_time = time.time()
squares_comp = [i ** 2 for i in range(1000)]
comp_time = time.time() - start_time

print(f"  Traditional loop: {loop_time:.6f} seconds")
print(f"  List comprehension: {comp_time:.6f} seconds")
print(f"  List comprehension is {loop_time/comp_time:.2f}x faster")

# 9.2 Best practices
print("\nBest Practices:")
print("  - Use list comprehensions for simple transformations")
print("  - Use enumerate() instead of range(len())")
print("  - Use zip() to iterate over multiple sequences")
print("  - Avoid modifying lists while iterating over them")
print("  - Use break and continue to control loop flow efficiently")

# ============================================================================
# 10. EXERCISES
# ============================================================================

print(f"\n{'='*50}")
print("EXERCISES - Practice with Loops!")
print("="*50)

# Exercise 1: Number guessing game
def exercise_1():
    """Number guessing game simulation."""
    print("\nExercise 1: Number Guessing Game")
    
    import random
    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0
    
    # Simulate guesses
    test_guesses = [50, 75, 88, 94, 91, 93, 92]
    
    print(f"Guess the number between 1 and 100! (Secret: {secret_number})")
    
    for guess in test_guesses:
        attempts += 1
        print(f"Attempt {attempts}: Guessing {guess}")
        
        if guess == secret_number:
            print(f"Congratulations! You found it in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
        
        if attempts >= max_attempts:
            print(f"Game over! The number was {secret_number}")
            break
    else:
        if attempts < max_attempts:
            print("Ran out of test guesses!")

exercise_1()

# Exercise 2: Pattern generator
def exercise_2():
    """Generate various patterns using nested loops."""
    print("\nExercise 2: Pattern Generator")
    
    def print_triangle(height):
        """Print a triangle pattern."""
        print(f"Triangle (height {height}):")
        for i in range(1, height + 1):
            print("  " + "*" * i)
    
    def print_diamond(size):
        """Print a diamond pattern."""
        print(f"Diamond (size {size}):")
        # Upper half
        for i in range(1, size + 1):
            spaces = " " * (size - i)
            stars = "*" * (2 * i - 1)
            print("  " + spaces + stars)
        
        # Lower half
        for i in range(size - 1, 0, -1):
            spaces = " " * (size - i)
            stars = "*" * (2 * i - 1)
            print("  " + spaces + stars)
    
    def print_multiplication_table(size):
        """Print multiplication table."""
        print(f"Multiplication table ({size}x{size}):")
        for i in range(1, size + 1):
            for j in range(1, size + 1):
                print(f"{i*j:4d}", end="")
            print()
    
    print_triangle(5)
    print()
    print_diamond(4)
    print()
    print_multiplication_table(5)

exercise_2()

# Exercise 3: Data processing with loops
def exercise_3():
    """Process data using various loop techniques."""
    print("\nExercise 3: Data Processing")
    
    # Sample sales data
    sales_data = [
        {"product": "Laptop", "quantity": 5, "price": 999.99},
        {"product": "Mouse", "quantity": 20, "price": 25.50},
        {"product": "Keyboard", "quantity": 15, "price": 75.00},
        {"product": "Monitor", "quantity": 8, "price": 299.99},
        {"product": "Headphones", "quantity": 12, "price": 89.99}
    ]
    
    print("Sales Data Analysis:")
    
    # Calculate totals
    total_revenue = 0
    total_items = 0
    
    for item in sales_data:
        item_revenue = item["quantity"] * item["price"]
        total_revenue += item_revenue
        total_items += item["quantity"]
        
        print(f"  {item['product']}: {item['quantity']} × ${item['price']:.2f} = ${item_revenue:.2f}")
    
    print(f"\nSummary:")
    print(f"  Total items sold: {total_items}")
    print(f"  Total revenue: ${total_revenue:.2f}")
    print(f"  Average revenue per item: ${total_revenue/total_items:.2f}")
    
    # Find best and worst performing products
    best_product = max(sales_data, key=lambda x: x["quantity"] * x["price"])
    worst_product = min(sales_data, key=lambda x: x["quantity"] * x["price"])
    
    print(f"  Best performing: {best_product['product']} (${best_product['quantity'] * best_product['price']:.2f})")
    print(f"  Worst performing: {worst_product['product']} (${worst_product['quantity'] * worst_product['price']:.2f})")

exercise_3()

print(f"\n{'='*50}")
print("Loops - Complete!")
print("Control Flow section finished!")
print("="*50)