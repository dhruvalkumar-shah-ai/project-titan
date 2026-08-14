# Day 3 — Functions

## Objective

Understand Python functions from fundamentals through function objects, including parameter/argument handling, scope, LEGB name resolution, and `global`/`nonlocal`.

---

# 1. Why Functions Exist

Functions allow us to package a reusable piece of behavior behind a defined interface.

The three major purposes of functions are:

### 1.1 Reusability

Write logic once and use it multiple times.

```python
def calculate_total(numbers):
    total = 0

    for number in numbers:
        total += number

    return total
```

The same function can be reused with different inputs.

### 1.2 Abstraction

The caller does not need to know the internal implementation.

```python
calculate_total(numbers)
```

The caller only needs to understand:

* what input the function expects
* what result it returns

### 1.3 Decomposition

Large programs can be divided into smaller logical units.

```text
Application
├── load_data()
├── validate_data()
├── process_data()
├── calculate_metrics()
└── generate_report()
```

This improves readability, maintainability, testing, and reuse.

---

# 2. Function Definition

A function is defined using the `def` keyword.

```python
def calculate_total(numbers):
    total = 0

    for number in numbers:
        total += number

    return total
```

Components:

```text
def              → keyword used to define a function
calculate_total  → function name
(numbers)        → parameter list
:                → begins the function body
indented code    → function body
return           → sends a value back to the caller
```

General structure:

```python
def function_name(parameters):
    function_body
```

## Definition vs Execution

Defining a function does not execute its body.

```python
def greet():
    print("Hello")
```

At this point, Python creates the function object and binds it to the name `greet`.

The body executes only when the function is called:

```python
greet()
```

Therefore:

```python
def greet():
    print("Hello")

print("A")
greet()
print("B")
```

produces:

```text
A
Hello
B
```

---

# 3. Parameters

A parameter is a variable declared in a function definition that receives a value when the function is called.

```python
def calculate_area(length, width):
    return length * width
```

Here:

```text
length → parameter
width  → parameter
```

Parameters define what inputs the function expects.

---

# 4. Arguments

An argument is the actual value supplied when calling a function.

```python
def calculate_area(length, width):
    return length * width

area = calculate_area(10, 5)
```

Here:

```text
Parameters:
    length
    width

Arguments:
    10
    5
```

Python binds:

```text
length → 10
width  → 5
```

The distinction is:

> Parameter = variable in the function definition.

> Argument = actual value supplied during the function call.

---

# 5. Positional Arguments

Positional arguments are bound to parameters according to their position.

```python
def calculate_area(length, width):
    return length * width

calculate_area(10, 5)
```

Binding:

```text
1st argument → 1st parameter
2nd argument → 2nd parameter

length → 10
width  → 5
```

Reversing the arguments changes the binding:

```python
calculate_area(5, 10)
```

results in:

```text
length → 5
width  → 10
```

The function uses the order supplied by the caller.

---

# 6. Keyword Arguments

Keyword arguments explicitly identify the parameter receiving the value.

```python
def introduce(name, age, city):
    print(name, age, city)

introduce(
    city="Bangalore",
    name="Rahul",
    age=28
)
```

Binding:

```text
name → "Rahul"
age  → 28
city → "Bangalore"
```

Unlike positional arguments, keyword arguments do not depend on the order in which they are written.

For example:

```python
introduce(
    name="Rahul",
    age=28,
    city="Bangalore"
)
```

and:

```python
introduce(
    city="Bangalore",
    name="Rahul",
    age=28
)
```

produce the same parameter bindings.

## Positional arguments must come before keyword arguments

Valid:

```python
connect("localhost", timeout=60)
```

Invalid:

```python
connect(host="localhost", 9000)
```

The general ordering is:

```text
positional arguments
        ↓
keyword arguments
```

---

# 7. Default Arguments

A default argument provides a fallback value when the caller does not provide a value for that parameter.

```python
def introduce(name, city="Bangalore"):
    print(name, city)
```

Calling:

```python
introduce("Rahul")
```

uses the default:

```text
name → "Rahul"
city → "Bangalore"
```

The default can be overridden:

```python
introduce("Rahul", "Hyderabad")
```

results in:

```text
name → "Rahul"
city → "Hyderabad"
```

Example with multiple defaults:

```python
def connect(host, port=8080, timeout=30):
    print(host, port, timeout)
```

```python
connect("localhost")
```

results in:

```text
host    → "localhost"
port    → 8080
timeout → 30
```

```python
connect("localhost", 9000)
```

results in:

```text
host    → "localhost"
port    → 9000
timeout → 30
```

```python
connect("localhost", 9000, 60)
```

results in:

```text
host    → "localhost"
port    → 9000
timeout → 60
```

```python
connect("localhost", timeout=60)
```

