# Python Functions - Modular and Reusable Code

Welcome to the Python Functions section! This folder covers everything you need to know about creating, using, and mastering functions in Python - from basic function definition to advanced functional programming concepts.

## 📚 What You'll Learn

This section covers Python functions comprehensively:

- **Function Basics** - Definition, parameters, arguments, and return values
- **Advanced Functions** - Variable arguments, lambda functions, closures
- **Functional Programming** - Higher-order functions, map, filter, reduce
- **Best Practices** - Function design, documentation, and optimization

## 📁 Files in This Section

### 1. [`01_function_basics.py`](01_function_basics.py)
**Foundation of Function Programming**
- Function definition and calling syntax
- Parameters and arguments (positional, keyword, default)
- Return values and multiple returns
- Variable scope (local, global, nonlocal)
- Function documentation with docstrings
- Common pitfalls and best practices

**Key Concepts:**
```python
# Basic function structure
def function_name(param1, param2="default"):
    """Function docstring explaining purpose."""
    # Function body
    return result

# Different parameter types
def flexible_func(required, default="value", *args, **kwargs):
    pass

# Multiple return values
def get_stats(data):
    return min(data), max(data), sum(data)/len(data)

# Variable scope
global_var = "accessible everywhere"
def my_function():
    local_var = "only inside function"
    global global_var  # To modify global variable
```

**When to use Functions:**
- Breaking down complex problems into smaller parts
- Avoiding code repetition (DRY principle)
- Creating reusable code components
- Organizing code logically
- Testing individual pieces of functionality

### 2. [`02_advanced_functions.py`](02_advanced_functions.py)
**Advanced Function Techniques**
- Variable arguments (*args and **kwargs)
- Lambda functions (anonymous functions)
- Higher-order functions (functions as arguments/return values)
- Closures and nested functions
- Functional programming with map, filter, reduce
- Introduction to decorators

**Key Concepts:**
```python
# Variable arguments
def flexible_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

# Lambda functions
square = lambda x: x ** 2
numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))

# Higher-order functions
def apply_operation(data, operation):
    return [operation(item) for item in data]

# Closures
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)

# Functional programming
from functools import reduce
total = reduce(lambda x, y: x + y, numbers)
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

**When to use Advanced Functions:**
- Creating flexible APIs with variable arguments
- Functional programming and data transformations
- Event handling and callback systems
- Creating function factories and specialized tools
- Building decorators and middleware

## 🎯 Learning Objectives

By the end of this section, you should be able to:

### **Function Fundamentals**
- ✅ Define and call functions with various parameter types
- ✅ Use default parameters and handle optional arguments
- ✅ Return single and multiple values from functions
- ✅ Understand and apply variable scope rules
- ✅ Write clear function documentation

### **Advanced Function Techniques**
- ✅ Use *args and **kwargs for flexible function signatures
- ✅ Create and use lambda functions appropriately
- ✅ Implement higher-order functions and callbacks
- ✅ Understand closures and their practical applications
- ✅ Apply functional programming techniques

### **Function Design**
- ✅ Design functions following single responsibility principle
- ✅ Create pure functions without side effects
- ✅ Handle edge cases and error conditions
- ✅ Optimize function performance and readability
- ✅ Choose between different function patterns

## 🚀 Getting Started

### Prerequisites
- Completed [01_python_basics/](../01_python_basics/), [02_data_structures/](../02_data_structures/), and [03_control_flow/](../03_control_flow/)
- Understanding of variables, data types, and control structures
- Familiarity with Python syntax and indentation

### How to Use These Files

1. **Start with `01_function_basics.py`** - Master the fundamentals
2. **Progress to `02_advanced_functions.py`** - Learn advanced techniques
3. **Run all code examples** - See functions in action
4. **Complete the exercises** - Practice with real scenarios
5. **Apply concepts** - Use functions in your own projects

### Running the Files

```bash
# Navigate to the folder
cd Python_learning/04_functions/

