````
# Day 2 — Python Data Structures, Functions & Problem Solving

## Objective

Build a strong foundation in Python's core data structures, reusable functions,
iteration patterns, and basic algorithmic problem solving.

---

# 1. Lists

A list is an ordered, mutable collection.

```python
numbers = [10, 20, 30, 40]
````

## Key properties

* Ordered
* Mutable
* Allows duplicates
* Supports indexing and slicing
* Can contain heterogeneous data

## Common operations

```python
numbers.append(50)          # Add at end
numbers.extend([60, 70])    # Add multiple elements
numbers.insert(1, 15)       # Insert at index
numbers.remove(20)          # Remove first occurrence
numbers.pop()               # Remove and return last element
numbers.pop(1)              # Remove and return element at index
```

## Sorting

```python
numbers.sort()              # Modifies original list
sorted_numbers = sorted(numbers)  # Creates new sorted list
```

## List comprehension

```python
squares = [x ** 2 for x in numbers]
```

## Important problem-solving patterns

### Manual aggregation

```python
total = 0

for number in numbers:
    total += number
```

### Finding maximum

Initialize from the input rather than assuming `0` is a valid maximum:

```python
maximum = numbers[0]

for number in numbers[1:]:
    if number > maximum:
        maximum = number
```

This is important when values can be negative.

### Second-largest unique number

Maintain two pieces of state:

```text
maximum
second_maximum
```

When a new maximum is found:

```text
second_maximum = maximum
maximum = current
```

For the second-largest unique value, duplicates of the maximum must not
replace the second-largest value.

---

# 2. Sets

A set is an unordered collection of unique elements.

```python
numbers = {1, 2, 3, 4}
```

## Key properties

* Unique elements
* Mutable
* No positional indexing
* Efficient membership testing
* Useful for removing duplicates

## Important operations

```python
numbers.add(5)
numbers.remove(3)
numbers.discard(10)
```

## Set operations

```python
a | b       # Union
a & b       # Intersection
a - b       # Difference
a ^ b       # Symmetric difference
```

## Common use cases

### Remove duplicates

```python
unique_numbers = set(numbers)
```

### Check membership

```python
if value in numbers:
    ...
```

### Track previously seen elements

```python
seen = set()

for number in numbers:
    if number in seen:
        # duplicate found
        ...
    seen.add(number)
```

This pattern was used to find the first duplicate.

---

# 3. Tuples

A tuple is an ordered, immutable collection.

```python
employee = ("Dhruval", "AI Developer", 3)
```

## Key properties

* Ordered
* Immutable
* Allows duplicates
* Supports indexing and slicing

## Single-element tuple

The comma is important:

```python
a = (10)     # int
b = (10,)    # tuple
```

The comma makes it a tuple.

## Tuple indexing and slicing

```python
employee[0]
employee[-1]
employee[:2]
employee[::-1]
```

## Tuple packing

```python
employee = "Dhruval", 3, "AI Developer"
```

Multiple values are packed into a tuple.

## Tuple unpacking

```python
employee = ("Dhruval", 3, "AI Developer")

name, experience, role = employee
```

## Extended unpacking

```python
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers
```

Result:

```text
first  -> 10
middle -> [20, 30, 40]
last   -> 50
```

## Common tuple methods

```python
numbers.count(20)
numbers.index(30)
```

## List vs Tuple

```text
List
→ mutable
→ dynamic collection

Tuple
→ immutable
→ fixed collection
```

Choose based on the nature and required operations of the data.

Important: immutability applies to the tuple structure itself. A tuple can
contain mutable objects such as lists.

---

# 4. Dictionaries

A dictionary stores key-value pairs.

```python
employee = {
    "name": "Dhruval",
    "role": "AI Developer",
    "experience": 3
}
```

Conceptually:

```text
key          value
------------------------
name         Dhruval
role         AI Developer
experience   3
```

## Accessing values

```python
employee["name"]
```

If the key is missing, this raises `KeyError`.

For optional keys:

```python
employee.get("salary")
```

A default can also be supplied:

```python
employee.get("salary", 0)
```

### `[]` vs `.get()`

Use `[]` when the key is required.

Use `.get()` when the key may be absent or optional.

---

## Add / update

The same syntax performs both operations:

```python
employee["experience"] = 3
```

If the key doesn't exist → add.

If the key exists → update.

---

## Dictionary iteration

```python
for key in employee:
    print(key)
