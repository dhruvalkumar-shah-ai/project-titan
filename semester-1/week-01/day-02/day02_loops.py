for num in range(1, 101):
    # range starts with 0; so added start with 1 and ending is excluded so end is 101
    print(num)

for num in range(1, 51):
    if num % 2 == 0:
        print(num)
# print([num for num in range(1, 51) if num % 2 ==0])

numbers = [10, 20, 30, 40, 50]
if len(numbers) > 0:
    sum_val, min_val, max_val = numbers[0], numbers[0], numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
        sum_val += num

    avg = sum_val / len(numbers)
    print(sum_val, avg, max_val, min_val)
else:
    print("Empty list")

numbers = [10, 15, 20, 35, 40, 50]
for num in numbers:
    if num > 30:
        print(num)
        break

numbers = [10, 15, 20, 25, 30, 35]
for num in numbers:
    if num % 10 == 0:
        print(num)
    else:
        continue
"""
This demonstrates the purpose of continue more naturally:

invalid → skip
valid   → process

Your current implementation isn't wrong. This is just cleaner.
"""



skills = ["Python", "SQL", "PySpark", "Azure"]
for idx, skill in enumerate(skills, start = 1):
    # Enumerate starts with 0; our requirement is to start with 1
    print(idx, skill)

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(name, score)

"""
For Pattern:
1 2 3
1 2 3
1 2 3
"""
for i in range(1, 4):
    for j in range(1, 4):
        print(j, end = " ")
    print()

"""
For Pattern:
1
1 2
1 2 3
"""
for i in range(1, 4):
    for j in range(1, i+1):
        print(j, end = " ")
    print()

numbers = [10, 20, 30, 20, 40, 10]
unique_ele = set()
for num in numbers:
    if num in unique_ele:
        print(num)
        break
    else:
        unique_ele.add(num)

def find_number(numbers, target):
    for num in numbers:
        if num == target:
            print("Found")
            break
    else:
        print("Not Found")

find_number([10, 20, 30, 40, 50], 30)
find_number([10, 20, 30, 40, 50], 35)

numbers = [10, 20, 10, 30, 20, 40, 50, 30]
print("Count ", len(numbers))
print("Unique Count ", len(set(numbers)))
freq_count, max_val, min_val, first_duplicate = {}, None, None, None
for num in numbers:
    freq_count[num] = freq_count.get(num, 0) + 1
    if max_val is None:
        max_val = num
    if min_val is None:
        min_val = num
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num
    if first_duplicate is None and freq_count[num] == 2:
        first_duplicate = num
print("Frequency ", freq_count)
print("Maximum ", max_val)
print("Minimum ", min_val)
print("First Duplicate ", first_duplicate)

count = 10
while count>0:
    print(count)
    count-=1

while True:
    number = int(input("Enter number: "))

    if number == 0:
        break