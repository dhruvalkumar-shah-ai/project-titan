employee = ("Dhruval", "AI Developer", 3, "Python")
print("name ", employee[0])
print("role ", employee[1])
print("experience ", employee[2])
print("skill ", employee[3])

numbers = (10, 20, 30, 40, 50, 60)
print(numbers[:3]) # First 3 elements
print(numbers[-3:]) # Last 3 elements
print(numbers[::-1]) # Reversed Tuple

numbers = (10, 20, 30)
# numbers[0] = 100; Since numbers is an object of class Tuple;
# it can't be modified once created
# The tuple structure/bindings can't be changed. 
# If a tuple contains a mutable object such as a list,
# that nested object can still be modified.


a = (10)
b = (10,)
print(type(a)) # ---> int
print(type(b)) # ---> tuple
# The comma is what makes the expression a tuple;
# parentheses are often just used for grouping/readability.

employee = ("Dhruval", "AI Developer", 3)
name, role, experience = employee
print(name)
print(role)
print(experience)

numbers = (10, 20, 30, 40, 50, 60)
first, *middle, last = numbers
print(first)
print(middle)
print(last)

numbers = (10, 20, 20, 30, 20, 40)
# count_20=0
# for num in numbers:
#     if num == 20:
#         count_20 +=1
# print(count_20)
print(numbers.count(20))
print(numbers.index(30))

# When would you choose a tuple instead of a list?
# When we know that once declared, we wouldn't have to change
# the members of a datastructure; we select tuple
# else we select list.

# Engineering Reason:
# Let's say I want to store information regarding my birth-date
# or aadhar number then I can use tuple; since once declared
# they're bound to remain unchanged; whereas phone-number, email,
# address etc. can be changed and therefore must be stored as list.