results in:

```text
host    → "localhost"
port    → 8080
timeout → 60
```

## Important Rule

A non-default parameter cannot follow a default parameter.

Invalid:

```python
def introduce(name="Rahul", city):
    ...
```

Valid:

```python
def introduce(name, city="Bangalore"):
    ...
```

---

# 8. `*args`

`*args` allows a function to accept a variable number of positional arguments.

```python
def show_args(*args):
    print(args)
```

Calling:

```python
show_args(10, 20, 30)
```

causes the positional arguments to be collected into a tuple:

```python
args = (10, 20, 30)
```

Therefore:

```python
type(args)
```

returns:

```text
<class 'tuple'>
```

The name `args` is conventional. The `*` is what provides the special behavior.

This is also valid:

```python
def show_args(*numbers):
    print(numbers)
```

The collected values are still stored in a tuple.

## Zero positional arguments

```python
show_args()
```

results in:

```python
args = ()
```

## `*` during function calls

The same syntax can also be used for unpacking:

```python
numbers = [10, 20, 30]

show_args(*numbers)
```

This effectively supplies:

```python
show_args(10, 20, 30)
```

So:

```text
* in definition → collect positional arguments
* in call       → unpack an iterable into positional arguments
```

## Implementation

```python
def calculate_sum(*args):
    if not args:
        return None

    total = 0

    for number in args:
        total += number

    return total
```

Example:

```python
calculate_sum(1, 2, 3)
```

returns:

```text
6
```

The implementation deliberately does not use Python's built-in `sum()`.

---

# 9. `**kwargs`

`**kwargs` allows a function to accept a variable number of keyword arguments.

```python
def inspect(**kwargs):
    print(type(kwargs))
    print(kwargs)
```

Calling:

```python
inspect(
    name="Dhruval",
    age=25,
    city="Hyderabad"
)
```

creates:

```python
kwargs = {
    "name": "Dhruval",
    "age": 25,
    "city": "Hyderabad"
}
```

Therefore:

```text
type(kwargs)
→ <class 'dict'>
```

The name `kwargs` is conventional. The `**` provides the special behavior.

## `*args` vs `**kwargs`

| Syntax     | Collects             | Container  |
| ---------- | -------------------- | ---------- |
| `*args`    | positional arguments | tuple      |
| `**kwargs` | keyword arguments    | dictionary |

Both can be used together:

```python
def example(*args, **kwargs):
    ...
```

Example:

```python
example(
    10,
    20,
    30,
    name="Dhruval",
    city="Hyderabad"
)
```

Conceptually:

```text
args
→ (10, 20, 30)

kwargs
→ {
    "name": "Dhruval",
    "city": "Hyderabad"
}
```

## Implementation

```python
def build_profile(*args, **kwargs):
    kwargs.update({"skills": args})
    return kwargs
```

Example:

```python
profile = build_profile(
    "Python",
    "Databricks",
    "Computer Vision",
    name="Dhruval",
    experience=3
)
```

The result contains:

```python
{
    "name": "Dhruval",
    "experience": 3,
    "skills": (
        "Python",
        "Databricks",
        "Computer Vision"
    )
}
```

---

# 10. Return Values

`return` sends a value from a function back to its caller.

```python
def calculate_sum(a, b):
    total = a + b
    return total
```

Calling:

```python
result = calculate_sum(10, 20)
```

means:

```text
calculate_sum(10, 20)
        ↓
       30
        ↓
result = 30
```

## `print()` vs `return`

`print()` displays a value.

```python
print(value)
```

`return` sends a value back to the caller.

```python
return value
```

These are not interchangeable.

Example:

```python
def test():
    print("Hello")

result = test()

print("Result:", result)
```

Output:

```text
Hello
Result: None
```

Because `test()` has no explicit return statement.

A function without an explicit return returns:

```python
None
```

Therefore:

```python
result = None
```

## Key distinction

```text
print(x)
→ display x

return x
→ send x to the caller
```

---

# 11. Scope

Scope defines where a name/variable is accessible.

Example:

```python
x = 10

def test():
    y = 20

    print(x)
    print(y)

test()

print(x)
```

Here:

```text
x → global scope
y → local scope of test()
```

`y` is accessible inside `test()` but not outside it.

## Local Scope

A variable assigned inside a function normally belongs to that function's local scope.

```python
x = 10

def test():
    x = 20
    print(x)

test()
print(x)
```

Output:

```text
20
10
```

There are two separate `x` names:

```text
Global scope
└── x = 10

test() local scope
└── x = 20
```

The local `x` does not overwrite the global `x`.

---

# 12. LEGB

Python uses the LEGB rule for name resolution.

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

Python searches these scopes in order and stops at the first matching name.

## Local

