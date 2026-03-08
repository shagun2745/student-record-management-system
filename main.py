# Student Record Management System

# dictionary to store student records
students = {}

# accepting 3 student records
for i in range(3):
    name = input("Enter student name: ")
    marks = input("Enter marks: ")
    students[name] = marks

# display records
print("\nStudent Records:")
for name, marks in students.items():
    print(name, ":", marks)

# save records to file
file = open("student_records.txt", "w")

for name, marks in students.items():
    file.write(name + " : " + marks + "\n")

file.close()

print("\nRecords saved to file.")

# read file contents
print("\nReading data from file:")
file = open("student_records.txt", "r")

print(file.read())

file.close()
