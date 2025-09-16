"""
Python Data Structures - Sets
=============================

Sets are unordered collections of unique elements in Python. They are mutable
but can only contain immutable (hashable) elements. Sets are perfect for
removing duplicates, membership testing, and mathematical set operations.

Key Concepts Covered:
- Set creation and initialization
- Set operations (union, intersection, difference)
- Adding and removing elements
- Set methods and operations
- Frozen sets (immutable sets)
- Set comprehensions
- Practical use cases
"""

# ============================================================================
# 1. CREATING SETS
# ============================================================================

print("Python Sets - Comprehensive Guide")
print("=" * 34)

# 1.1 Different ways to create sets
print("1. Creating Sets:")
print("-" * 17)

# Empty set (must use set(), not {})
empty_set = set()
# empty_dict = {}  # This creates a dictionary, not a set!

# Set with initial values
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "cherry"}
mixed_set = {1, "hello", 3.14, True}

# Set from other iterables
string_to_set = set("Python")  # {'P', 'y', 't', 'h', 'o', 'n'}
list_to_set = set([1, 2, 2, 3, 3, 4])  # Removes duplicates

print(f"Empty set: {empty_set}")
print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed set: {mixed_set}")
print(f"From string: {string_to_set}")
print(f"From list (duplicates removed): {list_to_set}")

# ============================================================================
# 2. SET CHARACTERISTICS
# ============================================================================

print("\n2. Set Characteristics:")
print("-" * 22)

# 2.1 Sets contain only unique elements
duplicates = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
print(f"Set with duplicates: {duplicates}")  # Duplicates are automatically removed

# 2.2 Sets are unordered
letters = {"c", "a", "b"}
print(f"Letters set: {letters}")  # Order may vary between runs

# 2.3 Sets can only contain hashable (immutable) elements
valid_set = {1, "hello", (1, 2), frozenset({3, 4})}
print(f"Valid set with hashable elements: {valid_set}")

# This would cause an error (unhashable types):
# invalid_set = {[1, 2], {3, 4}}  # Lists and sets are not hashable

# ============================================================================
# 3. ACCESSING SET ELEMENTS
# ============================================================================

print("\n3. Accessing Set Elements:")
print("-" * 27)

colors = {"red", "green", "blue", "yellow"}
print(f"Colors set: {colors}")

# 3.1 Sets don't support indexing (no order)
# print(colors[0])  # This would cause TypeError

# 3.2 Check membership with 'in' operator
print(f"'red' in colors: {'red' in colors}")
print(f"'purple' in colors: {'purple' in colors}")

# 3.3 Iterate through set elements
print("Iterating through colors:")
for color in colors:
    print(f"  {color}")

# 3.4 Get arbitrary element with pop() or use iteration
if colors:
    print(f"Set length: {len(colors)}")
    print(f"Any element exists: {bool(colors)}")

# ============================================================================
# 4. ADDING ELEMENTS TO SETS
# ============================================================================

print("\n4. Adding Elements to Sets:")
print("-" * 29)

# 4.1 add() - Add single element
animals = {"cat", "dog"}
print(f"Original animals: {animals}")

animals.add("bird")
print(f"After add('bird'): {animals}")

# Adding duplicate has no effect
animals.add("cat")
print(f"After add('cat') again: {animals}")

# 4.2 update() - Add multiple elements
animals.update(["fish", "rabbit", "hamster"])
print(f"After update with list: {animals}")

animals.update("cow")  # Adds each character as separate element
print(f"After update with string: {animals}")

# 4.3 update() with multiple iterables
animals.update({"elephant"}, ["tiger", "lion"])
print(f"After update with multiple iterables: {animals}")

# ============================================================================
# 5. REMOVING ELEMENTS FROM SETS
# ============================================================================

print("\n5. Removing Elements from Sets:")
print("-" * 32)

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(f"Original numbers: {numbers}")

# 5.1 remove() - Remove element (raises KeyError if not found)
numbers.remove(5)
print(f"After remove(5): {numbers}")

