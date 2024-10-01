# Initial list of students with their marks (stored as tuples)
students = [("Akansha", 43), ("Fyz", 29), ("Shubham", 40)]

# Function to display the list of students
def student_data(students):
    print("List of students:")
    for name, marks in students:
        print(f"Name: {name}, Marks: {marks}")
    print()


student_data(students)

def add_student(students, name, marks):
    students.append((name, marks))
    print(f"Added {name} with {marks} marks.\n")

# Function to remove a student by name
def remove_student(students, name):
    students[:] = [student for student in students if student[0] != name]
    print(f"Removed {name}.\n")
    