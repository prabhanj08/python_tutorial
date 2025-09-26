"""
Python Control Flow - Conditionals
==================================

Conditional statements allow programs to make decisions and execute different
code paths based on certain conditions. Python uses if, elif, and else
statements to control program flow based on boolean expressions.

Key Concepts Covered:
- if, elif, else statements
- Comparison and logical operators
- Boolean expressions and truthiness
- Nested conditionals
- Conditional expressions (ternary operator)
- Best practices for writing conditionals
"""

# ============================================================================
# 1. BASIC IF STATEMENTS
# ============================================================================

print("Python Conditionals - Comprehensive Guide")
print("=" * 42)

# 1.1 Simple if statement
print("1. Basic If Statements:")
print("-" * 23)

age = 18
if age >= 18:
    print("You are eligible to vote!")

# 1.2 if-else statement
temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot.")

# 1.3 Multiple conditions
score = 85
if score >= 90:
    print("Grade: A")
else:
    if score >= 80:
        print("Grade: B")
    else:
        if score >= 70:
            print("Grade: C")
        else:
            print("Grade: F")

# ============================================================================
# 2. IF-ELIF-ELSE STATEMENTS
# ============================================================================

print("\n2. If-Elif-Else Statements:")
print("-" * 28)

# 2.1 Better way to handle multiple conditions
score = 92
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# 2.2 Real-world example: Traffic light system
def traffic_light_action(color):
    """Determine action based on traffic light color."""
    if color.lower() == "red":
        return "Stop"
    elif color.lower() == "yellow":
        return "Caution - prepare to stop"
    elif color.lower() == "green":
        return "Go"
    else:
        return "Invalid color"

# Test traffic light function
colors = ["red", "yellow", "green", "blue"]
for color in colors:
    action = traffic_light_action(color)
    print(f"Light: {color} -> Action: {action}")

# ============================================================================
# 3. COMPARISON OPERATORS
# ============================================================================

print("\n3. Comparison Operators:")
print("-" * 25)

a = 10
b = 20
c = 10

print(f"a = {a}, b = {b}, c = {c}")
print(f"a == b: {a == b}")    # Equal to
print(f"a != b: {a != b}")    # Not equal to
print(f"a < b: {a < b}")      # Less than
print(f"a > b: {a > b}")      # Greater than
print(f"a <= c: {a <= c}")    # Less than or equal to
print(f"a >= c: {a >= c}")    # Greater than or equal to

# 3.1 String comparisons
name1 = "Alice"
name2 = "Bob"
name3 = "alice"

print(f"\nString comparisons:")
print(f"'{name1}' == '{name2}': {name1 == name2}")
print(f"'{name1}' < '{name2}': {name1 < name2}")  # Lexicographic order
print(f"'{name1}' == '{name3}': {name1 == name3}")  # Case sensitive
print(f"'{name1}'.lower() == '{name3}': {name1.lower() == name3}")

# 3.2 Chained comparisons
x = 15
print(f"\nChained comparisons with x = {x}:")
print(f"10 < x < 20: {10 < x < 20}")
print(f"10 < x < 15: {10 < x < 15}")
print(f"10 <= x <= 20: {10 <= x <= 20}")

# ============================================================================
# 4. LOGICAL OPERATORS
# ============================================================================

print("\n4. Logical Operators:")
print("-" * 21)

# 4.1 and, or, not operators
age = 25
has_license = True
has_insurance = False

print(f"Age: {age}, Has license: {has_license}, Has insurance: {has_insurance}")

# AND operator - all conditions must be True
if age >= 18 and has_license:
    print("Can drive (age and license check)")

if age >= 18 and has_license and has_insurance:
    print("Fully qualified to drive")
else:
    print("Missing requirements for driving")

# OR operator - at least one condition must be True
if age < 18 or not has_license:
    print("Cannot drive due to age or license")

# NOT operator - reverses boolean value
if not has_insurance:
    print("Need to get insurance")

# 4.2 Complex logical expressions
temperature = 22
is_sunny = True
is_weekend = False

if (temperature > 20 and is_sunny) or is_weekend:
    print("Good day for outdoor activities!")

# ============================================================================
# 5. TRUTHINESS AND FALSY VALUES
# ============================================================================

print("\n5. Truthiness and Falsy Values:")
print("-" * 32)

# 5.1 Falsy values in Python
falsy_values = [False, 0, 0.0, "", [], {}, set(), None]

print("Falsy values:")
for value in falsy_values:
    if not value:
        print(f"  {repr(value)} is falsy")