# This would raise KeyError:
# numbers.remove(15)

# 5.2 discard() - Remove element (no error if not found)
numbers.discard(3)
print(f"After discard(3): {numbers}")

numbers.discard(15)  # No error even though 15 is not in set
print(f"After discard(15) - no error: {numbers}")

# 5.3 pop() - Remove and return arbitrary element
removed = numbers.pop()
print(f"Popped element: {removed}")
print(f"After pop(): {numbers}")

# 5.4 clear() - Remove all elements
test_set = {1, 2, 3}
print(f"Before clear(): {test_set}")
test_set.clear()
print(f"After clear(): {test_set}")

# ============================================================================
# 6. SET OPERATIONS - MATHEMATICAL OPERATIONS
# ============================================================================

print("\n6. Set Operations (Mathematical):")
print("-" * 34)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {1, 2, 3}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Set C: {set_c}")

# 6.1 Union (|) - All elements from both sets
union_result = set_a | set_b
union_method = set_a.union(set_b)
print(f"A | B (union): {union_result}")
print(f"A.union(B): {union_method}")

# 6.2 Intersection (&) - Common elements
intersection_result = set_a & set_b
intersection_method = set_a.intersection(set_b)
print(f"A & B (intersection): {intersection_result}")
print(f"A.intersection(B): {intersection_method}")

# 6.3 Difference (-) - Elements in first set but not in second
difference_result = set_a - set_b
difference_method = set_a.difference(set_b)
print(f"A - B (difference): {difference_result}")
print(f"A.difference(B): {difference_method}")

# 6.4 Symmetric Difference (^) - Elements in either set but not both
sym_diff_result = set_a ^ set_b
sym_diff_method = set_a.symmetric_difference(set_b)
print(f"A ^ B (symmetric difference): {sym_diff_result}")
print(f"A.symmetric_difference(B): {sym_diff_method}")

# ============================================================================
# 7. SET RELATIONSHIPS
# ============================================================================

print("\n7. Set Relationships:")
print("-" * 20)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {2, 3}
set_d = {1, 2, 3, 4, 5}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Set C: {set_c}")
print(f"Set D: {set_d}")

# 7.1 Subset relationships
print(f"C is subset of A: {set_c.issubset(set_a)}")
print(f"C <= A: {set_c <= set_a}")
print(f"A is subset of C: {set_a.issubset(set_c)}")

# 7.2 Superset relationships
print(f"A is superset of C: {set_a.issuperset(set_c)}")
print(f"A >= C: {set_a >= set_c}")

# 7.3 Disjoint sets (no common elements)
print(f"A and B are disjoint: {set_a.isdisjoint(set_b)}")
print(f"A and C are disjoint: {set_a.isdisjoint(set_c)}")

# 7.4 Set equality
print(f"A equals D: {set_a == set_d}")
print(f"A equals B: {set_a == set_b}")

# ============================================================================
# 8. SET COMPREHENSIONS
# ============================================================================

print("\n8. Set Comprehensions:")
print("-" * 20)

# Set comprehension syntax: {expression for item in iterable if condition}

# 8.1 Basic set comprehension
numbers = [1, 2, 3, 4, 5, 2, 3, 4]  # List with duplicates
squares = {x**2 for x in numbers}
print(f"Numbers list: {numbers}")
print(f"Squares set: {squares}")  # Duplicates automatically removed

# 8.2 Set comprehension with condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# 8.3 Set comprehension with string manipulation
words = ["hello", "world", "python", "hello", "programming"]
word_lengths = {len(word) for word in words}
uppercase_words = {word.upper() for word in words}

print(f"Original words: {words}")
print(f"Word lengths: {word_lengths}")
print(f"Uppercase words: {uppercase_words}")

# ============================================================================
# 9. FROZEN SETS (IMMUTABLE SETS)
# ============================================================================

print("\n9. Frozen Sets (Immutable Sets):")
print("-" * 33)

# 9.1 Creating frozen sets
regular_set = {1, 2, 3, 4, 5}
frozen_set1 = frozenset([1, 2, 3, 4, 5])
frozen_set2 = frozenset("hello")

