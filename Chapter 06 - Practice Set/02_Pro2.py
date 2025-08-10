# Program to find out whether a student has passed or failed if it requires a total of 40% and atleast 33% in each subject to pass.
# Assume 3 subjects and take marks as an input from the user.

Math = int(input("Enter the math marks= "))
OR = int(input("Enter the OR marks= "))
AOA = int(input("Enter the AOA marks= "))

total_percentage = ((Math+OR+AOA)/300)*100
print(total_percentage)

if(total_percentage>=40 and Math>=33 and OR>=33 and AOA>=33):
    print("You are passed.", total_percentage)

else:
    print("You are failed. Try again next year in sha allah", total_percentage)