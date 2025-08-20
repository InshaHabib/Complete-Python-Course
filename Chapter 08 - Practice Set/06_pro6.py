# Python function which converts inches to cms.

def function(n):
    cms = n * 2.54
    print(f"{n} inches is equal to {cms} cms")

function(int(input("Enter the number of inches to convert to cms: ")))