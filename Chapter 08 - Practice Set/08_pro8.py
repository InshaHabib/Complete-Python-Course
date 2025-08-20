# Print python function to print multiplication table of a given number.

def func_table(num):
    for i in range(1,13):
        print(f"{num} * {i} = {num*i}")
    return "Table printed successfully."

print(func_table(int(input("Enter a number to print it's table: "))))

 