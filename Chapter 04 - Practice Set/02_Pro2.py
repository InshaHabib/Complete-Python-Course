# Program to accept marks of 6 students and display then in a sorted manner.
marks = []

stu1 = int(input("Enter marks here:"))
marks.append(stu1)
stu2 = int(input("Enter marks here:"))
marks.append(stu2)
stu3 = int(input("Enter marks here:"))
marks.append(stu3)
stu4 = int(input("Enter marks here:"))
marks.append(stu4)
stu5 = int(input("Enter marks here:"))
marks.append(stu5)
stu6 = int(input("Enter marks here:"))
marks.append(stu6)

marks.sort()
print(marks)