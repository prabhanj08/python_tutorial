# 05. Modules and Packages 📦

**Learn how to organize and structure your Python code effectively**

## 📋 Overview

This module covers Python's module and package system, which is essential for organizing code, managing dependencies, and creating reusable components. You'll learn how to create, import, and distribute Python modules and packages.

## 🎯 Learning Objectives

By the end of this module, you will be able to:
- Understand the difference between modules and packages
- Create and import custom modules
- Work with built-in Python modules
- Organize code into packages
- Manage dependencies with package managers
- Set up and use virtual environments
- Understand Python's import system

## 📚 Topics Covered

### 1. **[01_modules.py](01_modules.py)** - Working with Modules
- What are modules?
- Creating custom modules
- Importing modules (import, from...import, as)
- Built-in modules exploration
- Module search path
- `__name__ == "__main__"` pattern

### 2. **[02_packages.py](02_packages.py)** - Creating and Using Packages
- What are packages?
- Creating package structure
- `__init__.py` files
- Subpackages and nested packages
- Relative vs absolute imports
- Package distribution basics

### 3. **[03_package_managers.py](03_package_managers.py)** - Package Management
- Introduction to pip
- Installing and managing packages
- requirements.txt files
- Introduction to conda and poetry
- Package versioning and dependencies
- Publishing packages to PyPI

### 4. **[04_virtual_environments.py](04_virtual_environments.py)** - Virtual Environments
- Why use virtual environments?
- Creating virtual environments with venv
- Activating and deactivating environments
- Managing project dependencies
- Best practices for environment management

## 🚀 Getting Started

1. **Read the concepts** in each Python file
2. **Run the examples** to see modules and packages in action
3. **Complete the exercises** to practice organizing code
4. **Build the mini-project** to apply your knowledge

## 💡 Key Concepts

### Module vs Package
- **Module**: A single Python file containing code
- **Package**: A directory containing multiple modules with an `__init__.py` file

### Import Strategies
```python
import module_name                    # Import entire module
from module_name import function     # Import specific function
from module_name import *            # Import all (not recommended)
import module_name as alias          # Import with alias
```

### Virtual Environment Benefits
- Isolated dependencies per project
- Avoid version conflicts
- Clean project setup
- Reproducible environments

## 🛠️ Practical Exercises

### Exercise 1: Create a Math Utilities Module
Create a module with mathematical functions and import them in different ways.

### Exercise 2: Build a Package Structure
Create a package with multiple modules and demonstrate imports.

### Exercise 3: Dependency Management
Set up a virtual environment and manage project dependencies.

### Exercise 4: Package Distribution
Create a simple package ready for distribution.

## 🎯 Mini-Project: Personal Library Package

Create a personal utility package with the following structure:
```
my_utils/
├── __init__.py
├── math_tools/
│   ├── __init__.py
│   ├── calculations.py
│   └── statistics.py
├── text_tools/
│   ├── __init__.py
│   ├── formatters.py
│   └── validators.py
└── file_tools/
    ├── __init__.py
    └── handlers.py
```

## 🔗 What's Next?

After mastering modules and packages, you'll move on to:
- **[06_oop/](../06_oop/)** - Object-Oriented Programming
- Advanced code organization patterns
- Design patterns and architecture

## 📖 Additional Resources

- [Python Module Documentation](https://docs.python.org/3/tutorial/modules.html)
- [Python Package Index (PyPI)](https://pypi.org/)
- [Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)

---

**Remember**: Good code organization is the foundation of maintainable software! 🏗️