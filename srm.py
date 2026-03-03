import csv

class Student:
    def __init__(self, student_id, name, marks):
        if not (0 <= marks <= 100):
            raise ValueError("Marks must be between 0 and 100")

        self.student_id = student_id
        self.name = name
        self.marks = marks

    def update_marks(self, new_marks):
        if not (0 <= new_marks <= 100):
            raise ValueError("Marks must be between 0 and 100")

        self.marks = new_marks

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Marks: {self.marks}"


class StudentManager:
    def __init__(self):
        self.students = {}  # key = student_id, value = Student object

    def add_student(self, student_id, name, marks):
        if student_id in self.students:
            print("Student ID already exists!")
            return

        try:
            self.students[student_id] = Student(student_id, name, marks)
            print("Student added successfully!")
        except ValueError as e:
            print(e)

    def search_student(self, student_id):
        student = self.students.get(student_id)
        if student:
            print(student)
        else:
            print("Student not found!")

    def update_student(self, student_id, new_marks):
        student = self.students.get(student_id)
        if not student:
            print("Student not found!")
            return

        try:
            student.update_marks(new_marks)
            print("Marks updated successfully!")
        except ValueError as e:
            print(e)

    def display_all(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students.values():
            print(student)

    def save_to_csv(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Marks"])

            for student in self.students.values():
                writer.writerow(
                    [student.student_id, student.name, student.marks]
                )

        print("Data saved successfully!")

    def load_from_csv(self, filename):
        try:
            with open(filename, "r") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    student_id = row["ID"]
                    name = row["Name"]
                    marks = int(row["Marks"])

                    self.students[student_id] = Student(
                        student_id, name, marks
                    )

            print("Data loaded successfully!")

        except FileNotFoundError:
            print("CSV file not found. Starting fresh.")