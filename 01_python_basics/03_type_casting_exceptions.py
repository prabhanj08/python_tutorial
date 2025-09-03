"""
Python Basics - Type Casting and Basic Exceptions
=================================================

This module covers type conversion (casting) and basic exception handling in Python.
Understanding how to convert between data types and handle errors is fundamental
for writing robust Python programs.

Key Concepts Covered:
- Implicit and explicit type conversion
- Built-in type casting functions
- Common type conversion scenarios
- Basic exception handling
- Common exception types
"""

# ============================================================================
# 1. TYPE CASTING FUNDAMENTALS
# ============================================================================

print("Type Casting in Python")
print("=" * 30)

# Type casting (type conversion) is the process of converting one data type to another
# Python supports both implicit and explicit type conversion

# ============================================================================
# 2. IMPLICIT TYPE CONVERSION (AUTOMATIC)
# ============================================================================

print("\n1. Implicit Type Conversion:")
print("-" * 30)

# Python automatically converts data types when needed
num_int = 123
num_float = 1.23

# When int and float are used together, int is converted to float
result = num_int + num_float
print(f"Integer: {num_int} (type: {type(num_int).__name__})")
print(f"Float: {num_float} (type: {type(num_float).__name__})")
print(f"Result: {result} (type: {type(result).__name__})")

# Boolean to integer conversion
bool_val = True
int_val = 10
result2 = bool_val + int_val  # True is treated as 1
print(f"\nBoolean + Integer: {bool_val} + {int_val} = {result2}")

# ============================================================================
# 3. EXPLICIT TYPE CONVERSION (MANUAL)
# ============================================================================

print("\n2. Explicit Type Conversion:")
print("-" * 30)

# 3.1 Converting to Integer - int()
print("Converting to Integer:")
float_num = 3.14
str_num = "42"
bool_val = True

int_from_float = int(float_num)    # Truncates decimal part
int_from_str = int(str_num)        # Converts string to int
int_from_bool = int(bool_val)      # True = 1, False = 0

print(f"float {float_num} -> int: {int_from_float}")
print(f"string '{str_num}' -> int: {int_from_str}")
print(f"boolean {bool_val} -> int: {int_from_bool}")

# 3.2 Converting to Float - float()
print("\nConverting to Float:")
int_num = 42
str_float = "3.14"
bool_val = False

float_from_int = float(int_num)
float_from_str = float(str_float)
float_from_bool = float(bool_val)

print(f"int {int_num} -> float: {float_from_int}")
print(f"string '{str_float}' -> float: {float_from_str}")
print(f"boolean {bool_val} -> float: {float_from_bool}")

# 3.3 Converting to String - str()
print("\nConverting to String:")
num = 123
float_val = 45.67
bool_val = True
list_val = [1, 2, 3]

str_from_int = str(num)
str_from_float = str(float_val)
str_from_bool = str(bool_val)
str_from_list = str(list_val)

print(f"int {num} -> string: '{str_from_int}'")
print(f"float {float_val} -> string: '{str_from_float}'")
print(f"boolean {bool_val} -> string: '{str_from_bool}'")
print(f"list {list_val} -> string: '{str_from_list}'")

# 3.4 Converting to Boolean - bool()
print("\nConverting to Boolean:")
# Falsy values: 0, 0.0, '', [], {}, None, False
# Everything else is truthy

values_to_test = [0, 1, -1, 0.0, 3.14, '', 'hello', [], [1, 2], {}, {'a': 1}, None]

for value in values_to_test:
    bool_result = bool(value)
    print(f"bool({repr(value)}) = {bool_result}")

# ============================================================================
# 4. ADVANCED TYPE CONVERSION
# ============================================================================

print("\n3. Advanced Type Conversion:")
print("-" * 30)

# 4.1 Converting between number bases
print("Number Base Conversion:")
decimal_num = 42

binary_str = bin(decimal_num)      # To binary string
octal_str = oct(decimal_num)       # To octal string
hex_str = hex(decimal_num)         # To hexadecimal string

print(f"Decimal {decimal_num}:")
print(f"  Binary: {binary_str}")
print(f"  Octal: {octal_str}")
print(f"  Hexadecimal: {hex_str}")

