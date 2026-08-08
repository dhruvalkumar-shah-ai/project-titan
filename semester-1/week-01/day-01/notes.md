# Day 1 — Python Foundations

## 1. Variables and Objects

Python is dynamically typed.

A variable/name does not have a permanently fixed type. A name refers
to an object, and it can be rebound to an object of a different type.

Example:

```python
name = "Dhruval"
name = 100

The name name refers to a str object and later refers to an int object.

name = "Dhruval"
experience = 3

print(type(name))
print(type(experience))

Output:
<class 'str'>
<class 'int'>

Rebinding:
Assignment can rebind a name to another object:
x = 10
y = x

x = 20

Conceptually:
x ───► 20

y ───► 10

Therefore:
x = 20
y = 10

Changing what x refers to does not change what y refers to.

Mutation:
Some Python objects can be modified after they are created.
x = [10]
y = x

x.append(20)

Both x and y refer to the same list object:
x ──┐
    ├──► [10, 20]
y ──┘

Therefore:
x = [10, 20]
y = [10, 20]

5. Key Learning
Rebinding:
x = 20

Changes what the name x refers to.

Mutation:
x.append(20)

Changes the existing object itself.

Important distinction:

Rebinding changes the reference. Mutation changes the object.

6. Questions / Things to Revisit
Mutable vs immutable objects
How Python stores objects in memory
Shallow copy vs deep copy
How function arguments behave