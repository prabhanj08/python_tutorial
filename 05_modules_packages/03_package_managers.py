"""
05. Modules and Packages - Package Management
============================================

Package managers help you install, update, and manage Python packages and their dependencies.
This module covers pip, conda, poetry, and best practices for dependency management.

Topics covered:
- Introduction to pip (Python Package Installer)
- Installing and managing packages
- requirements.txt files
- Introduction to conda and poetry
- Package versioning and dependencies
- Publishing packages to PyPI
"""

import subprocess
import sys
import os
import json
from pathlib import Path

print("=" * 60)
print("PYTHON PACKAGE MANAGERS - MANAGING DEPENDENCIES")
print("=" * 60)

# =============================================================================
# 1. UNDERSTANDING PACKAGE MANAGERS
# =============================================================================

print("\n1. UNDERSTANDING PACKAGE MANAGERS")
print("-" * 30)

print("Package managers help you:")
print("- Install packages from repositories")
print("- Manage package versions")
print("- Handle dependencies automatically")
print("- Create reproducible environments")
print("- Publish your own packages")

print("\nMain Python package managers:")
print("1. pip - Default Python package installer")
print("2. conda - Cross-platform package manager")
print("3. poetry - Modern dependency management")
print("4. pipenv - Combines pip and virtualenv")

# =============================================================================
# 2. PIP - PYTHON PACKAGE INSTALLER
# =============================================================================

print("\n2. PIP - PYTHON PACKAGE INSTALLER")
print("-" * 30)

def run_command(command, capture_output=True):
    """Run a command and return the result"""
    try:
        if capture_output:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.stdout.strip(), result.stderr.strip(), result.returncode
        else:
            result = subprocess.run(command, shell=True)
            return "", "", result.returncode
    except Exception as e:
        return "", str(e), 1

# Check pip version
print("Checking pip installation:")
stdout, stderr, returncode = run_command("pip --version")
if returncode == 0:
    print(f"✓ pip is installed: {stdout}")
else:
    print(f"✗ pip not found: {stderr}")

# Show pip help
print(f"\nCommon pip commands:")
print("pip install <package>     - Install a package")
print("pip install <package>==<version> - Install specific version")
print("pip uninstall <package>   - Uninstall a package")
print("pip list                  - List installed packages")
print("pip show <package>        - Show package information")
print("pip freeze                - List packages with versions")
print("pip search <term>         - Search for packages (deprecated)")

# =============================================================================
# 3. INSTALLING PACKAGES WITH PIP
# =============================================================================

print("\n3. INSTALLING PACKAGES WITH PIP")
print("-" * 30)

# List currently installed packages
print("Currently installed packages (first 10):")
stdout, stderr, returncode = run_command("pip list")
if returncode == 0:
    lines = stdout.split('\n')
    for line in lines[:12]:  # Show header + first 10 packages
        print(line)
else:
    print("Could not list packages")

# Show package information
print(f"\nPackage information example (requests):")
stdout, stderr, returncode = run_command("pip show requests")
if returncode == 0:
    print(stdout[:500] + "..." if len(stdout) > 500 else stdout)
else:
    print("requests package not installed")

# =============================================================================
# 4. REQUIREMENTS.TXT FILES
# =============================================================================

print("\n4. REQUIREMENTS.TXT FILES")
print("-" * 30)

print("requirements.txt is a file listing project dependencies")

# Create a sample requirements.txt
requirements_content = """# Web framework
flask==2.3.3
requests>=2.25.0

# Data processing
pandas>=1.3.0
numpy>=1.21.0

# Testing
pytest>=6.0.0
pytest-cov>=2.12.0

# Development tools
black>=21.0.0
flake8>=3.9.0

# Optional dependencies
matplotlib>=3.4.0  # For plotting
beautifulsoup4>=4.9.0  # For web scraping

# Git dependencies (example)
# git+https://github.com/user/repo.git

# Local dependencies (example)
# -e ./local_package
"""

with open("requirements.txt", "w") as f:
    f.write(requirements_content)

print("Created sample requirements.txt:")
print(requirements_content)

