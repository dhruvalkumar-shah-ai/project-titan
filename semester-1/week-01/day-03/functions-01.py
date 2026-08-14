def calculate_total(numbers):
    """
    a function that:

    accepts a collection of numbers
    calculates the total
    returns the total
    does not print inside the function
    """
    if numbers is None or numbers == []: return None
    total = 0
    for number in numbers:
        total += number
    return total

def calculate_sum(*args):
    """
    a function that:

    accept any number of positional numeric arguments
    return their sum
    """
    if not args: return None
    total = 0
    for number in args:
        total += number
    return total

def build_profile(*args, **kwargs):
    kwargs.update({"skills": args})
    return kwargs

# result = calculate_total([1,2,3,4,5,6])
result = calculate_sum(1, 2, 3)
profile = build_profile(
    "Python",
    "Databricks",
    "Computer Vision",
    name="Dhruval",
    experience=3
)
print(result)
print(profile)