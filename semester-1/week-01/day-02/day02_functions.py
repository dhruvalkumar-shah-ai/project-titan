def calculate_sum(numbers):
    """
    Calculate sum of numbers without using sum()
    """
    if len(numbers)==0: return None
    sum_val = 0
    for num in numbers:
        sum_val += num
    return sum_val

def calculate_statistics(numbers):
    """
    Return statistics of list like max, min, sum and average without using standand Python list functions.
    """
    """
        Currently:

        max_val, min_val, sum_val, avg_val = None, None, None, None

        then later you return those values for an empty list.

        That's not wrong.

        But I want you to start thinking about what your function's contract should be.

        For an empty list, what should:

        calculate_statistics([])

        return?

        Possibilities:

        (None, None, 0, None)

        or:

        None

        or raise an exception.

        We should explicitly decide that rather than accidentally inheriting behavior from initialization.

        Also:

        You return:

        return [max_val, min_val, sum_val, avg_val]

        This technically works, but conceptually these are four related results, and a tuple is more appropriate:

        return max_val, min_val, sum_val, avg_val
    """
    if len(numbers)>0:
        max_val, min_val, sum_val, avg_val = numbers[0], numbers[0], 0, 0
        for num in numbers:
            if num > max_val:
                max_val = num
            if num < min_val:
                min_val = num
            sum_val += num
        avg_val = sum_val / len(numbers)
        return max_val, min_val, sum_val, avg_val
    return None

def separate_even_odd(numbers):
    """
    Return a tuple seperating even and odd numbers from the list.
    """
    even_list, odd_list = [], []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    return even_list, odd_list # return even_list, odd_list; this returns tuples by default.

def count_frequency(numbers):
    """
    Return a dictionary containing count (frequency) of each element
    """
    freq={}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    return freq

def find_maximum(*numbers):
    """
    Return maximum value from received tuple.
    """
    if len(numbers) > 0:
        max_val = numbers[0]
        for num in numbers:  # You could avoid processing the first number twice by switching to numbers[1:]
            if num > max_val:
                max_val = num
        return max_val
    return None

def create_employee(**details):
    """
    Return the received dictionary as-is.
    """
    return details # **kwargs collects arbitrary keyword arguments into a dictionary.

def analyze_numbers(numbers):
    """
    Return analytics of given list with a dictionary containing maximum, minimum, sum, average, even_count and odd_count
    """
    ans_dict = {}
    if len(numbers)==0:
        ans_dict["count"]=0
        ans_dict["unique_count"]=0
        ans_dict["maximum"]=None
        ans_dict["minimum"]=None
        ans_dict["sum"]=None
        ans_dict["average"]=None
        ans_dict["even_count"]=0
        ans_dict["odd_count"]=0
        return ans_dict
    ans_dict["count"]= len(numbers)
    ans_dict["unique_count"]= len(set(numbers))
    max_val, min_val, sum_val, avg_val = calculate_statistics(numbers)
    ans_dict["maximum"]= max_val
    ans_dict["minimum"]= min_val
    ans_dict["sum"]= sum_val
    ans_dict["average"]= avg_val
    even_list, odd_list = separate_even_odd(numbers)
    ans_dict["even_count"]= len(even_list)
    ans_dict["odd_count"]= len(odd_list)
    return ans_dict


print(calculate_sum([10, 20, 30, 40]))
print(calculate_statistics([10, 20, 30, 40]))
print(separate_even_odd([1, 2, 3, 4, 5, 6]))
print(count_frequency([1, 2, 2, 3, 3, 3, 4]))
print(find_maximum(10, 20, 5, 40, 15))
print(create_employee(
    name="Dhruval",
    role="AI Developer",
    experience=3,
    skills={"Python", "SQL", "Azure"}
))
print(analyze_numbers([10, 20, 20, 30, 40, 40, 50, 50, 50]))
