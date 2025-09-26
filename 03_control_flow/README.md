# Python Control Flow - Decision Making and Repetition

Welcome to the Python Control Flow section! This folder covers the fundamental concepts that allow your programs to make decisions and repeat actions based on conditions.

## 📚 What You'll Learn

This section covers Python's control flow mechanisms:

- **Conditionals** - Making decisions with if, elif, else
- **Loops** - Repeating actions with for and while loops
- **Loop Control** - Managing loop execution with break, continue, pass
- **Advanced Iteration** - Using enumerate, zip, and comprehensions

## 📁 Files in This Section

### 1. [`01_conditionals.py`](01_conditionals.py)
**Decision Making with If Statements**
- Basic if, elif, else statements
- Comparison and logical operators
- Boolean expressions and truthiness
- Nested conditionals and best practices
- Conditional expressions (ternary operator)
- Real-world decision-making examples

**Key Concepts:**
```python
# Basic conditional structure
if condition:
    # Execute if condition is True
    pass
elif another_condition:
    # Execute if another_condition is True
    pass
else:
    # Execute if all conditions are False
    pass

# Ternary operator
result = "adult" if age >= 18 else "minor"

# Logical operators
if age >= 18 and has_license and has_insurance:
    print("Can drive legally")
```

**When to use Conditionals:**
- Making decisions based on user input
- Validating data before processing
- Implementing business logic rules
- Error handling and edge cases
- Creating branching program flows

### 2. [`02_loops.py`](02_loops.py)
**Repetition with For and While Loops**
- For loops for iterating over sequences
- While loops for condition-based repetition
- Loop control statements (break, continue, pass)
- Nested loops for complex iterations
- Loop with else clause
- Enumerate, zip, and range functions

**Key Concepts:**
```python
# For loop - iterate over sequences
for item in sequence:
    print(item)

# While loop - repeat while condition is true
while condition:
    # Do something
    # Update condition to avoid infinite loop
    pass

# Loop control
for item in items:
    if skip_condition:
        continue  # Skip to next iteration
    if stop_condition:
        break     # Exit loop completely
    
    # Process item

# Advanced iteration
for index, value in enumerate(items):
    print(f"{index}: {value}")

for a, b in zip(list1, list2):
    print(f"{a} + {b} = {a + b}")
```

**When to use Loops:**
- Processing collections of data
- Repeating actions until a condition is met
- Implementing algorithms that require iteration
- Menu-driven programs
- Data validation with retry logic

## 🎯 Learning Objectives

By the end of this section, you should be able to:

### **Conditionals**
- ✅ Write clear and efficient conditional statements
- ✅ Use comparison and logical operators effectively
- ✅ Understand truthiness and falsy values in Python
- ✅ Implement complex decision-making logic
- ✅ Apply conditional expressions for concise code

### **Loops**
- ✅ Choose between for and while loops appropriately
- ✅ Use loop control statements effectively
- ✅ Implement nested loops for complex problems
- ✅ Apply enumerate, zip, and range functions
- ✅ Optimize loop performance and readability

### **Control Flow Design**
- ✅ Design clear program flow structures
- ✅ Avoid common pitfalls like infinite loops
- ✅ Write maintainable and readable control structures
- ✅ Combine conditionals and loops effectively

## 🚀 Getting Started

### Prerequisites
- Completed [01_python_basics/](../01_python_basics/) and [02_data_structures/](../02_data_structures/)
- Understanding of variables, data types, and basic operations
- Familiarity with Python syntax and indentation

### How to Use These Files

1. **Start with `01_conditionals.py`** - Learn decision making
2. **Progress to `02_loops.py`** - Master repetition and iteration
3. **Run all code examples** - See control flow in action
4. **Complete the exercises** - Practice with real scenarios
5. **Combine concepts** - Use conditionals within loops and vice versa

### Running the Files

```bash
# Navigate to the folder
cd Python_learning/03_control_flow/

# Run each file to see examples
python 01_conditionals.py
python 02_loops.py
```

## 🔄 Control Flow Patterns

### **Common Conditional Patterns**

#### **Input Validation**
```python
def validate_age(age):
    if age < 0:
        return "Age cannot be negative"
    elif age > 150:
        return "Age seems unrealistic"
    elif age < 18:
        return "Minor"
    else:
        return "Adult"
```

#### **Multi-condition Checks**
```python
def check_access(user_role, is_active, has_permission):
    if not is_active:
        return "Account inactive"
    elif user_role == "admin":
        return "Full access"
    elif user_role == "user" and has_permission:
        return "Limited access"
    else:
        return "Access denied"
```

