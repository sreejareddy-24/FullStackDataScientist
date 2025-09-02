#Write a python script to enter student number, name, marks in c, c++ and java calculate and display total marks, average, result and grade. Print fail if student average is less than 70.  

name = input("Enter student name: ")
s_number = int(input("Enter student number: "))
c_marks = int(input("Enter your marks in C: "))
cpp_marks = int(input("Enter your marks in C++: "))
java_marks = int(input("Enter your marks in Java: "))


total_marks = c_marks + cpp_marks + java_marks
avg_marks = total_marks / 3


if avg_marks < 70:
    result = "FAIL"
    grade = "F"
else:
    result = "PASS"
    if avg_marks >= 90:
        grade = "A"
    elif avg_marks >= 80:
        grade = "B"
    elif avg_marks >= 70:
        grade = "C"
    else:
        grade = "D"


print("\n--- Student Report ---")
print("Student Number:", s_number)
print("Student Name:", name)
print("Marks in C:", c_marks)
print("Marks in C++:", cpp_marks)
print("Marks in Java:", java_marks)
print("Total Marks:", total_marks)
print("Average Marks:", avg_marks)
print("Result:", result)
print("Grade:", grade)
