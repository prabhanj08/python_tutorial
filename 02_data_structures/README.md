# Python Data Structures - Core Collections

Welcome to the Python Data Structures section! This folder covers the four fundamental built-in data structures that form the backbone of Python programming.

## 📚 What You'll Learn

This section covers Python's core data structures and when to use each one:

- **Lists** - Ordered, mutable collections for sequences
- **Tuples** - Ordered, immutable collections for fixed data
- **Sets** - Unordered collections of unique elements
- **Dictionaries** - Key-value pairs for mapping relationships

## 📁 Files in This Section

### 1. [`01_lists.py`](01_lists.py)
**Ordered, Mutable Collections**
- Creating and accessing lists
- List methods (append, extend, remove, pop)
- List slicing and indexing
- List comprehensions
- Sorting and searching
- Nested lists and practical examples

**Key Concepts:**
```python
# List creation and manipulation
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits[0] = "apricot"

# List comprehension
squares = [x**2 for x in range(10) if x % 2 == 0]

# List methods
fruits.sort()
fruits.reverse()
```

**When to use Lists:**
- Storing ordered sequences of items
- When you need to modify the collection
- When order matters and duplicates are allowed
- For homogeneous data that grows/shrinks

### 2. [`02_tuples.py`](02_tuples.py)
**Ordered, Immutable Collections**
- Creating tuples and tuple packing/unpacking
- Accessing tuple elements
- Tuple methods (count, index)
- Named tuples for structured data
- Nested tuples and practical applications
- Performance benefits of immutability

**Key Concepts:**
```python
# Tuple creation
coordinates = (10, 20)
person = "Alice", 25, "Engineer"  # Tuple packing

# Tuple unpacking
name, age, job = person
x, y = coordinates

# Named tuples
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
```

**When to use Tuples:**
- Storing fixed collections that won't change
- Representing coordinates, database records
- Function returns with multiple values
- Dictionary keys (tuples are hashable)
- When performance is critical

### 3. [`03_sets.py`](03_sets.py)
**Unordered Collections of Unique Elements**
- Creating sets and set operations
- Mathematical set operations (union, intersection, difference)
- Adding and removing elements
- Set comprehensions
- Frozen sets for immutable collections
- Membership testing and deduplication

**Key Concepts:**
```python
# Set creation and operations
numbers = {1, 2, 3, 4, 5}
evens = {2, 4, 6, 8}

# Set operations
union = numbers | evens
intersection = numbers & evens
difference = numbers - evens

# Set comprehension
squares = {x**2 for x in range(10)}

# Membership testing (very fast)
if 3 in numbers:
    print("Found!")
```

**When to use Sets:**
- Removing duplicates from collections
- Fast membership testing
- Mathematical set operations
- When order doesn't matter
- Storing unique identifiers

### 4. [`04_dictionaries.py`](04_dictionaries.py)
**Key-Value Pairs for Mapping**
- Creating and accessing dictionaries
- Dictionary methods and operations
- Dictionary comprehensions
- Nested dictionaries for complex data
- Dictionary views and iteration patterns
- Performance characteristics

**Key Concepts:**
```python
# Dictionary creation and access
student = {"name": "Alice", "age": 20, "grade": "A"}
print(student["name"])
print(student.get("gpa", "Not Available"))

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}

# Nested dictionaries
students = {
    "alice": {"age": 20, "grades": {"math": 85, "science": 92}},
    "bob": {"age": 19, "grades": {"math": 78, "science": 85}}
}

# Dictionary methods
for key, value in student.items():
    print(f"{key}: {value}")
```

**When to use Dictionaries:**
- Mapping relationships between data
- Fast lookups by key
- Storing structured data
- Configuration settings
- Caching and memoization

## 🎯 Learning Objectives

By the end of this section, you should be able to:

### **Data Structure Selection**
- ✅ Choose the right data structure for specific use cases
- ✅ Understand performance characteristics of each structure
- ✅ Know when mutability vs immutability matters
- ✅ Understand ordered vs unordered collections

### **Lists**
- ✅ Create and manipulate lists effectively
- ✅ Use list methods and comprehensions
- ✅ Handle nested lists and complex data
- ✅ Optimize list operations for performance

### **Tuples**
- ✅ Use tuples for immutable data
- ✅ Apply tuple packing and unpacking
- ✅ Work with named tuples for structured data
- ✅ Understand when tuples are better than lists

### **Sets**
- ✅ Perform set operations for data analysis
- ✅ Use sets for deduplication and membership testing
- ✅ Apply mathematical set operations
- ✅ Choose between sets and frozensets

