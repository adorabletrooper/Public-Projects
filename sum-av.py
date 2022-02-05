"""
Program to print the sum and average of n numbers entered by the user.
"""
n = int(input("Enter the value of n: "))
count = n
sumNum = 0
while count != 0:
    sumNum += int(input(f"[{count} number added]Enter number: "))
    count -= 1

print(f"Sum of the {n} numbers input: {sumNum}\nAverage of the {n} numbers input: "+ str(sumNum / n))