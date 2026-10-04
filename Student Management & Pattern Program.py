students = []
subjects_set = set()

def add_student():
    name = input("Enter student name: ")
    roll_no = int(input("Enter roll number: "))
    subject = input("Enter subject: ")
    marks = int(input("Enter marks: "))

    subjects_set.add(subject)

    student_info = (name, roll_no)
    student_dict = {"info": student_info,"subject": subject, "marks": marks }
    students.append(student_dict)
    print("Student added successfully!\n")


def show_students():
    if len(students) == 0:
        print("No students added yet.\n")
        return
    print("\n------ ALL STUDENTS ------")
    for i in range(len(students)):
        s = students[i]
        print(f"{i+1}. Name: {s['info'][0]}, Roll No: {s['info'][1]}, Subject: {s['subject']}, Marks: {s['marks']}")
    print()


def show_subjects():
    print("\n------ UNIQUE SUBJECTS TAUGHT ------")
    for sub in subjects_set:
        print(sub)
    print()


def calculate_average():
    if len(students) == 0:
        print("No data to calculate average.\n")
        return
    total = 0
    for s in students:
        total += s["marks"]
    average = total / len(students)
    print(f"\nClass Average Marks: {average:.2f}\n")


def print_pattern():
    rows = int(input("Enter number of rows for pattern: "))
    choice = int(input("Press 1 for Triangle, 2 for Pyramid, 3 for Number Triangle: "))

    if choice == 1:
        i = 1
        while i <= rows:
            print("*" * i)
            i += 1

    elif choice == 2:
        for i in range(1, rows+1):
            print(" " * (rows-i) + "*" * (2*i-1))

    elif choice == 3:
        for i in range(1, rows+1):
            line = ""
            for j in range(1, i+1):
                line += str(j) + " "
            print(line)

    else:
        print("Invalid choice")
    print()


def menu():
    print("====== STUDENT MANAGEMENT & PATTERN TOOLKIT ======")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Show Unique Subjects")
    print("4. Calculate Class Average")
    print("5. Print Pattern")
    print("6. Exit")


while True:
    menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        show_students()
    elif choice == 3:
        show_subjects()
    elif choice == 4:
        calculate_average()
    elif choice == 5:
        print_pattern()
    elif choice == 6:
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid choice, try again.\n")