# Converting back from strings
print(f"\nConverting back:")
print(f"Binary '0b101010' to decimal: {int('0b101010', 2)}")
print(f"Octal '0o52' to decimal: {int('0o52', 8)}")
print(f"Hex '0x2a' to decimal: {int('0x2a', 16)}")

# 4.2 Converting collections
print("\nCollection Conversion:")
# String to list
text = "hello"
char_list = list(text)
print(f"String '{text}' to list: {char_list}")

# List to tuple
num_list = [1, 2, 3, 4]
num_tuple = tuple(num_list)
print(f"List {num_list} to tuple: {num_tuple}")

# List to set (removes duplicates)
duplicate_list = [1, 2, 2, 3, 3, 3]
unique_set = set(duplicate_list)
print(f"List {duplicate_list} to set: {unique_set}")

# ============================================================================
# 5. BASIC EXCEPTION HANDLING
# ============================================================================

print("\n4. Basic Exception Handling:")
print("-" * 30)

# Exceptions occur when Python encounters an error during execution
# Common exceptions during type conversion:

# 5.1 ValueError - Invalid conversion
print("ValueError Examples:")

try:
    # This will raise ValueError
    invalid_int = int("hello")
except ValueError as e:
    print(f"ValueError caught: {e}")

try:
    # This will also raise ValueError
    invalid_float = float("not_a_number")
except ValueError as e:
    print(f"ValueError caught: {e}")

# 5.2 TypeError - Incompatible types
print("\nTypeError Examples:")

try:
    # This will raise TypeError
    result = "hello" + 5
except TypeError as e:
    print(f"TypeError caught: {e}")

# 5.3 Safe type conversion with exception handling
print("\nSafe Type Conversion:")

def safe_int_conversion(value):
    """Safely convert a value to integer."""
    try:
        return int(value)
    except ValueError:
        print(f"Cannot convert '{value}' to integer")
        return None
    except TypeError:
        print(f"Invalid type for conversion: {type(value)}")
        return None

# Test safe conversion
test_values = ["123", "45.67", "hello", None, [1, 2, 3]]
for val in test_values:
    result = safe_int_conversion(val)
    print(f"safe_int_conversion({repr(val)}) = {result}")

# ============================================================================
# 6. PRACTICAL TYPE CONVERSION SCENARIOS
# ============================================================================

print("\n5. Practical Scenarios:")
print("-" * 30)

# 6.1 User input processing
def process_user_age():
    """Simulate processing user input for age."""
    user_input = "25"  # Simulating input() which always returns string
    
    try:
        age = int(user_input)
        if age < 0:
            print("Age cannot be negative")
        elif age > 150:
            print("Age seems unrealistic")
        else:
            print(f"User age: {age} years")
            return age
    except ValueError:
        print("Please enter a valid number for age")
        return None

process_user_age()

# 6.2 Data cleaning and validation
def clean_numeric_data(data_list):
    """Clean a list of mixed data types to extract numbers."""
    cleaned_numbers = []
    
    for item in data_list:
        try:
            # Try to convert to float first (handles both int and float strings)
            num = float(item)
            cleaned_numbers.append(num)
        except (ValueError, TypeError):
            print(f"Skipping non-numeric value: {repr(item)}")
    
    return cleaned_numbers

# Test data cleaning
messy_data = ["123", "45.67", "hello", "89", None, "3.14", "world", "0"]
clean_data = clean_numeric_data(messy_data)
print(f"\nOriginal data: {messy_data}")
print(f"Cleaned numbers: {clean_data}")

# 6.3 Configuration file processing
def parse_config_value(key, value):
    """Parse configuration values with appropriate type conversion."""
    # Define expected types for different config keys
    boolean_keys = ['debug', 'enabled', 'active']
    integer_keys = ['port', 'timeout', 'max_connections']
    float_keys = ['rate', 'threshold', 'percentage']
    
    try:
        if key.lower() in boolean_keys:
            # Handle various boolean representations
            if isinstance(value, str):
                return value.lower() in ['true', '1', 'yes', 'on']
            return bool(value)
        elif key.lower() in integer_keys:
            return int(value)
        elif key.lower() in float_keys:
            return float(value)
        else:
            return str(value)  # Default to string
    except (ValueError, TypeError) as e:
        print(f"Error parsing config {key}={value}: {e}")
        return None