print("Usage:")
print("pip install -r requirements.txt    # Install all dependencies")
print("pip freeze > requirements.txt      # Generate requirements from current env")

# =============================================================================
# 5. ADVANCED PIP USAGE
# =============================================================================

print("\n5. ADVANCED PIP USAGE")
print("-" * 30)

print("Advanced pip commands:")
print("pip install --upgrade <package>    # Upgrade package")
print("pip install --user <package>       # Install for current user only")
print("pip install -e .                   # Install package in development mode")
print("pip install --no-deps <package>    # Install without dependencies")
print("pip install --force-reinstall <package>  # Force reinstall")

# Create a sample setup.py for development installation
setup_py_content = '''from setuptools import setup, find_packages

setup(
    name="my-dev-package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "click>=7.0",
    ],
    entry_points={
        'console_scripts': [
            'my-tool=my_package.cli:main',
        ],
    },
)'''

with open("setup.py", "w") as f:
    f.write(setup_py_content)

print(f"\nCreated setup.py for development installation")
print("Use 'pip install -e .' to install in development mode")

# =============================================================================
# 6. CONDA PACKAGE MANAGER
# =============================================================================

print("\n6. CONDA PACKAGE MANAGER")
print("-" * 30)

print("Conda is a cross-platform package manager that can install packages")
print("from multiple languages (Python, R, C++, etc.)")

# Check if conda is available
stdout, stderr, returncode = run_command("conda --version")
if returncode == 0:
    print(f"✓ Conda is available: {stdout}")
    
    print(f"\nCommon conda commands:")
    print("conda install <package>         # Install package")
    print("conda create -n <name> python   # Create environment")
    print("conda activate <name>           # Activate environment")
    print("conda deactivate                # Deactivate environment")
    print("conda list                      # List packages")
    print("conda env list                  # List environments")
    print("conda remove <package>          # Remove package")
    
else:
    print("✗ Conda not available")
    print("Conda can be installed via Anaconda or Miniconda")

# Create environment.yml example
environment_yml = """name: my-project
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.9
  - numpy>=1.21
  - pandas>=1.3
  - matplotlib>=3.4
  - pip
  - pip:
    - flask>=2.0
    - requests>=2.25
"""

with open("environment.yml", "w") as f:
    f.write(environment_yml)

print(f"\nCreated environment.yml for conda:")
print("conda env create -f environment.yml  # Create environment from file")

# =============================================================================
# 7. POETRY PACKAGE MANAGER
# =============================================================================

print("\n7. POETRY PACKAGE MANAGER")
print("-" * 30)

print("Poetry is a modern dependency management tool that handles:")
print("- Dependency resolution")
print("- Virtual environment management")
print("- Package building and publishing")

# Check if poetry is available
stdout, stderr, returncode = run_command("poetry --version")
if returncode == 0:
    print(f"✓ Poetry is available: {stdout}")
    
    print(f"\nCommon poetry commands:")
    print("poetry init                     # Initialize new project")
    print("poetry add <package>            # Add dependency")
    print("poetry install                  # Install dependencies")
    print("poetry shell                    # Activate virtual environment")
    print("poetry run <command>            # Run command in environment")
    print("poetry build                    # Build package")
    print("poetry publish                  # Publish to PyPI")
    
else:
    print("✗ Poetry not available")
    print("Install with: curl -sSL https://install.python-poetry.org | python3 -")

# Create pyproject.toml example
pyproject_toml = """[tool.poetry]
name = "my-awesome-project"
version = "0.1.0"
description = "An awesome Python project"
authors = ["Your Name <you@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.8"
requests = "^2.25.0"
click = "^8.0.0"
pandas = {version = "^1.3.0", optional = true}

[tool.poetry.group.dev.dependencies]
pytest = "^6.0.0"
black = "^21.0.0"
flake8 = "^3.9.0"

[tool.poetry.extras]
data = ["pandas", "numpy"]

[tool.poetry.scripts]
my-cli = "my_project.cli:main"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
"""

with open("pyproject.toml", "w") as f:
    f.write(pyproject_toml)

print(f"\nCreated pyproject.toml for Poetry")

# =============================================================================
# 8. PACKAGE VERSIONING
# =============================================================================