# 5.2 Truthy values
truthy_values = [True, 1, -1, "hello", [1], {"key": "value"}, {1, 2}]

print("\nTruthy values:")
for value in truthy_values:
    if value:
        print(f"  {repr(value)} is truthy")

# 5.3 Practical use of truthiness
def check_data(data):
    """Check if data is valid using truthiness."""
    if data:
        print(f"Data is valid: {data}")
        return True
    else:
        print(f"Data is empty or invalid: {repr(data)}")
        return False

# Test with different data types
test_data = ["hello", "", [1, 2, 3], [], 0, 42, None]
for data in test_data:
    check_data(data)

# ============================================================================
# 6. CONDITIONAL EXPRESSIONS (TERNARY OPERATOR)
# ============================================================================

print("\n6. Conditional Expressions (Ternary):")
print("-" * 37)

# 6.1 Basic ternary operator
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Age: {age}, Status: {status}")

# 6.2 Multiple ternary expressions
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(f"Score: {score}, Grade: {grade}")

# 6.3 Ternary in function calls
def get_discount(is_member, purchase_amount):
    """Calculate discount based on membership and purchase amount."""
    base_discount = 0.1 if is_member else 0.05
    bonus_discount = 0.05 if purchase_amount > 100 else 0
    return base_discount + bonus_discount

# Test discount calculation
customers = [
    (True, 150),   # Member, high purchase
    (True, 50),    # Member, low purchase
    (False, 150),  # Non-member, high purchase
    (False, 50)    # Non-member, low purchase
]

for is_member, amount in customers:
    discount = get_discount(is_member, amount)
    savings = amount * discount
    print(f"Member: {is_member}, Amount: ${amount}, Discount: {discount:.1%}, Savings: ${savings:.2f}")

# ============================================================================
# 7. EXERCISES
# ============================================================================

print(f"\n{'='*50}")
print("EXERCISES - Practice with Conditionals!")
print("="*50)

# Exercise 1: Number classifier
def exercise_1():
    """Classify numbers based on various criteria."""
    print("\nExercise 1: Number Classifier")
    
    def classify_number(num):
        """Classify a number based on multiple criteria."""
        classifications = []
        
        # Sign classification
        if num > 0:
            classifications.append("positive")
        elif num < 0:
            classifications.append("negative")
        else:
            classifications.append("zero")
        
        # Even/odd classification (only for non-zero)
        if num != 0:
            if num % 2 == 0:
                classifications.append("even")
            else:
                classifications.append("odd")
        
        # Size classification
        if abs(num) > 100:
            classifications.append("large")
        elif abs(num) > 10:
            classifications.append("medium")
        elif num != 0:
            classifications.append("small")
        
        return classifications
    
    test_numbers = [42, -17, 0, 150, -5, 8]
    for num in test_numbers:
        classifications = classify_number(num)
        print(f"{num}: {', '.join(classifications)}")

exercise_1()

# Exercise 2: Password strength checker
def exercise_2():
    """Check password strength based on multiple criteria."""
    print("\nExercise 2: Password Strength Checker")
    
    def check_password_strength(password):
        """Evaluate password strength based on multiple criteria."""
        if not password:
            return "Password cannot be empty"
        
        score = 0
        feedback = []
        
        # Length check
        if len(password) >= 12:
            score += 3
        elif len(password) >= 8:
            score += 2
        else:
            feedback.append("Password should be at least 8 characters")
        
        # Character type checks
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
        
        if has_lower:
            score += 1
        else:
            feedback.append("Add lowercase letters")
        
        if has_upper:
            score += 1
        else:
            feedback.append("Add uppercase letters")
        
        if has_digit:
            score += 1
        else:
            feedback.append("Add numbers")
        
        if has_special:
            score += 2
        else:
            feedback.append("Add special characters")
        
        # Determine strength
        if score >= 8:
            strength = "Very Strong"
        elif score >= 6:
            strength = "Strong"
        elif score >= 4:
            strength = "Medium"
        elif score >= 2:
            strength = "Weak"
        else:
            strength = "Very Weak"
        
        result = f"Strength: {strength} (Score: {score}/10)"
        if feedback:
            result += f"\nSuggestions: {', '.join(feedback)}"
        
        return result
    
    test_passwords = [
        "password",
        "Password123",
        "MyStr0ng!Pass",
        "VerySecure@Password123",
        "weak"
    ]
    
    for password in test_passwords:
        result = check_password_strength(password)
        print(f"Password: '{password}'")
        print(result)
        print()

exercise_2()

print(f"\n{'='*50}")
print("Conditionals - Complete!")
print("Next: Learn about Loops")
print("="*50)