```

```python
for value in employee.values():
    print(value)
```

```python
for key, value in employee.items():
    print(key, value)
```

Remember:

```text
.keys()    → keys
.values()  → values
.items()   → key + value
```

---

## Removing values

```python
employee.pop("role")
```

or:

```python
del employee["experience"]
```

`pop()` can also provide a default:

```python
employee.pop("salary", None)
```

---

## Frequency map pattern

One of the most important dictionary patterns:

```python
frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1
```

For:

```python
[1, 2, 2, 3, 3, 3]
```

the result is:

```python
{
    1: 1,
    2: 2,
    3: 3
}
```

This pattern is fundamental to algorithmic problem solving.

---

## Nested dictionaries

Dictionaries can contain dictionaries:

```python
employee = {
    "name": "Dhruval",
    "job": {
        "role": "AI Developer",
        "experience": 3
    }
}
```

Access:

```python
employee["job"]["role"]
```

---

## Dictionary comprehension

```python
squares = {
    number: number ** 2
    for number in range(1, 6)
}
```

Result:

```python
{
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}
```

---

# 5. Functions

Functions allow logic to be packaged into reusable units.

```python
def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total
```

## Important concepts

* Function definition
* Parameters
* Arguments
* Return values
* Default arguments
* Keyword arguments
* `*args`
* `**kwargs`
* Local scope
* Docstrings
* Function composition

## `return` vs `print`

```python
def calculate_sum(numbers):
    return 100
```

`return` sends a value back to the caller.

`print()` only displays a value.

---

## `*args`

```python
def find_maximum(*numbers):
    ...
```

Multiple positional arguments are collected into a tuple.

```python
find_maximum(10, 20, 30)
```

Conceptually:

```python
numbers = (10, 20, 30)
```

---

## `**kwargs`

```python
def create_employee(**details):
    return details
```

Keyword arguments are collected into a dictionary.

```python
create_employee(
    name="Dhruval",
    role="AI Developer",
    experience=3
)
```

produces a dictionary-like structure:

```python
{
    "name": "Dhruval",
    "role": "AI Developer",
    "experience": 3
}
```

---

## Returning multiple values

```python
def calculate_statistics(numbers):
    return maximum, minimum, total, average
```

Python packs the returned values into a tuple.

They can then be unpacked:

```python
maximum, minimum, total, average = calculate_statistics(numbers)
```

---

## Function composition

Large logic should be broken into focused functions.

Example:

```text
analyze_numbers()
    |
    +-- calculate_statistics()
    |
    +-- separate_even_odd()
    |
    +-- count_frequency()
```

This improves readability, reuse, testing, and maintainability.

---

# 6. Loops

Loops allow repeated processing of data.

## `for`

```python
for number in numbers:
    print(number)
```

A `for` loop iterates over an iterable.

Iterables include:

* Lists
* Tuples
* Sets
* Strings
* Dictionaries
* Other iterable objects

---

## `range()`

```python
range(start, stop, step)
```

The stop value is excluded.

Examples:

```python
range(5)
# 0, 1, 2, 3, 4

range(2, 6)
# 2, 3, 4, 5

range(2, 10, 2)
# 2, 4, 6, 8
```

---

## `while`

A `while` loop continues while a condition remains true.

```python
count = 10

while count > 0:
    print(count)
    count -= 1
```

A `while` loop is useful when the number of iterations is not known in
advance.

Example:

```python
while True:
    number = int(input("Enter number: "))

    if number == 0:
        break
```

---

## `break`

Terminates the entire current loop.

```python
for number in numbers:
    if number > 30:
        break
```

---

## `continue`

Skips the remainder of the current iteration.

```python
for number in numbers:
    if number % 10 != 0:
        continue

    print(number)
```

---

## `enumerate()`

Use when both index and value are required.

```python
for index, skill in enumerate(skills, start=1):
    print(index, skill)