# Test configuration parsing
config_data = {
    'debug': 'true',
    'port': '8080',
    'rate': '0.95',
    'name': 'MyApp',
    'enabled': '1',
    'invalid_port': 'not_a_number'
}

print(f"\nConfiguration Parsing:")
for key, value in config_data.items():
    parsed = parse_config_value(key, value)
    print(f"{key}: '{value}' -> {parsed} ({type(parsed).__name__})")

# ============================================================================
# 7. COMMON PITFALLS AND BEST PRACTICES
# ============================================================================

print("\n6. Common Pitfalls and Best Practices:")
print("-" * 30)

# Pitfall 1: Loss of precision
print("Pitfall 1: Precision loss in conversion")
large_float = 123.456789
converted_int = int(large_float)
print(f"Float {large_float} -> int {converted_int} (decimal part lost)")

# Pitfall 2: Unexpected boolean conversion
print("\nPitfall 2: Boolean conversion surprises")
print(f"bool('False') = {bool('False')}")  # True! (non-empty string)
print(f"bool('0') = {bool('0')}")          # True! (non-empty string)
print(f"bool(0) = {bool(0)}")              # False (integer zero)

# Best Practice 1: Always handle exceptions
print("\nBest Practice 1: Exception handling")
def robust_conversion(value, target_type):
    """Robustly convert value to target type."""
    try:
        if target_type == int:
            return int(value)
        elif target_type == float:
            return float(value)
        elif target_type == str:
            return str(value)
        elif target_type == bool:
            return bool(value)
        else:
            raise ValueError(f"Unsupported target type: {target_type}")
    except Exception as e:
        print(f"Conversion failed: {e}")
        return None

# Test robust conversion
test_value = "123.45"
for target in [int, float, str, bool]:
    result = robust_conversion(test_value, target)
    print(f"'{test_value}' -> {target.__name__}: {result}")

# ============================================================================
# 8. EXERCISES
# ============================================================================

print(f"\n{'='*50}")
print("EXERCISES - Practice Type Casting!")
print("="*50)

# Exercise 1: Temperature converter
def temperature_converter():
    """Convert between Celsius and Fahrenheit."""
    celsius_str = "25.5"  # Simulating user input
    
    try:
        celsius = float(celsius_str)
        fahrenheit = (celsius * 9/5) + 32
        print(f"\nExercise 1: Temperature Conversion")
        print(f"{celsius}°C = {fahrenheit:.1f}°F")
    except ValueError:
        print("Invalid temperature value")

temperature_converter()

# Exercise 2: Grade calculator
def calculate_grade():
    """Calculate letter grade from numeric score."""
    scores = ["85", "92.5", "78", "invalid", "95"]
    
    print(f"\nExercise 2: Grade Calculator")
    for score_str in scores:
        try:
            score = float(score_str)
            if score >= 90:
                grade = 'A'
            elif score >= 80:
                grade = 'B'
            elif score >= 70:
                grade = 'C'
            elif score >= 60:
                grade = 'D'
            else:
                grade = 'F'
            print(f"Score {score} -> Grade {grade}")
        except ValueError:
            print(f"Invalid score: {score_str}")

calculate_grade()

# Exercise 3: Data type analyzer
def analyze_data_types(data):
    """Analyze and convert a list of mixed data types."""
    print(f"\nExercise 3: Data Type Analysis")
    
    for item in data:
        original_type = type(item).__name__
        print(f"\nOriginal: {repr(item)} ({original_type})")
        
        # Try converting to different types
        conversions = {}
        
        try:
            conversions['int'] = int(item)
        except (ValueError, TypeError):
            conversions['int'] = "Cannot convert"
        
        try:
            conversions['float'] = float(item)
        except (ValueError, TypeError):
            conversions['float'] = "Cannot convert"
        
        try:
            conversions['str'] = str(item)
        except:
            conversions['str'] = "Cannot convert"
        
        conversions['bool'] = bool(item)
        
        for target_type, result in conversions.items():
            print(f"  -> {target_type}: {result}")

# Test data analysis
mixed_data = [42, "123", 3.14, True, "", [1, 2], None]
analyze_data_types(mixed_data)

print(f"\n{'='*50}")
print("Type Casting and Basic Exceptions - Complete!")
print("Next: Learn about Functions and Built-in Functions")
print("="*50)