# Run each file to see examples
python 01_function_basics.py
python 02_advanced_functions.py
```

## 🔧 Function Design Patterns

### **Common Function Patterns**

#### **Input Validation**
```python
def safe_divide(a, b):
    """Safely divide two numbers with validation."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

#### **Configuration Functions**
```python
def create_database_connection(host="localhost", port=5432, **config):
    """Create database connection with flexible configuration."""
    connection_string = f"postgresql://{host}:{port}"
    # Apply additional configuration
    return connection_string
```

#### **Factory Functions**
```python
def create_validator(min_val, max_val):
    """Create a validation function for a specific range."""
    def validator(value):
        return min_val <= value <= max_val
    return validator

age_validator = create_validator(0, 120)
```

#### **Callback Functions**
```python
def process_data(data, success_callback=None, error_callback=None):
    """Process data with optional callbacks."""
    try:
        result = perform_processing(data)
        if success_callback:
            success_callback(result)
        return result
    except Exception as e:
        if error_callback:
            error_callback(e)
        raise
```

### **Functional Programming Patterns**

#### **Data Transformation Pipeline**
```python
def process_numbers(numbers):
    """Transform numbers using functional programming."""
    return list(
        map(lambda x: x ** 2,           # Square
            filter(lambda x: x % 2 == 0,  # Filter evens
                   numbers)))              # Original data
```

#### **Reduce for Aggregation**
```python
from functools import reduce

def find_max(numbers):
    """Find maximum using reduce."""
    return reduce(lambda x, y: x if x > y else y, numbers)

def factorial(n):
    """Calculate factorial using reduce."""
    return reduce(lambda x, y: x * y, range(1, n + 1))
```

## 💡 Best Practices

### **Function Design Principles**

#### **Single Responsibility**
```python
# Good: Each function has one clear purpose
def calculate_tax(income, rate):
    return income * rate

def format_currency(amount):
    return f"${amount:.2f}"

def display_tax_info(income, rate):
    tax = calculate_tax(income, rate)
    print(f"Tax: {format_currency(tax)}")
```

#### **Pure Functions (No Side Effects)**
```python
# Good: Pure function - same input always gives same output
def calculate_discount(price, discount_rate):
    return price * (1 - discount_rate)

# Avoid: Function with side effects
def calculate_discount_bad(price, discount_rate):
    print(f"Calculating discount...")  # Side effect
    global total_discounts
    total_discounts += 1  # Side effect
    return price * (1 - discount_rate)
```

#### **Clear Parameter Names**
```python
# Good: Descriptive parameter names
def send_email(recipient_email, subject, message_body, sender_email=None):
    pass

# Avoid: Unclear parameter names
def send_email(to, subj, msg, frm=None):
    pass
```

### **Performance Tips**

#### **Use Built-in Functions**
```python
# Fast: Use built-in sum()
total = sum(numbers)

# Slower: Manual loop
total = 0
for num in numbers:
    total += num
```

#### **List Comprehensions vs Loops**
```python
# Fast: List comprehension
squares = [x**2 for x in numbers]

# Slower: Manual loop with append
squares = []
for x in numbers:
    squares.append(x**2)
```

#### **Avoid Repeated Calculations**
```python
# Good: Calculate once
length = len(data)
for i in range(length):
    process(data[i])

# Avoid: Repeated calculation
for i in range(len(data)):  # len() called every iteration
    process(data[i])
```

## 🔗 What's Next?

After mastering functions, you'll be ready for:

- **[05_modules_packages/](../05_modules_packages/)** - Code organization and imports
- **[06_oop/](../06_oop/)** - Object-oriented programming concepts
- **[07_advanced_concepts/](../07_advanced_concepts/)** - Decorators, generators, and more

## 📖 Additional Resources

### **Official Documentation:**
- [Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Built-in Functions](https://docs.python.org/3/library/functions.html)
- [Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)

### **Advanced Topics:**
- Function annotations and type hints
- Async functions and coroutines
- Partial functions with `functools.partial`
- Method resolution order in inheritance

## 🤔 Common Questions

### **"When should I use lambda vs regular functions?"**
- **Lambda**: For simple, one-line functions used immediately (map, filter, sort key)
- **Regular functions**: For complex logic, reusable code, or when you need documentation

### **"What's the difference between *args and **kwargs?"**
- **\*args**: Captures extra positional arguments as a tuple
- **\*\*kwargs**: Captures extra keyword arguments as a dictionary

### **"How do I avoid the mutable default argument trap?"**
```python
# Wrong: Mutable default argument
def bad_function(items=[]):  # Don't do this!
    items.append("new")
    return items

# Right: Use None and create new object
def good_function(items=None):
    if items is None:
        items = []
    items.append("new")
    return items
```

### **"When should I use global variables?"**
- **Avoid global variables** when possible
- **Use function parameters** to pass data
- **Return values** instead of modifying globals
- **Consider classes** for shared state

## 🛠️ Practice Projects

Try building these projects to reinforce your learning:

### **Beginner Projects**
- **Calculator Module**: Create functions for different operations
- **Text Processor**: Functions for string manipulation and analysis
- **Unit Converter**: Temperature, distance, weight conversion functions
- **Grade Calculator**: Functions for different grading schemes

### **Intermediate Projects**
- **Data Validator**: Create validation functions for different data types
- **File Processor**: Functions to read, process, and write different file formats
- **Math Library**: Implement mathematical functions and operations
- **Configuration Manager**: Functions to handle application settings

### **Advanced Projects**
- **Event System**: Implement callback-based event handling
- **Data Pipeline**: Create functional programming data processing pipeline
- **Plugin System**: Use higher-order functions for extensible architecture
- **Memoization Library**: Implement caching for expensive function calls

## 🎯 Key Takeaways

### **Function Fundamentals**
1. **Functions are first-class objects** in Python - they can be assigned, passed, and returned
2. **Parameters vs Arguments**: Parameters are in definition, arguments are in calls
3. **Scope matters**: Understand local, global, and nonlocal scope rules
4. **Documentation is crucial**: Use docstrings to explain function purpose and usage

### **Advanced Concepts**
1. **Flexibility with \*args and \*\*kwargs**: Create functions that accept variable arguments
2. **Lambda functions**: Perfect for short, simple operations in functional programming
3. **Closures**: Functions that remember their enclosing scope
4. **Higher-order functions**: Functions that work with other functions

### **Design Principles**
1. **Single responsibility**: Each function should do one thing well
2. **Pure functions**: Avoid side effects when possible
3. **Clear interfaces**: Use descriptive names and handle edge cases
4. **Reusability**: Write functions that can be used in multiple contexts

---

**Ready to master Python functions? Start with `01_function_basics.py` and build your functional programming skills! 🔧**

*Remember: Good functions are the building blocks of maintainable, scalable Python programs!*