employees = [
    {
        "name": "Alice",
        "department": "Data",
        "salary": 80000,
        "skills": {"Python", "SQL"}
    },
    {
        "name": "Bob",
        "department": "AI",
        "salary": 90000,
        "skills": {"Python", "ML"}
    },
    {
        "name": "Charlie",
        "department": "Data",
        "salary": 85000,
        "skills": {"SQL", "PySpark"}
    },
    {
        "name": "David",
        "department": "AI",
        "salary": 95000,
        "skills": {"Python", "Deep Learning"}
    }
]

def get_departments(employees):
    """
    Returns unique departments
    """
    unique_department=set()
    for employee in employees:
        unique_department.add(employee["department"])
    return unique_department

def count_by_department(employees):
    """
    Returns employee strength per department
    """
    department_count = {}
    for employee in employees:
        department_count[employee["department"]] = department_count.get(employee["department"], 0) + 1
    return department_count

def average_salary_by_department(employees):
    """
    Returns average salary by department
    """
    department_salary = {}
    for employee in employees:
        department_salary[employee["department"]] = department_salary.get(employee["department"], 0) + employee["salary"]
    
    department_count = count_by_department(employees)
    for department in department_salary.keys():
        department_salary[department] = department_salary[department] / department_count[department]
    return department_salary

def find_highest_paid(employees):
    """
    Returns name and salary of highest paid employee
    """
    highest_paid_emp, highest_salary = None, None
    for employee in employees:
        if highest_salary is None:
            highest_salary = employee["salary"]
            highest_paid_emp = employee["name"]
        elif employee["salary"] > highest_salary:
            highest_salary = employee["salary"]
            highest_paid_emp = employee["name"]
    return highest_paid_emp, highest_salary

def get_all_skills(employees):
    """
    Returns unique skill set of all employees
    """
    all_skills = set()
    for employee in employees:
        all_skills.update(employee["skills"])
    return all_skills

def employees_with_skill(employees, req_skill):
    """
    Returns a list of employees with required skill
    """
    skilled_employees = []
    for employee in employees:
        """
        Employee may or may not have skills; therefore it's advisable to use get() function instead of direct access
        """
        if req_skill in employee.get("skills", set()):
            skilled_employees.append(employee["name"])
    return skilled_employees

def highest_salary_by_department(employees):
    """
    Return highest salary by department
    """
    highest_salary = {}
    for employee in employees:
        salary, department = employee["salary"], employee["department"]
        if salary > highest_salary.get(department, 0):
            highest_salary[department] = salary
    return highest_salary

def department_salary_report(employees):
    """
    Generate per department statistics
    """
    department_statistics = {}
    department_count = count_by_department(employees)
    avg_salary_by_department = average_salary_by_department(employees)
    max_salary_by_department = highest_salary_by_department(employees)
    for department in department_count.keys():
        temp_department = {}
        temp_department["department"] = department
        temp_department["employees"] = department_count[department]
        temp_department["average_salary"] = avg_salary_by_department[department]
        temp_department["highest_salary"] = max_salary_by_department[department]
        department_statistics[department]=temp_department
    return department_statistics


def analyze_employees(employees):
    """
    Function displaying statistics related to employees
    """
    print("Total Employees: ", len(employees))
    print("Unique Departments: ", get_departments(employees))
    print("Employee count by department: ", count_by_department(employees))
    avg_salary_by_department = average_salary_by_department(employees)
    print("Average salary by department: ", avg_salary_by_department)
    highest_paid_emp, highest_salary = find_highest_paid(employees)
    print("Highest Paid Employee: ", highest_paid_emp, " → ", highest_salary)
    print("Unique Skills: ", get_all_skills(employees))
    print("Employees having Python Skill: ", employees_with_skill(employees, "Python"))
    max_salary, max_salary_dept = None, None
    if len(avg_salary_by_department)>0:
        for department, salary in avg_salary_by_department.items():
            if max_salary is None:
                max_salary = salary
                max_salary_dept = department
            elif salary > max_salary:
                max_salary = salary
                max_salary_dept = department
    print("Department with highest average salary: ", max_salary_dept, " → ", max_salary)
    print("Department wise report: ", department_salary_report(employees))


analyze_employees(employees)