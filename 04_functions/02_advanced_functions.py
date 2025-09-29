"""
Python Functions - Advanced Function Concepts
=============================================

This module covers advanced function concepts including variable arguments,
lambda functions, higher-order functions, closures, and functional programming
techniques. These concepts enable more flexible and powerful function design.

Key Concepts Covered:
- *args and **kwargs (variable arguments)
- Lambda functions (anonymous functions)
- Higher-order functions
- Closures and nested functions
- Function decorators (basic introduction)
- Functional programming with map, filter, reduce
"""

# ============================================================================
# 1. VARIABLE ARGUMENTS (*args and **kwargs)
# ============================================================================

print("Advanced Functions - Comprehensive Guide")
print("=" * 41)

# 1.1 *args - Variable positional arguments
print("1. Variable Arguments (*args and **kwargs):")
print("-" * 42)

def sum_all(*args):
    """Sum all provided arguments."""
    print(f"Arguments received: {args}")
    return sum(args)

print("Using *args:")
result1 = sum_all(1, 2, 3)
result2 = sum_all(10, 20, 30, 40, 50)
print(f"sum_all(1, 2, 3) = {result1}")
print(f"sum_all(10, 20, 30, 40, 50) = {result2}")

# 1.2 **kwargs - Variable keyword arguments
def print_info(**kwargs):
    """Print all keyword arguments."""
    print("Keyword arguments received:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("\nUsing **kwargs:")
print_info(name="Alice", age=25, city="New York")
print_info(product="Laptop", price=999.99, brand="TechCorp")

# 1.3 Combining regular parameters, *args, and **kwargs
def flexible_function(required_param, default_param="default", *args, **kwargs):
    """Demonstrate all parameter types together."""
    print(f"Required parameter: {required_param}")
    print(f"Default parameter: {default_param}")
    print(f"Additional positional args: {args}")
    print(f"Keyword args: {kwargs}")

print("\nCombining all parameter types:")
flexible_function("must_provide", "custom_default", 1, 2, 3, 
                 extra1="value1", extra2="value2")

# 1.4 Unpacking arguments
def calculate_rectangle_area(length, width):
    """Calculate rectangle area."""
    return length * width

# Unpacking list/tuple with *
dimensions = [5, 3]
area1 = calculate_rectangle_area(*dimensions)
print(f"\nUnpacking list {dimensions}: area = {area1}")

# Unpacking dictionary with **
rect_info = {"length": 8, "width": 4}
area2 = calculate_rectangle_area(**rect_info)
print(f"Unpacking dict {rect_info}: area = {area2}")

# ============================================================================
# 2. LAMBDA FUNCTIONS
# ============================================================================

print("\n2. Lambda Functions:")
print("-" * 19)

# 2.1 Basic lambda functions
print("Basic lambda functions:")
square = lambda x: x ** 2
add = lambda x, y: x + y
is_even = lambda x: x % 2 == 0

print(f"square(5) = {square(5)}")
print(f"add(3, 7) = {add(3, 7)}")
print(f"is_even(4) = {is_even(4)}")
print(f"is_even(5) = {is_even(5)}")

# 2.2 Lambda with conditional expressions
max_of_two = lambda x, y: x if x > y else y
absolute_value = lambda x: x if x >= 0 else -x

print(f"\nLambda with conditionals:")
print(f"max_of_two(10, 7) = {max_of_two(10, 7)}")
print(f"absolute_value(-5) = {absolute_value(-5)}")

# 2.3 Lambda functions in data structures
operations = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y if y != 0 else "Division by zero"
}

print(f"\nLambda functions in dictionary:")
for op_name, op_func in operations.items():
    result = op_func(10, 3)
    print(f"{op_name}(10, 3) = {result}")

# ============================================================================
# 3. HIGHER-ORDER FUNCTIONS
# ============================================================================

print("\n3. Higher-Order Functions:")
print("-" * 26)

# 3.1 Functions that take other functions as arguments
def apply_operation(numbers, operation):
    """Apply an operation to all numbers in a list."""
    return [operation(num) for num in numbers]

def apply_to_pairs(numbers, operation):
    """Apply operation to consecutive pairs."""
    result = []
    for i in range(len(numbers) - 1):
        result.append(operation(numbers[i], numbers[i + 1]))
    return result

numbers = [1, 2, 3, 4, 5]
print(f"Original numbers: {numbers}")

# Apply different operations
squared = apply_operation(numbers, lambda x: x ** 2)
doubled = apply_operation(numbers, lambda x: x * 2)
print(f"Squared: {squared}")
print(f"Doubled: {doubled}")

# Apply to pairs
sums = apply_to_pairs(numbers, lambda x, y: x + y)
products = apply_to_pairs(numbers, lambda x, y: x * y)
print(f"Consecutive sums: {sums}")
print(f"Consecutive products: {products}")

# 3.2 Functions that return other functions
def create_multiplier(factor):
    """Create a function that multiplies by a given factor."""
    def multiplier(x):
        return x * factor
    return multiplier

