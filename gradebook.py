print('''--------------------------------------------------------
Title      : GradeBook Analyzer
Course     : Programming for Problem Solving using Python
Author     : Shubham Halder 
Date       : 2025-11-03
Roll No.   : 2501410002
--------------------------------------------------------''')

# MENU 
def display_menu():
    print("\n===== GRADEBOOK ANALYZER =====")
    print("1. Enter student data manually")
    print("2. Show statistics")
    print("3. Show grade distribution") 
    print("4. Show pass/fail results")
    print("5. Display all students")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    return choice

# INPUT STUDENT NAMES 
def input_names():
    names = []
    num_students = int(input("Enter number of students: "))
    for i in range(num_students):
        name = input(f"Enter Student {i+1} Name : ")
        names.append(name)
    return names

# INPUT MARKS
def input_marks(names):
    marks = []
    for n in names:
        mark = float(input(f"Enter marks of {n}: "))
        marks.append(mark)
    return marks

# AVERAGE 
def calculate_average(marks):
    total = 0
    for m in marks:
        total += m
    return total / len(marks)

# MEDIAN
def calculate_median(marks):
    sorted_marks = sorted(marks)
    n = len(sorted_marks)
    if n % 2 == 1:
        return sorted_marks[n // 2]
    else:
        return (sorted_marks[n // 2 - 1] + sorted_marks[n // 2]) / 2

# GRADES 
def calculate_grades(marks):
    grade_list = []
    for m in marks:
        if m >= 90:
            grade_list.append('A')
        elif m >= 80:
            grade_list.append('B')
        elif m >= 70:
            grade_list.append('C')
        elif m >= 60:
            grade_list.append('D')
        else:
            grade_list.append('F')
    return grade_list

# TOPPER & LOWEST 
def topper_and_lowest(names, marks):
    highest = max(marks)
    lowest = min(marks)
    toppers = []
    lows = []
    for i in range(len(marks)):
        if marks[i] == highest:
            toppers.append(names[i])
        if marks[i] == lowest:
            lows.append(names[i])
    return toppers, lows

# GRADE DISTRIBUTION
def show_grade_distribution(grades):
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    f_count = 0
    
    for grade in grades:
        if grade == 'A':
            a_count += 1
        elif grade == 'B':
            b_count += 1
        elif grade == 'C':
            c_count += 1
        elif grade == 'D':
            d_count += 1
        elif grade == 'F':
            f_count += 1
    
    print("\n--- GRADE DISTRIBUTION ---")
    print(f"A: {a_count} students")
    print(f"B: {b_count} students")
    print(f"C: {c_count} students")
    print(f"D: {d_count} students")
    print(f"F: {f_count} students")

# PASS/FAIL ANALYSIS
def show_pass_fail(names, marks):
    passed = []
    failed = []
    
    for i in range(len(marks)):
        if marks[i] >= 40:
            passed.append(names[i])
        else:
            failed.append(names[i])
    
    print("\n--- PASS/FAIL ANALYSIS ---")
    print(f"PASSED (≥40): {len(passed)} students")
    if passed:
        print("Names: " + ", ".join(passed))
    
    print(f"\nFAILED (<40): {len(failed)} students")
    if failed:
        print("Names: " + ", ".join(failed))

# DISPLAY ALL STUDENTS
def display_all_students(names, marks, grades):
    print("\n===== ALL STUDENTS =====")
    print("Name\t\tMarks\tGrade")
    print("----\t\t-----\t-----")
    for i in range(len(names)):
        print(f"{names[i]}\t\t{marks[i]}\t{grades[i]}")

# MAIN FUNCTION 
def main():
    student_names = []
    student_marks = []
    student_grades = []
    
    while True:
        choice = display_menu()
        
        if choice == '1':
            student_names = input_names()
            student_marks = input_marks(student_names)
            student_grades = calculate_grades(student_marks)
            print(f"\n Added {len(student_names)} students successfully!")
            
        elif choice == '2':
            if len(student_names) == 0:
                print(" No student data available. Please enter data first.")
            else:
                avg = calculate_average(student_marks)
                median = calculate_median(student_marks)
                toppers, lows = topper_and_lowest(student_names, student_marks)
                
                print("\n===== STATISTICS =====")
                print(f"Total Students : {len(student_names)}")
                print(f"Average Marks  : {avg:.2f}")
                print(f"Median Marks   : {median:.2f}")
                print(f"Highest Score  : {max(student_marks)} by {toppers}")
                print(f"Lowest Score   : {min(student_marks)} by {lows}")
                
        elif choice == '3':
            if len(student_names) == 0:
                print(" No student data available. Please enter data first.")
            else:
                show_grade_distribution(student_grades)
                
        elif choice == '4':
            if len(student_names) == 0:
                print(" No student data available. Please enter data first.")
            else:
                show_pass_fail(student_names, student_marks)
                
        elif choice == '5':
            if len(student_names) == 0:
                print(" No student data available. Please enter data first.")
            else:
                display_all_students(student_names, student_marks, student_grades)
                
        elif choice == '6':
            print(" Exiting program. Goodbye!")
            break
            
        else:
            print(" Invalid choice! Try again.")

main()

