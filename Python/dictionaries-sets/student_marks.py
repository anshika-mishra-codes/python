marks = {
    "Anshu": 80,
    "Mahek": 65,
    "Shraddha": 90
}

name = input("Enter student name: ")

if name in marks:
    print("Marks:", marks[name])
else:
    print("Student not found")