### **Common Loop Patterns**

#### **Data Processing**
```python
# Process each item in a collection
for item in data:
    processed_item = process(item)
    results.append(processed_item)
```

#### **Search and Find**
```python
# Find first matching item
for item in items:
    if matches_criteria(item):
        found_item = item
        break
else:
    found_item = None
```

#### **Accumulation**
```python
# Calculate running totals
total = 0
for value in values:
    total += value
```

#### **Menu Systems**
```python
while True:
    choice = get_user_choice()
    if choice == "quit":
        break
    elif choice == "option1":
        handle_option1()
    elif choice == "option2":
        handle_option2()
    else:
        print("Invalid choice")
```

## 💡 Best Practices

### **Conditionals**
- **Use early returns** to reduce nesting
- **Create descriptive boolean variables** for complex conditions
- **Avoid deep nesting** - use elif instead of nested if statements
- **Use truthiness** appropriately (empty lists, None, 0 are falsy)
- **Order conditions** from most specific to most general

### **Loops**
- **Use for loops** for known iterations (sequences, ranges)
- **Use while loops** for condition-based repetition
- **Always ensure loop termination** to avoid infinite loops
- **Use enumerate()** instead of range(len()) for indexing
- **Use zip()** to iterate over multiple sequences together
- **Consider list comprehensions** for simple transformations

### **Performance Tips**
- **List comprehensions** are often faster than equivalent loops
- **Break early** when you find what you're looking for
- **Use built-in functions** (sum, max, min) instead of manual loops when possible
- **Avoid modifying lists** while iterating over them

## 🔗 What's Next?

After mastering control flow, you'll be ready for:

- **[04_functions/](../04_functions/)** - Advanced function concepts and design
- **[05_modules_packages/](../05_modules_packages/)** - Code organization and imports
- **[06_oop/](../06_oop/)** - Object-oriented programming concepts

## 📖 Additional Resources

### **Official Documentation:**
- [Python Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Built-in Functions](https://docs.python.org/3/library/functions.html)
- [Compound Statements](https://docs.python.org/3/reference/compound_stmts.html)

### **Advanced Topics:**
- List, set, and dictionary comprehensions
- Generator expressions for memory efficiency
- Context managers and the `with` statement
- Exception handling in loops

## 🤔 Common Questions

### **"When should I use if vs elif vs else?"**
- **if**: First condition to check
- **elif**: Additional conditions to check (only if previous conditions were False)
- **else**: Default action when no conditions are met

### **"When should I use for vs while loops?"**
- **for loop**: When you know how many times to iterate or have a sequence to iterate over
- **while loop**: When you need to repeat until a condition becomes False

### **"How do I avoid infinite loops?"**
```python
# Always ensure the condition can become False
counter = 0
while counter < 10:  # Clear termination condition
    print(counter)
    counter += 1     # Always update the condition variable
```

### **"What's the difference between break and continue?"**
- **break**: Exits the entire loop immediately
- **continue**: Skips the rest of the current iteration and goes to the next one

## 🛠️ Practice Projects

Try building these projects to reinforce your learning:

### **Beginner Projects**
- **Number Guessing Game**: Use while loops and conditionals
- **Grade Calculator**: Process student scores with loops and conditions
- **Simple Menu System**: Implement user choices with loops
- **Password Validator**: Check password strength with multiple conditions

### **Intermediate Projects**
- **Text Adventure Game**: Complex branching storylines
- **Data Filter**: Process and filter large datasets
- **Pattern Generator**: Create ASCII art with nested loops
- **Simple Calculator**: Menu-driven with input validation

### **Advanced Projects**
- **File Processor**: Read and process multiple files
- **Game of Life**: Implement Conway's cellular automaton
- **Sorting Algorithms**: Implement bubble sort, selection sort
- **Web Scraper**: Extract data with conditional logic

## 🎯 Key Takeaways

### **Control Flow Fundamentals**
1. **Conditionals** let your program make decisions
2. **Loops** let your program repeat actions efficiently
3. **Proper indentation** is crucial for Python control structures
4. **Loop control statements** provide fine-grained control over execution

### **Design Principles**
1. **Keep it simple** - avoid overly complex nested structures
2. **Be explicit** - use clear variable names and conditions
3. **Plan for edge cases** - handle unexpected inputs gracefully
4. **Optimize for readability** - code is read more often than written

---

**Ready to control your program's flow? Start with `01_conditionals.py` and master decision making! 🔀**

*Remember: Good control flow makes your programs more robust, readable, and maintainable!*