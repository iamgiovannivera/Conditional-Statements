#The Greatest Showdown
#Task 1
num1 = int(input("Assign first number: "))
num2 = int(input("Assign second number: "))
num3 = int(input("Assign third number: "))

if num1 > num2 and num1 > num3:
    print(f"The first number, {num1}, is the largest.")
elif num2 > num1 and num2 > num3:
    print(f"The second number, {num2}, is the largest.")
elif num3 > num2 and num3 > num1:
    print(f"The third number, {num3}, is the largest.")
else:
    pass

#Task 2
if num1 < num2 and num1 < num3:
    print(f"The first number, {num1}, is the smallest.")
elif num2 < num1 and num2 < num3:
    print(f"The second number, {num2}, is the smallest.")
elif num3 < num2 and num3 < num1:
    print(f"The third number, {num3}, is the smallest.")

#Task 3
if num1 == num2 and num1 == num3:
    print("All numbers are equal.")
elif num1 == num2 and num1 > num3:
    print("The first and second numbers are equal and largest.")
elif num1 == num3 and num1 > num2:
    print("The first and third numbers are equal and largest.")
elif num2 == num3 and num2 > num1:
    print("The second and third numbers are equal and largest.")
elif num1 == num2 and num1 > num3:
    print("The first and second numbers are equal.")
elif num1 == num3 and num1 > num2:
    print("The first and third numbers are equal.")
elif num2 == num3 and num2 > num1:
    print("The second and third numbers are equal.")
else: 
    pass