The current function's scope.

```python
x = "global"

def test():
    x = "local"
    print(x)
```

Python finds `x` locally first:

```text
Local → "local" → STOP
```

Output:

```text
local
```

## Enclosing

The scope of an outer function surrounding a nested function.

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        print(x)

    inner()

outer()
```

Inside `inner()`:

```text
Local      → x not found
Enclosing  → x found
```

Therefore:

```text
enclosing
```

## Global

Module-level scope.

```python
x = "global"
```

If `x` isn't found in local or enclosing scopes, Python searches the global scope.

## Built-in

If the name isn't found in local, enclosing, or global scopes, Python searches built-in names.

Example:

```python
def test():
    print(len([1, 2, 3]))
```

There is no local, enclosing, or global `len`, so Python finds the built-in `len`.

If a name cannot be found anywhere in:

```text
Local → Enclosing → Global → Built-in
```

Python raises:

```text
NameError
```

---

# 13. Local / Global / Nonlocal

## `global`

`global` explicitly tells Python that an assignment should modify a module-level/global variable.

```python
x = 10

def test():
    global x
    x = 20

test()

print(x)
```

Output:

```text
20
```

Without `global`, this:

```python
x = 20
```

inside the function would create a local variable.

## `nonlocal`

`nonlocal` refers to a variable in the nearest enclosing function scope.

```python
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)

outer()
```

Output:

```text
20
```

Here:

```text
outer x: 10 → 20
```

The global scope is not modified.

## `global` vs `nonlocal`

```text
global
→ targets module/global scope

nonlocal
→ targets nearest enclosing function scope
```

Example:

```python
x = 10

def outer():
    x = 20

    def inner():
        nonlocal x
        x = 30

    inner()
    print("outer:", x)

outer()

print("global:", x)
```

Output:

```text
outer: 30
global: 10
```

The `nonlocal x` modifies `outer()`'s `x`, not the global `x`.

With:

```python
global x
```

inside `inner()`, the global variable would instead be modified.

---

# 14. Functions as Objects

In Python, a function is an object.

Consider:

```python
def greet():
    print("Hello")
```

The name `greet` refers to a function object.

We can assign that function object to another name:

```python
x = greet
```

This does not call the function.

It creates another reference to the same function object.

Therefore:

```python
greet()
```

and:

```python
x()
```

both execute the same function.

Example:

```python
def greet():
    print("Hello")

x = greet

print(type(greet))
print(type(x))

x()
```

Both:

```python
type(greet)
type(x)
```

produce:

```text
<class 'function'>
```

And:

```python
x()
```

prints:

```text
Hello
```

## Important distinction

```python
x = greet
```

means:

> Assign the function object referenced by `greet` to `x`.

Whereas:

```python
x = greet()
```

means:

> Call `greet()` and assign its return value to `x`.

These are fundamentally different.

Conceptually:

```text
greet ──────┐
            │
            ↓
      function object
            ↑
            │
x ──────────┘
```

Both names refer to the same function object.

---

# Day 3 Implementation

## `calculate_total()`

```python
def calculate_total(numbers):
    if numbers is None or numbers == []:
        return None

    total = 0

    for number in numbers:
        total += number

    return total
```

This function:

* accepts a collection
* calculates the total
* returns the total
* does not print inside the function
* returns `None` for `None` or an empty list

The choice of `None` for an empty collection represents an API design decision: absence of a result rather than a numeric result of zero.

## `calculate_sum(*args)`

```python
def calculate_sum(*args):
    if not args:
        return None

    total = 0

    for number in args:
        total += number

    return total
```

This accepts any number of positional numeric arguments.

Example:

```python
calculate_sum(1, 2, 3)
```

returns:

```text
6
```

## `build_profile(*args, **kwargs)`

```python
def build_profile(*args, **kwargs):
    kwargs.update({"skills": args})
    return kwargs
```

This demonstrates collecting positional and keyword arguments together.

---

# Day 3 Key Takeaways

1. Functions provide reusability, abstraction, and decomposition.
2. Defining a function does not execute its body.
3. Parameters are declared in the function definition.
4. Arguments are supplied during the function call.
5. Positional arguments bind according to position.
6. Keyword arguments bind according to parameter name.
7. Default arguments provide fallback values.
8. `*args` collects positional arguments into a tuple.
9. `**kwargs` collects keyword arguments into a dictionary.
10. `return` sends a value to the caller; `print()` only displays a value.
11. Variables assigned inside a function normally belong to local scope.
12. LEGB means Local → Enclosing → Global → Built-in.
13. `global` targets the global scope.
14. `nonlocal` targets the nearest enclosing function scope.
15. Functions are objects and can be assigned to other names.
16. `x = function` references the function object; `x = function()` calls it and stores its return value.