print("\n8. PACKAGE VERSIONING")
print("-" * 30)

print("Version specifiers:")
print("==1.4.2    # Exactly version 1.4.2")
print(">=1.4.2    # Version 1.4.2 or higher")
print("~=1.4.2    # Compatible release (>=1.4.2, <1.5.0)")
print(">=1.4,<2.0 # Version range")
print("!=1.5      # Any version except 1.5")

print(f"\nSemantic Versioning (SemVer):")
print("MAJOR.MINOR.PATCH")
print("- MAJOR: Incompatible API changes")
print("- MINOR: Backwards-compatible functionality")
print("- PATCH: Backwards-compatible bug fixes")

# =============================================================================
# 9. PUBLISHING PACKAGES
# =============================================================================

print("\n9. PUBLISHING PACKAGES TO PYPI")
print("-" * 30)

print("Steps to publish a package:")
print("1. Create account on PyPI (https://pypi.org)")
print("2. Install twine: pip install twine")
print("3. Build package: python setup.py sdist bdist_wheel")
print("4. Upload to TestPyPI first: twine upload --repository testpypi dist/*")
print("5. Test installation from TestPyPI")
print("6. Upload to PyPI: twine upload dist/*")

# Create a complete package structure example
package_structure = """
my_package/
├── my_package/
│   ├── __init__.py
│   ├── core.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   └── test_utils.py
├── docs/
│   └── README.md
├── setup.py
├── setup.cfg
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
├── MANIFEST.in
├── LICENSE
└── README.md
"""

print(f"\nRecommended package structure:")
print(package_structure)

# =============================================================================
# 10. BEST PRACTICES
# =============================================================================

print("\n10. BEST PRACTICES")
print("-" * 30)

print("Dependency management best practices:")
print("1. Use virtual environments for each project")
print("2. Pin exact versions in production (requirements.txt)")
print("3. Use version ranges in libraries (setup.py)")
print("4. Separate development and production dependencies")
print("5. Regularly update dependencies")
print("6. Use dependency scanning tools")
print("7. Document installation instructions")
print("8. Test with multiple Python versions")

# Create different requirements files
requirements_dev = """# Development dependencies
pytest>=6.0.0
pytest-cov>=2.12.0
black>=21.0.0
flake8>=3.9.0
mypy>=0.910
pre-commit>=2.15.0

# Documentation
sphinx>=4.0.0
sphinx-rtd-theme>=0.5.0
"""

with open("requirements-dev.txt", "w") as f:
    f.write(requirements_dev)

requirements_prod = """# Production dependencies (pinned versions)
flask==2.3.3
requests==2.31.0
pandas==1.5.3
numpy==1.24.3
gunicorn==20.1.0
"""

with open("requirements-prod.txt", "w") as f:
    f.write(requirements_prod)

print("Created requirements-dev.txt and requirements-prod.txt")

# =============================================================================
# EXERCISES
# =============================================================================

print("\n" + "=" * 60)
print("EXERCISES")
print("=" * 60)

print("""
Exercise 1: Package Installation Practice
- Create a virtual environment
- Install requests, pandas, and matplotlib
- Generate a requirements.txt file
- Create a new environment and install from requirements.txt

Exercise 2: Dependency Analysis
- Choose a popular package (e.g., django, flask, numpy)
- Use 'pip show' to examine its dependencies
- Create a dependency tree diagram
- Identify potential version conflicts

Exercise 3: Package Creation
- Create a simple package with setup.py
- Include dependencies in setup.py
- Install in development mode with 'pip install -e .'
- Test importing your package

Exercise 4: Version Management
- Create requirements.txt with different version specifiers
- Test installing with different version constraints
- Understand when to use ==, >=, ~=, etc.

Exercise 5: Publishing Preparation
- Create a complete package structure
- Write setup.py with proper metadata
- Create README.md and LICENSE files
- Build the package (don't publish to PyPI)
""")

# =============================================================================
# SOLUTIONS (Uncomment to see solutions)
# =============================================================================

print("\n" + "=" * 60)
print("EXERCISE SOLUTIONS")
print("=" * 60)

