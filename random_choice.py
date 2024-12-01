import random

student_grades = ["A", "B", "C", "D"]

# Below two lines are just to check concepts
print(type(student_grades))
print(f"Hello there {random.choice(student_grades)}")

# Two methis either print directly or save it in a variable and then print
print(random.choice(student_grades))
results = random.choice(student_grades)
print(results)

# Find the length and choose from a range of integer of that length
print(len(student_grades))
final_grade = random.randint(0, 3)

# Used the print statement with round brackets and gets an error: print(student_grades(final_grade))
print(student_grades[final_grade])