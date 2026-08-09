name = "Dhruval"
experience = 3
target = "AI/ML Engineer"

print(name)
print(experience)
print(target)

print(type(name))
print(type(experience))
print(type(target))

name = 100

print(name)
print(type(name))


x = 10
y = x

x = 20

print(x)
print(y)

x = [10]
y = x

x.append(20)

print(x)
print(y)

name = "Dhruval"       # str
experience = 3         # int

age = 25
salary = 8.5
is_learning = True

print(age)
print(type(age))

print(salary)
print(type(salary))

print(is_learning)
print(type(is_learning))

print(10 / 3)
print(10 // 3)
print(10 % 3)

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 ** 3)

# Comparison Operators
# They compare two values and produce a Boolean Value.
# The six basic ones are: ==, !=, >, <, >=, <=
x = 10
y = 20

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# ==  → "Do these have equal values?"
# is  → "Are these the same object?"

x = 10
y = 10

print(x == y)
print(x is y)

x = [10]
y = [10]

print(x == y)
print(x is y)

"""
Python's short-circuit Behaviour:
Python actually short-circuit's any boolean expression:

Example:
False and something ---> then something won't be evaluated since entire expression is False
True or something ---> Then something won't be evaluated since entire expression is True

THis helps in:
1. performance
2. avoid unnecessary computation
3. safe conditional expressions
4. real-world Python Code
"""

"""
If Condition:
This is actually part of decision-making statements.
"""
age = 20

if age >= 18:
    print("You are eligible to vote.")

age = 15
if age >= 18:
    print("You are eligible to vote.")

"""
Else Condition:
If we want Python to do something when the condition is false
"""

age = 15

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

"""
              age >= 18?
                 │
          ┌──────┴──────┐
        True           False
          │               │
      eligible        not eligible
"""
"""
if condition:
    # runs when True
else:
    # runs when False
"""
"""
comparison
    ↓
True / False
    ↓
if / else
    ↓
decision
"""
age = 16

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

"""
age >= 18
16 >= 18
   ↓
 False
   ↓
check elif

age >= 13
16 >= 13
   ↓
 True
   ↓
print("Teenager")

And importantly, once Python finds a true condition, it executes that block and skips the
remaining elif/else blocks.
"""

age = 20

if age >= 13:
    print("Teenager")
elif age >= 18:
    print("Adult")

"""
20 >= 13
   ↓
 True
   ↓
print("Teenager")
   ↓
STOP checking this if/elif chain
"""

"""
In an if/elif/else chain, Python executes only the first condition that evaluates to True.
Therefore, condition ordering matters.
"""
age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
"""
if condition_1:
    if condition_2:
        # execute
The inner if (condition_2) will only be evaluated if condition_1 is True

age = 25
has_id = True

        age >= 18?
             │
           True
             ↓
        has_id?
             │
           True
             ↓
     "Entry allowed"
"""

age = 20
has_id = False

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Underage")

"""
age >= 18
20 >= 18
   ↓
 True
   ↓
enter outer if
   ↓
has_id
   ↓
 False
   ↓
inner else
   ↓
"ID required"
"""

name = "Dhruval"

print("D" in name)
print("z" in name)
print("D" not in name)
print("z" not in name)

"""
True; since "D" exists in Dhruval as D is capital
False; since "z" does not exists in Dhruval
False; since "D" exists in Dhruval and D is capital
True; since "z" does not exist in Dhruval
"""