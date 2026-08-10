numbers = [10, 20, 20, 30, 40, 40, 50, 50, 50]
unique_num = set(numbers)

# Number of unique elements:
print(len(unique_num))

# Check membership
skills = {"Python", "SQL", "PySpark", "Azure", "Databricks"}
job_skills = ["Python", "Java", "SQL", "AWS"]

for skill in job_skills:
    print(skill, " → ", skill in skills)

my_skills = {
    "Python",
    "SQL",
    "PySpark",
    "Azure",
    "Power BI"
}

job_skills = {
    "Python",
    "SQL",
    "Spark",
    "AWS",
    "Databricks"
}
print(my_skills.intersection(job_skills)) # Skills I already have that job requires
print(job_skills.difference(my_skills)) # Skills required by job that I'm missing
print(my_skills.difference(job_skills)) # Skills I have that job doesn't require

numbers = [10, 20, 30, 20, 40, 50, 10, 60]
if len(numbers) == len(set(numbers)):
    print("No Duplicates")
else:
    print("Duplicates exist")

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
set_a, set_b = set(list_a), set(list_b)
print(set_a & set_b)
print(set_a.difference(set_b))
print(set_b.difference(set_a))
print(set_a | set_b)