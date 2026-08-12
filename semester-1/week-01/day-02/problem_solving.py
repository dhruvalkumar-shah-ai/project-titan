numbers = [4, 5, 1, 2, 1, 4, 5, 6]
employees = [
    {"name": "A", "department": "Data", "salary": 80000},
    {"name": "B", "department": "AI", "salary": 95000},
    {"name": "C", "department": "Data", "salary": 90000},
    {"name": "D", "department": "AI", "salary": 85000},
    {"name": "E", "department": "Data", "salary": 100000}
]

def first_non_repeating(numbers):
    """
    Return First non-repeating number from given list
    """
    if len(numbers)==0: return None
    freq_count = {}
    for number in numbers:
        freq_count[number] = freq_count.get(number, 0) + 1
    for number in numbers:
        if freq_count[number] == 1:
            return number
    return None
    

def departmental_analysis(employees):
    """
    Return departmental analysis over employees data-dictionary.
    """
    department_statistics = {}
    highest_paid_emp, highest_salary = None, None
    for employee in employees:
        name, department, salary = employee["name"], employee["department"], employee["salary"]
        if highest_salary is None:
            highest_salary = salary
            highest_paid_emp = name
        if salary > highest_salary:
            highest_salary = salary
            highest_paid_emp = name
        
        if department in department_statistics:
            department_statistics[department]["emp_count"] += 1
            department_statistics[department]["salary"] += salary
        else:
            department_statistics[department] = {"emp_count": 1, "salary": salary}
    
    highest_avg_salary, dept_highest_avg_salary = None, None
    for department in department_statistics.keys():
        avg_salary = department_statistics[department]["salary"] / department_statistics[department]["emp_count"]
        department_statistics[department]["avg_salary"] = avg_salary

        if highest_avg_salary is None:
            highest_avg_salary = avg_salary
            dept_highest_avg_salary = department
        if avg_salary > highest_avg_salary:
            highest_avg_salary = avg_salary
            dept_highest_avg_salary = department
    
    return department_statistics, highest_paid_emp, dept_highest_avg_salary

first_non_repeating_number = first_non_repeating(numbers)
department_statistics, highest_paid_emp, dept_highest_avg_salary = departmental_analysis(employees)
print(first_non_repeating_number)
for department in department_statistics.keys():
    print("Department Name: ", department, "Employee Count: ", department_statistics[department]["emp_count"], "Average Salary: ", department_statistics[department]["avg_salary"])
print("Highest Paid Employee: ", highest_paid_emp)
print("Department with Highest Average Salary: ", dept_highest_avg_salary)