print(f"Regular set: {regular_set}")
print(f"Frozen set 1: {frozen_set1}")
print(f"Frozen set 2: {frozen_set2}")

# 9.2 Frozen sets are immutable
# frozen_set1.add(6)  # This would cause AttributeError

# 9.3 Frozen sets can be used as dictionary keys or set elements
nested_sets = {
    frozenset([1, 2, 3]): "first",
    frozenset([4, 5, 6]): "second"
}
print(f"Dictionary with frozenset keys: {nested_sets}")

set_of_sets = {frozenset([1, 2]), frozenset([3, 4]), frozenset([5, 6])}
print(f"Set of frozensets: {set_of_sets}")

# 9.4 Frozen sets support all read-only set operations
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 5, 6])

print(f"Frozen set 1: {fs1}")
print(f"Frozen set 2: {fs2}")
print(f"Union: {fs1 | fs2}")
print(f"Intersection: {fs1 & fs2}")

# ============================================================================
# 10. PRACTICAL EXAMPLES
# ============================================================================

print("\n10. Practical Examples:")
print("-" * 23)

# 10.1 Remove duplicates from a list
def remove_duplicates(items):
    """Remove duplicates while preserving some order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

numbers_with_dups = [1, 2, 3, 2, 4, 3, 5, 1, 6]
unique_numbers = remove_duplicates(numbers_with_dups)
print(f"Original: {numbers_with_dups}")
print(f"Unique (order preserved): {unique_numbers}")
print(f"Unique (set method): {list(set(numbers_with_dups))}")

# 10.2 Find common interests
def find_common_interests():
    """Find common interests between people."""
    alice_interests = {"reading", "hiking", "cooking", "photography"}
    bob_interests = {"hiking", "gaming", "cooking", "music"}
    charlie_interests = {"reading", "gaming", "movies", "cooking"}
    
    print(f"Alice's interests: {alice_interests}")
    print(f"Bob's interests: {bob_interests}")
    print(f"Charlie's interests: {charlie_interests}")
    
    # Common interests between Alice and Bob
    alice_bob_common = alice_interests & bob_interests
    print(f"Alice & Bob common: {alice_bob_common}")
    
    # Interests unique to Alice
    alice_unique = alice_interests - bob_interests - charlie_interests
    print(f"Alice's unique interests: {alice_unique}")
    
    # All interests combined
    all_interests = alice_interests | bob_interests | charlie_interests
    print(f"All interests: {all_interests}")

find_common_interests()

# 10.3 Validate data integrity
def validate_user_permissions():
    """Validate user permissions using sets."""
    # Define permission sets
    admin_permissions = {"read", "write", "delete", "execute", "admin"}
    editor_permissions = {"read", "write", "execute"}
    viewer_permissions = {"read"}
    
    # User's current permissions
    user_permissions = {"read", "write", "admin", "invalid_perm"}
    
    print(f"User permissions: {user_permissions}")
    print(f"Admin permissions: {admin_permissions}")
    
    # Check if user has admin privileges
    is_admin = admin_permissions.issubset(user_permissions)
    print(f"User is admin: {is_admin}")
    
    # Find invalid permissions
    all_valid_permissions = admin_permissions | editor_permissions | viewer_permissions
    invalid_permissions = user_permissions - all_valid_permissions
    print(f"Invalid permissions: {invalid_permissions}")
    
    # Find missing admin permissions
    missing_admin_perms = admin_permissions - user_permissions
    print(f"Missing admin permissions: {missing_admin_perms}")

validate_user_permissions()

# ============================================================================
# 11. PERFORMANCE CHARACTERISTICS
# ============================================================================

print("\n11. Performance Characteristics:")
print("-" * 31)

import time

# Create large collections for testing
size = 100000
test_list = list(range(size))
test_set = set(range(size))

# Test membership checking
search_value = size - 1

# List membership (O(n))
start = time.time()
for _ in range(1000):
    _ = search_value in test_list
list_time = time.time() - start

# Set membership (O(1) average)
start = time.time()
for _ in range(1000):
    _ = search_value in test_set
set_time = time.time() - start

print(f"List membership time: {list_time:.6f} seconds")
print(f"Set membership time: {set_time:.6f} seconds")
print(f"Set is {list_time/set_time:.0f}x faster for membership testing")

# ============================================================================
# 12. EXERCISES
# ============================================================================

print(f"\n{'='*50}")
print("EXERCISES - Practice with Sets!")
print("="*50)

# Exercise 1: Text analysis
def exercise_1():
    """Analyze text using sets."""
    print("\nExercise 1: Text Analysis")
    
    text1 = "the quick brown fox jumps over the lazy dog"
    text2 = "a quick brown dog runs over the lazy fox"
    
    words1 = set(text1.split())
    words2 = set(text2.split())
    
    print(f"Text 1 words: {words1}")
    print(f"Text 2 words: {words2}")
    
    # Common words
    common = words1 & words2
    print(f"Common words: {common}")
    
    # Unique to each text
    unique_to_text1 = words1 - words2
    unique_to_text2 = words2 - words1
    print(f"Unique to text 1: {unique_to_text1}")
    print(f"Unique to text 2: {unique_to_text2}")
    
    # All unique words
    all_words = words1 | words2
    print(f"All unique words: {all_words}")
    print(f"Total unique words: {len(all_words)}")

exercise_1()

# Exercise 2: Student course enrollment
def exercise_2():
    """Manage student course enrollments."""
    print("\nExercise 2: Course Enrollment")
    
    # Student enrollments
    math_students = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
    science_students = {"Bob", "Charlie", "Frank", "Grace", "Alice"}
    english_students = {"Alice", "Diana", "Frank", "Henry", "Ivy"}
    
    print(f"Math students: {math_students}")
    print(f"Science students: {science_students}")
    print(f"English students: {english_students}")
    
    # Students taking all three subjects
    all_three = math_students & science_students & english_students
    print(f"Students taking all three: {all_three}")
    
    # Students taking at least one subject
    any_subject = math_students | science_students | english_students
    print(f"Students taking any subject: {any_subject}")
    
    # Students taking only math
    only_math = math_students - science_students - english_students
    print(f"Students taking only math: {only_math}")
    
    # Students taking math and science but not English
    math_science_not_english = (math_students & science_students) - english_students
    print(f"Math and Science but not English: {math_science_not_english}")

exercise_2()

# Exercise 3: Data deduplication
def exercise_3():
    """Remove duplicates from various data sources."""
    print("\nExercise 3: Data Deduplication")
    
    # Email lists from different sources
    newsletter_emails = ["alice@email.com", "bob@email.com", "charlie@email.com", "alice@email.com"]
    promotion_emails = ["bob@email.com", "diana@email.com", "eve@email.com", "bob@email.com"]
    survey_emails = ["alice@email.com", "charlie@email.com", "frank@email.com"]
    
    print(f"Newsletter emails: {newsletter_emails}")
    print(f"Promotion emails: {promotion_emails}")
    print(f"Survey emails: {survey_emails}")
    
    # Convert to sets to remove duplicates
    newsletter_set = set(newsletter_emails)
    promotion_set = set(promotion_emails)
    survey_set = set(survey_emails)
    
    print(f"Newsletter unique: {newsletter_set}")
    print(f"Promotion unique: {promotion_set}")
    print(f"Survey unique: {survey_set}")
    
    # All unique email addresses
    all_emails = newsletter_set | promotion_set | survey_set
    print(f"All unique emails: {all_emails}")
    print(f"Total unique subscribers: {len(all_emails)}")
    
    # Emails that appear in all lists
    frequent_subscribers = newsletter_set & promotion_set & survey_set
    print(f"Frequent subscribers (all lists): {frequent_subscribers}")

exercise_3()

print(f"\n{'='*50}")
print("Sets - Complete!")
print("Next: Learn about Dictionaries")
print("="*50)