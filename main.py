# Load students from file
try:
    with open("students.txt", "r") as f:
        students = f.read().splitlines()
except:
    students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        if name in students:
            print("Student already exists!")
        else:
            students.append(name)
            print("Student added!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found")
        else:
            print("\nStudent List:")
            for i, s in enumerate(students, start=1):
                print(i, ".", s)

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in students:
            print("Student found!")
        else:
            print("Student not found")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in students:
            students.remove(name)
            print("Student deleted")
        else:
            print("Student not found")

    elif choice == "5":
        # Save to file before exit
        with open("students.txt", "w") as f:
            for s in students:
                f.write(s + "\n")

        print("Data saved. Exiting...")
        break

    else:
        print("Invalid choice")
        