from details import Students
from tabulate import tabulate
students_class:int=int(input("enter class of a student eg. 1a-10b : "))
numberofstudents:int=int(input("enter no.of students in a class : "))
numberofsubjects:int=int(input("enter no.of subjects : "))
subjects=[]
students=[]

for _ in range(numberofsubjects):
    subjects_name:str=input(f"enter {_+1} subject name  : ")
    subjects.append(subjects_name)

for _ in range(numberofstudents):
    roll_number=int(input("enter a student roll_number : "))
    students_name:str=input(f"enter a student name {roll_number} : ")
    student=Students(students_name,roll_number)
    is_student_fail:bool=False
    for subject in subjects:
        marks=int(input(f"enter a {students_name} marks in {subject} : "))
        
        if marks < 0 or marks > 100:
            print("you have entered out of range value ")
            marks=0
        if marks < 40:
            is_student_fail = True
        student.add_marks(subject,marks)
    student.total_marks=sum(student.marks.values())

    if is_student_fail:
        student.grade = "F"
        student.result = "Fail"
    else:
        average_marks = student.total_marks / len(subjects)
        if average_marks >= 90:
            student.grade = "A+"
        elif average_marks >= 80:
            student.grade = "A"
        elif average_marks >= 70:
            student.grade = "B"
        elif average_marks >= 60:
            student.grade = "C"
        elif average_marks >= 50:
            student.grade = "D"
        else:
            student.grade = "E"
        student.result = "Pass"

    students.append(student)
print(f"Report card of a student class {students_class}")
table=[]
header=["name","roll_number"]+subjects+["total","result","grade"]
for student in students:
    report=student.get_report()
    row=[report["students_name"],report["roll_number"]]
    for subject in subjects:
        row.append(report["marks"].get(subject,0))
    row.extend([report["total_marks"],
                report["result"],
                report["grade"]])
    table.append(row)

print(tabulate(table,headers=header,tablefmt="grid"))
    