# Program to calculate the grade of student from his marks according to our university standard.

marks = int(input("Enter your marks = "))

if(marks<=100 and marks>=85):
    grade = "Grade A+"

elif(marks<85 and marks>80):
    grade = "Grade A"

elif(marks<80 and marks>75):
    grade = "Grade B+"

elif(marks<75 and marks>70):
    grade = "Grade B"

elif(marks<70 and marks>65):
    grade = "Grade C+"

elif(marks<65 and marks>60):
    grade = "Grade C"

elif(marks<60 and marks>=55):
    grade = "Grade D+"

elif(marks<55 and marks>=50):
    grade = "Grade D"

elif(marks<50):
    grade = "Grade F"

print(f"Acoording to your marks {marks} you got a {grade}.")