# Solution 1: Package Installation Practice
print("\nSolution 1: Virtual Environment and Requirements")
print("Commands to run:")
print("python -m venv myenv")
print("source myenv/bin/activate  # On Windows: myenv\\Scripts\\activate")
print("pip install requests pandas matplotlib")
print("pip freeze > my_requirements.txt")

# Solution 3: Simple Package Creation
print("\nSolution 3: Simple Package Creation")

# Create a simple package
simple_package_dir = "simple_calculator"
os.makedirs(simple_package_dir, exist_ok=True)

# Package __init__.py
simple_init = '''"""
Simple Calculator Package
"""

__version__ = "1.0.0"

from .calculator import Calculator
from .operations import add, subtract, multiply, divide

__all__ = ['Calculator', 'add', 'subtract', 'multiply', 'divide']
'''

with open(f"{simple_package_dir}/__init__.py", "w") as f:
    f.write(simple_init)

# Operations module
operations_content = '''"""
Basic mathematical operations
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
'''

with open(f"{simple_package_dir}/operations.py", "w") as f:
    f.write(operations_content)

# Calculator class
calculator_content = '''"""
Calculator class
"""

from .operations import add, subtract, multiply, divide

class Calculator:
    """A simple calculator class"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = add(a, b)
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = subtract(a, b)
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = multiply(a, b)
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        result = divide(a, b)
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self):
        return self.history.copy()
    
    def clear_history(self):
        self.history.clear()
'''

with open(f"{simple_package_dir}/calculator.py", "w") as f:
    f.write(calculator_content)

# Setup.py for the package
simple_setup = '''from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="simple-calculator",
    version="1.0.0",
    author="Python Learner",
    author_email="learner@example.com",
    description="A simple calculator package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/username/simple-calculator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        # No external dependencies for this simple package
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.9",
        ],
    },
)'''

with open("simple_setup.py", "w") as f:
    f.write(simple_setup)

# README for the package
readme_content = '''# Simple Calculator

A simple Python calculator package for basic mathematical operations.

## Installation

```bash
pip install simple-calculator
```

## Usage

```python
from simple_calculator import Calculator, add

# Using functions directly
result = add(5, 3)
print(result)  # 8

# Using Calculator class
calc = Calculator()
result = calc.add(10, 5)
print(result)  # 15
print(calc.get_history())  # ['10 + 5 = 15']
```

## Features

- Basic arithmetic operations (add, subtract, multiply, divide)
- Calculator class with operation history
- Zero division error handling

## License

MIT License
'''

with open("README.md", "w") as f:
    f.write(readme_content)

print("Created simple_calculator package with:")
print("- Package structure")
print("- setup.py with metadata")
print("- README.md documentation")

# Test the package
try:
    sys.path.insert(0, '.')
    import simple_calculator
    
    calc = simple_calculator.Calculator()
    result1 = calc.add(10, 5)
    result2 = calc.multiply(3, 4)
    
    print(f"\nTesting simple_calculator package:")
    print(f"10 + 5 = {result1}")
    print(f"3 * 4 = {result2}")
    print(f"History: {calc.get_history()}")
    
except ImportError as e:
    print(f"Could not test package: {e}")

# Clean up created files
cleanup_files = [
    "requirements.txt", "requirements-dev.txt", "requirements-prod.txt",
    "setup.py", "environment.yml", "pyproject.toml", "simple_setup.py",
    "README.md"
]

cleanup_dirs = ["simple_calculator"]

print(f"\nCleaning up created files...")
for file in cleanup_files:
    try:
        if os.path.exists(file):
            os.remove(file)
    except:
        pass

for dir_name in cleanup_dirs:
    try:
        if os.path.exists(dir_name):
            import shutil
            shutil.rmtree(dir_name)
    except:
        pass

print("\n" + "=" * 60)
print("PACKAGE MANAGERS MODULE COMPLETE!")
print("=" * 60)
print("Key takeaways:")
print("1. pip is the standard Python package installer")
print("2. requirements.txt manages project dependencies")
print("3. Use virtual environments to isolate dependencies")
print("4. Poetry and conda offer advanced dependency management")
print("5. Semantic versioning helps manage compatibility")
print("6. Proper setup.py enables package distribution")