def create_validator(min_value, max_value):
    """Create a validation function for a range."""
    def validator(value):
        return min_value <= value <= max_value
    return validator

print(f"\nFunctions returning functions:")
double = create_multiplier(2)
triple = create_multiplier(3)
print(f"double(5) = {double(5)}")
print(f"triple(4) = {triple(4)}")

age_validator = create_validator(0, 120)
score_validator = create_validator(0, 100)
print(f"age_validator(25) = {age_validator(25)}")
print(f"age_validator(150) = {age_validator(150)}")
print(f"score_validator(85) = {score_validator(85)}")

# ============================================================================
# 4. CLOSURES
# ============================================================================

print("\n4. Closures:")
print("-" * 11)

# 4.1 Basic closure example
def outer_function(x):
    """Demonstrate closure - inner function remembers outer variable."""
    def inner_function(y):
        return x + y  # x is captured from outer scope
    return inner_function

# Create closures
add_10 = outer_function(10)
add_20 = outer_function(20)

print("Closure examples:")
print(f"add_10(5) = {add_10(5)}")  # 10 + 5 = 15
print(f"add_20(5) = {add_20(5)}")  # 20 + 5 = 25

# 4.2 Closure with mutable state
def create_counter(initial_value=0):
    """Create a counter function with persistent state."""
    count = initial_value
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    def get_count():
        return count
    
    def reset():
        nonlocal count
        count = initial_value
    
    # Return multiple functions
    counter.get_count = get_count
    counter.reset = reset
    return counter

print(f"\nClosure with state:")
counter1 = create_counter(0)
counter2 = create_counter(100)

print(f"Counter1: {counter1()}, {counter1()}, {counter1()}")
print(f"Counter2: {counter2()}, {counter2()}")
print(f"Counter1 current value: {counter1.get_count()}")
counter1.reset()
print(f"Counter1 after reset: {counter1()}")

# ============================================================================
# 5. FUNCTIONAL PROGRAMMING WITH BUILT-IN FUNCTIONS
# ============================================================================

print("\n5. Functional Programming:")
print("-" * 25)

# 5.1 map() function
numbers = [1, 2, 3, 4, 5]
print(f"Original numbers: {numbers}")

# Using map with lambda
squared_map = list(map(lambda x: x ** 2, numbers))
print(f"Squared (map): {squared_map}")

# Using map with regular function
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius_temps = [0, 20, 30, 40]
fahrenheit_temps = list(map(celsius_to_fahrenheit, celsius_temps))
print(f"Celsius: {celsius_temps}")
print(f"Fahrenheit: {fahrenheit_temps}")

# 5.2 filter() function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"\nFiltering from: {numbers}")

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# Filter numbers greater than 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"Greater than 5: {greater_than_5}")

# Filter with custom function
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = list(filter(is_prime, numbers))
print(f"Prime numbers: {primes}")

# 5.3 reduce() function
from functools import reduce

numbers = [1, 2, 3, 4, 5]
print(f"\nReducing: {numbers}")

# Sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print(f"Sum: {total}")

# Find maximum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Maximum: {maximum}")

# Factorial using reduce
factorial_5 = reduce(lambda x, y: x * y, range(1, 6))
print(f"5! = {factorial_5}")

# 5.4 Combining map, filter, and reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"\nCombining operations on: {numbers}")

# Sum of squares of even numbers
result = reduce(
    lambda x, y: x + y,  # Sum
    map(
        lambda x: x ** 2,  # Square
        filter(lambda x: x % 2 == 0, numbers)  # Filter evens
    )
)
print(f"Sum of squares of even numbers: {result}")

# Same operation using list comprehension (more Pythonic)
result_comprehension = sum(x ** 2 for x in numbers if x % 2 == 0)
print(f"Same result with comprehension: {result_comprehension}")

# ============================================================================
# 6. PRACTICAL EXAMPLES
# ============================================================================

print("\n6. Practical Examples:")
print("-" * 22)

# 6.1 Event system with callbacks
class EventSystem:
    """Simple event system using higher-order functions."""
    
    def __init__(self):
        self.callbacks = {}
    
    def on(self, event_name, callback):
        """Register a callback for an event."""
        if event_name not in self.callbacks:
            self.callbacks[event_name] = []
        self.callbacks[event_name].append(callback)
    
    def emit(self, event_name, *args, **kwargs):
        """Emit an event and call all registered callbacks."""
        if event_name in self.callbacks:
            for callback in self.callbacks[event_name]:
                callback(*args, **kwargs)

# Example usage
event_system = EventSystem()

# Register event handlers
event_system.on("user_login", lambda username: print(f"User {username} logged in"))
event_system.on("user_login", lambda username: print(f"Welcome back, {username}!"))
event_system.on("user_logout", lambda username: print(f"User {username} logged out"))

print("Event system example:")
event_system.emit("user_login", "Alice")
event_system.emit("user_logout", "Alice")

# 6.2 Data processing pipeline
def create_pipeline(*functions):
    """Create a data processing pipeline from functions."""
    def pipeline(data):
        result = data
        for func in functions:
            result = func(result)
        return result
    return pipeline

