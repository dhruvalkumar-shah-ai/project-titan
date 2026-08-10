numbers = [10, 25, 7, 42, 18, 31, 6]
# PROBLEM-1 ---> First element, Last element, First 3 elements, Last 3 elements, List in reverse order
print(numbers[0]) # First element
print(numbers[-1]) # Last element
print(numbers[:3]) # First 3 elements
print(numbers[-3:]) # Last 3 elements
print(numbers[::-1]) # List in reverse order

# PROBLEM-2 ---> Even, odd and square numbers
even_numbers = [no for no in numbers if no%2 == 0]
odd_numbers = [no for no in numbers if no%2 != 0]
squares = [no **2 for no in numbers]
print(even_numbers)
print(odd_numbers)
print(squares)

# PROBLEM-3 ---> Calculate maximum_val, minimum_val, sum_val, average_val
maximum_val, minimum_val, sum_val, average_val = None, None, None, None
if len(numbers)>0:
    maximum_val, minimum_val, sum_val = numbers[0], numbers[0], 0
    for no in numbers:
        if no > maximum_val:
            maximum_val = no
        if no < minimum_val:
            minimum_val=no
        sum_val += no

    average_val = sum_val/len(numbers)
print(maximum_val)
print(minimum_val)
print(sum_val)
print(average_val)

# PROBLEM-4 ---> Only unique elements, without using set() function
unique_li=[]
numbers = [10, 20, 30, 20, 40, 10, 50]
for no in numbers:
    if no not in unique_li:
        unique_li.append(no)
print(unique_li)

# PROBLEM-5 ----> We're aiming for second largest (unique) number
numbers = [5, 2, 9, 1, 7]
maximum_val, second_maximum_val = None, None
if len(numbers)>=2:
    if numbers[0]> numbers[1]:
        maximum_val = numbers[0]
        second_maximum_val = numbers[1]
    else:
        maximum_val = numbers[1]
        second_maximum_val = numbers[0]
    for no in numbers:
        if no > maximum_val:
            second_maximum_val = maximum_val
            maximum_val = no
        elif no > second_maximum_val and no!=maximum_val:
            second_maximum_val = no
print(second_maximum_val)