### **Dictionaries**
- ✅ Design effective key-value mappings
- ✅ Use dictionary methods and comprehensions
- ✅ Handle nested dictionaries and complex structures
- ✅ Optimize dictionary usage patterns

## 🚀 Getting Started

### Prerequisites
- Completed [01_python_basics/](../01_python_basics/)
- Understanding of variables and basic operations
- Familiarity with Python syntax

### How to Use These Files

1. **Start with `01_lists.py`** - Foundation for all collections
2. **Progress through each file sequentially** - Each builds understanding
3. **Run all code examples** - See data structures in action
4. **Complete the exercises** - Practice with real scenarios
5. **Compare and contrast** - Understand when to use each structure

### Running the Files

```bash
# Navigate to the folder
cd Python_learning/02_data_structures/

# Run each file to see examples
python 01_lists.py
python 02_tuples.py
python 03_sets.py
python 04_dictionaries.py
```

## 📊 Data Structure Comparison

| Feature | List | Tuple | Set | Dictionary |
|---------|------|-------|-----|------------|
| **Ordered** | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes (3.7+) |
| **Mutable** | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| **Duplicates** | ✅ Allowed | ✅ Allowed | ❌ No | ❌ Keys: No, Values: Yes |
| **Indexed** | ✅ Yes | ✅ Yes | ❌ No | ✅ By key |
| **Use Case** | Sequences | Fixed data | Unique items | Key-value mapping |

## 💡 Performance Tips

### **Lists**
- Use list comprehensions instead of loops when possible
- `append()` is faster than `insert(0, item)` for adding elements
- Use `collections.deque` for frequent insertions at both ends

### **Tuples**
- Faster than lists for read-only operations
- Use for fixed data that won't change
- Great for function returns and unpacking

### **Sets**
- Extremely fast membership testing: O(1) average
- Use for deduplication and mathematical operations
- Convert to list only when ordering is needed

### **Dictionaries**
- Fast key lookups: O(1) average
- Use `get()` method for safe access
- Dictionary comprehensions are efficient for transformations

## 🔗 What's Next?

After mastering data structures, you'll be ready for:

- **[03_control_flow/](../03_control_flow/)** - Conditionals and loops with data structures
- **[04_functions/](../04_functions/)** - Advanced functions working with collections
- **[05_modules_packages/](../05_modules_packages/)** - Organizing code and importing collections

## 📖 Additional Resources

### **Official Documentation:**
- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Collections Module](https://docs.python.org/3/library/collections.html)

### **Advanced Topics:**
- `collections.defaultdict` - Dictionaries with default values
- `collections.Counter` - Counting hashable objects
- `collections.OrderedDict` - Ordered dictionaries (pre-3.7)
- `collections.deque` - Double-ended queues

## 🤔 Common Questions

### **"Which data structure should I use?"**
- **List**: When you need ordered, changeable data
- **Tuple**: When you need ordered, unchangeable data
- **Set**: When you need unique items and fast membership testing
- **Dictionary**: When you need to map keys to values

### **"Can I convert between data structures?"**
```python
# Converting between structures
my_list = [1, 2, 3, 2, 1]
my_tuple = tuple(my_list)        # (1, 2, 3, 2, 1)
my_set = set(my_list)            # {1, 2, 3} - duplicates removed
my_dict = dict(enumerate(my_list)) # {0: 1, 1: 2, 2: 3, 3: 2, 4: 1}
```

### **"How do I choose between list and tuple?"**
- Use **list** when data might change
- Use **tuple** when data is fixed (coordinates, database records)
- Use **tuple** for better performance with read-only data

### **"When should I use sets vs lists?"**
- Use **sets** for unique items and fast membership testing
- Use **lists** when order matters or duplicates are needed
- Use **sets** for mathematical operations (union, intersection)

## 🛠️ Practice Projects

Try building these projects to reinforce your learning:

### **Beginner Projects**
- **Contact Book**: Use dictionaries to store contact information
- **Shopping List**: Use lists with add/remove functionality
- **Grade Calculator**: Use nested dictionaries for student grades
- **Word Counter**: Use dictionaries to count word frequencies

### **Intermediate Projects**
- **Inventory System**: Combine all data structures for product management
- **Student Database**: Use nested structures for complex data relationships
- **Data Analyzer**: Process CSV-like data using appropriate structures
- **Game Scoreboard**: Track high scores using sorted data structures

---

**Ready to master Python's data structures? Start with `01_lists.py` and build your foundation! 📊**

*Remember: The right data structure can make your code more efficient, readable, and maintainable. Choose wisely!*