# Data processing functions
def remove_empty_strings(data):
    """Remove empty strings from list."""
    return [item for item in data if item.strip()]

def convert_to_uppercase(data):
    """Convert all strings to uppercase."""
    return [item.upper() for item in data]

def sort_data(data):
    """Sort the data."""
    return sorted(data)

# Create processing pipeline
process_data = create_pipeline(
    remove_empty_strings,
    convert_to_uppercase,
    sort_data
)

print(f"\nData processing pipeline:")
raw_data = ["apple", "", "banana", "  ", "cherry", "date"]
processed_data = process_data(raw_data)
print(f"Raw data: {raw_data}")
print(f"Processed data: {processed_data}")

# 6.3 Memoization using closures
def memoize(func):
    """Create a memoized version of a function."""
    cache = {}
    
    def memoized_func(*args):
        if args in cache:
            print(f"Cache hit for {args}")
            return cache[args]
        
        print(f"Computing for {args}")
        result = func(*args)
        cache[args] = result
        return result
    
    return memoized_func

# Example: Fibonacci with memoization
@memoize
def fibonacci(n):
    """Calculate Fibonacci number (inefficient without memoization)."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"\nMemoization example:")
print(f"fibonacci(10) = {fibonacci(10)}")
print(f"fibonacci(10) = {fibonacci(10)}")  # Should use cache

# ============================================================================
# 7. EXERCISES
# ============================================================================

print(f"\n{'='*50}")
print("EXERCISES - Practice with Advanced Functions!")
print("="*50)

# Exercise 1: Function factory
def exercise_1():
    """Create functions that generate other functions."""
    print("\nExercise 1: Function Factory")
    
    def create_formatter(prefix="", suffix="", transform=None):
        """Create a string formatter function."""
        def formatter(text):
            result = str(text)
            if transform:
                result = transform(result)
            return f"{prefix}{result}{suffix}"
        return formatter
    
    # Create different formatters
    html_bold = create_formatter("<b>", "</b>")
    parentheses = create_formatter("(", ")")
    uppercase_exclaim = create_formatter("", "!", str.upper)
    
    test_text = "hello world"
    print(f"Original: '{test_text}'")
    print(f"HTML bold: '{html_bold(test_text)}'")
    print(f"Parentheses: '{parentheses(test_text)}'")
    print(f"Uppercase exclaim: '{uppercase_exclaim(test_text)}'")

exercise_1()

# Exercise 2: Advanced data processing
def exercise_2():
    """Process data using functional programming techniques."""
    print("\nExercise 2: Advanced Data Processing")
    
    # Sample data: list of dictionaries
    employees = [
        {"name": "Alice", "department": "Engineering", "salary": 75000, "years": 3},
        {"name": "Bob", "department": "Marketing", "salary": 65000, "years": 5},
        {"name": "Charlie", "department": "Engineering", "salary": 85000, "years": 7},
        {"name": "Diana", "department": "Sales", "salary": 70000, "years": 2},
        {"name": "Eve", "department": "Engineering", "salary": 90000, "years": 8}
    ]
    
    # Filter engineering employees
    engineers = list(filter(lambda emp: emp["department"] == "Engineering", employees))
    print(f"Engineers: {[emp['name'] for emp in engineers]}")
    
    # Get salaries of engineers
    engineer_salaries = list(map(lambda emp: emp["salary"], engineers))
    print(f"Engineer salaries: {engineer_salaries}")
    
    # Calculate average salary of engineers
    avg_salary = reduce(lambda x, y: x + y, engineer_salaries) / len(engineer_salaries)
    print(f"Average engineer salary: ${avg_salary:,.2f}")
    
    # Find senior employees (5+ years) with high salaries (75k+)
    senior_high_earners = list(filter(
        lambda emp: emp["years"] >= 5 and emp["salary"] >= 75000,
        employees
    ))
    print(f"Senior high earners: {[emp['name'] for emp in senior_high_earners]}")

exercise_2()

# Exercise 3: Custom decorators (introduction)
def exercise_3():
    """Introduction to decorators using closures."""
    print("\nExercise 3: Simple Decorators")
    
    def timer_decorator(func):
        """Decorator to time function execution."""
        import time
        
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
            return result
        
        return wrapper
    
    def logger_decorator(func):
        """Decorator to log function calls."""
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned: {result}")
            return result
        
        return wrapper
    
    # Apply decorators manually
    def slow_function(n):
        """A function that takes some time."""
        import time
        time.sleep(0.1)  # Simulate work
        return sum(range(n))
    
    # Decorate the function
    timed_function = timer_decorator(slow_function)
    logged_function = logger_decorator(slow_function)
    
    print("Testing decorated functions:")
    result1 = timed_function(1000)
    print(f"Result: {result1}")
    
    result2 = logged_function(100)

exercise_3()

print(f"\n{'='*50}")
print("Advanced Functions - Complete!")
print("Next: Learn about Lambda Functions and Functional Programming")
print("="*50)