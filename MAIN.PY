from srm import StudentManager

manager = StudentManager()
manager.load("students.csv")

while True:
    print("\n--- Student Record Manager ---")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Marks")
    print("4. Save & Exit")
    print("5. Display All Students")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("Enter ID: ")
        name = input("Enter Name: ")
        try:
            marks = int(input("Enter Marks: "))
        except ValueError:
            print("Marks must be a number.")
            continue
        manager.add_students(sid, name, marks)

    elif choice == "2":
        sid = input("Enter ID to search: ")
        manager.search(sid)

    elif choice == "3":
        sid = input("Enter ID: ")
        try:
            marks = int(input("Enter Marks: "))
        except ValueError:
            print("Marks must be a number.")
            continue
        manager.update(sid, marks)

    elif choice == "4":
        manager.save("students.csv")
        print("Exiting...")
        break

    elif choice == "5":
        manager.display()

    else:
        print("Invalid choice!")