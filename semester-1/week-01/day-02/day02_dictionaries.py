employee = {
    "name":"Dhruval",
    "role": "AI Developer",
    "experience": 3,
    "department": "AI/ML",
    "skills": ["Python", "Azure", "ML"]
}
print("Name ",employee["name"])
print("Role ", employee["role"])
print("Experience ", employee["experience"])
print("Department ", employee["department"])
print("Skills ", employee["skills"])

employee = {
    "name": "Dhruval",
    "role": "AI Developer"
}
employee["experience"] = 3 # employee.update({"experience": 3})
employee["location"]="Bangalore" # employee.update({"location": "Bangalore"})
print(employee)

employee = {
    "name": "Dhruval",
    "role": "AI Developer"
}
print(employee.get("name"))
print(employee["name"])
print(employee.get("salary"))
# print(employee["salary"]) # This would give KeyError

employee = {
    "name": "Dhruval",
    "role": "AI Developer",
    "experience": 3,
    "location": "Bangalore"
}
# Print only keys
for key in employee.keys():
    print(key)

# Print only values
for value in employee.values():
    print(value)

# Print both key & value
for key, value in employee.items():
    print(key, value)

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
freq={}
for num in numbers:
    freq[num] = freq.get(num, 0) + 1
# We use get function so that we don't face KeyError the first time we try to access element
# Or we may not have to use if condition (if num in freq:)

company = {
    "name": "Project Titan",
    "employee": {
        "name": "Dhruval",
        "role": "AI Developer",
        "skills": {
            "primary": "Python",
            "secondary": "SQL"
        }
    }
}
print(company["name"])
print(company["employee"]["name"])
print(company["employee"]["role"])
print(company["employee"]["skills"]["primary"])
print(company["employee"]["skills"]["secondary"])

numbers = [1, 2, 3, 4, 5]
square_numbers = {
   num: num ** 2 for num in numbers
}
print(square_numbers)

students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95
}
highest_score_student, above_85, highest_score, avg_score = None, [], 0, 0
for student in students.keys():
    if highest_score_student is None:
        highest_score_student = student
        highest_score = students.get(student)
    score = students.get(student)
    if score > 85:
        above_85.append(student)
    if score > highest_score:
        highest_score = score
        highest_score_student = student
    avg_score += score
if len(students)>0:
    print(highest_score_student, highest_score, above_85, avg_score / len(students))
else:
    print("No students")

employees = [
    {"name": "A", "department": "Data", "salary": 80000},
    {"name": "B", "department": "AI", "salary": 90000},
    {"name": "C", "department": "Data", "salary": 85000},
    {"name": "D", "department": "AI", "salary": 95000}
]

emp_count, emp_salary = {}, {}
highest_salary, highest_salary_emp = None, None

for employee in employees:
    department = employee.get("department")
    salary = employee.get("salary")
    name = employee.get("name")

    emp_count[department] = emp_count.get(department, 0) + 1
    emp_salary[department] = emp_salary.get(department, 0) + salary

    if highest_salary is None:
        highest_salary = salary
        highest_salary_emp = name
    if salary > highest_salary:
        highest_salary = salary
        highest_salary_emp = name

avg_salary = {}
highest_avg_salary_dept , highest_avg_salary = None, None

for key in emp_count:
    avg_salary[key] = emp_salary[key] / emp_count[key]
    if highest_avg_salary_dept is None:
        highest_avg_salary_dept = key
        highest_avg_salary = avg_salary[key]
    if avg_salary[key] > highest_avg_salary:
        highest_avg_salary = avg_salary[key]
        highest_avg_salary_dept = key
print(emp_count) # Employees per department
print(avg_salary) # Average salary per department
print(highest_salary_emp) # Employee with highest salary
print(highest_avg_salary_dept) # Department with highest average salary

employee = {
    "name": "Dhruval",
    "role": "AI Developer",
    "experience": 3
}
employee.pop("role")
employee.update({"role" : "AI Engineer"})
del employee["experience"]
print(employee)