```

This is preferable to manually managing an index.

---

## `zip()`

Use to iterate over corresponding elements of multiple iterables.

```python
for name, score in zip(names, scores):
    print(name, score)
```

---

## Nested loops

A loop inside another loop:

```python
for i in range(n):
    for j in range(n):
        ...
```

If both loops execute approximately `n` times:

```text
n × n = n²
```

Therefore:

```text
Time complexity = O(n²)
```

---

## Loop state

Many algorithms follow this pattern:

```text
Initialize state
      ↓
Iterate
      ↓
Inspect current element
      ↓
Update state
      ↓
Continue
      ↓
Return final state
```

Examples:

* Maximum/minimum
* Sum
* Frequency map
* First duplicate
* Second-largest element
* Department aggregation

This is one of the fundamental algorithmic patterns learned on Day 2.

---

## `for...else`

Python allows:

```python
for number in numbers:
    if number == target:
        print("Found")
        break
else:
    print("Not Found")
```

The `else` executes only if the loop completes without executing `break`.

---

# 7. Data Structure Selection

A useful decision framework:

```text
Need ordered + mutable collection?
        ↓
      List

Need fixed/immutable collection?
        ↓
      Tuple

Need uniqueness / membership?
        ↓
       Set

Need key → value lookup?
        ↓
   Dictionary
```

Examples:

```text
Employee records       → List of Dictionaries
Unique departments     → Set
(latitude, longitude)  → Tuple
employee_id → record   → Dictionary
word → frequency       → Dictionary
```

Data structure selection should be based on:

1. What the data represents
2. What operations are required
3. Whether mutation is required
4. Whether uniqueness is required
5. Whether key-based lookup is required
6. Expected complexity

---

# 8. Complexity Fundamentals

Basic loop patterns:

```python
for x in numbers:
    ...
```

Usually:

```text
O(n)
```

Nested loops:

```python
for x in numbers:
    for y in numbers:
        ...
```

Usually:

```text
O(n²)
```

Dictionary/set membership is generally average-case:

```text
O(1)
```

Therefore a pattern such as:

```python
seen = set()

for number in numbers:
    if number in seen:
        ...
    seen.add(number)
```

is generally:

```text
Time  → O(n) average
Space → O(n)
```

Important principle:

> Correctness and optimality are different things.

A solution can be correct but still have unnecessarily high complexity.

Example: removing elements from a list during a first-non-repeating-number algorithm can introduce O(n) list operations and potentially make the overall solution O(n²).

---

# 9. Employee Analytics Mini-Project

The Day-2 project combined all major concepts.

Input:

```text
List
  ↓
Dictionary employee records
  ↓
Sets for skills/departments
  ↓
Loops for processing
  ↓
Dictionaries for aggregation
  ↓
Functions for decomposition
```

Implemented analytics included:

* Total employees
* Unique departments
* Employee count by department
* Average salary by department
* Highest-paid employee
* Unique skills
* Employees with a particular skill
* Department with highest average salary
* Department salary report

Important pattern:

```text
GROUP BY department
        ↓
COUNT
SUM
AVERAGE
MAX
```

This is the Python-level foundation of aggregation patterns that later appear
in SQL and PySpark.

---

# 10. Day-2 Problem-Solving Lessons

## 1. Initialize state carefully

Avoid:

```python
maximum = 0
```

when values can be negative.

Prefer:

```python
maximum = numbers[0]
```

or an explicit `None`-based initialization.

---

## 2. Handle empty input deliberately

A function should have a clear contract for:

```python
[]
```

Don't let empty-input behavior happen accidentally.

---

## 3. Correct does not always mean optimal

Always ask:

```text
Does this work?
        ↓
What is the time complexity?
        ↓
What is the space complexity?
        ↓
Can it be improved?
```

---

## 4. Required vs optional dictionary keys

Use:

```python
employee["salary"]
```

when salary is required.

Use:

```python
employee.get("salary")
```

when salary may be absent.

---

## 5. Think in state transitions

For algorithmic problems:

```text
Current input
     ↓
Current state
     ↓
Decision
     ↓
State update
```

This pattern appeared repeatedly throughout Day 2.

---