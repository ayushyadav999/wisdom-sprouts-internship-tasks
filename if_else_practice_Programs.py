#1. Check positive, negative or zero
'''
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
'''

# Check even or odd
'''
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
'''

# Find greater of two numbers
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Greater number is", a)
elif b > a:
    print("Greater number is", b)
else:
    print("Both numbers are equal")
'''

# Find greatest of three numbers
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Greatest number is", a)
elif b >= a and b >= c:
    print("Greatest number is", b)
else:
    print("Greatest number is", c)

# Check voting eligibility

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
'''
# Check leap year
'''
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
'''

# Check vowel or consonant
'''
ch = input("Enter an alphabet: ").lower()

if len(ch) != 1 or not ch.isalpha():
    print("Please enter one alphabet")
elif ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")
'''

# Check divisibility by 5 and 11
'''
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")
'''

# Check multiple of 3 and 7
'''
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print("Multiple of both 3 and 7")
else:
    print("Not a multiple of both 3 and 7")
'''

# Assign grade based on marks
'''
marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")
'''
# Check uppercase or lowercase
'''
ch = input("Enter an alphabet: ")

if len(ch) != 1 or not ch.isalpha():
    print("Please enter one alphabet")
elif ch.isupper():
    print("Uppercase letter")
else:
    print("Lowercase letter")
'''

# Check vowel using if-elif

ch = input("Enter an alphabet: ").lower()
'''
if len(ch) != 1 or not ch.isalpha():
    print("Please enter one alphabet")
elif ch == 'a':
    print("Vowel")
elif ch == 'e':
    print("Vowel")
elif ch == 'i':
    print("Vowel")
elif ch == 'o':
    print("Vowel")
elif ch == 'u':
    print("Vowel")
else:
    print("Consonant")
'''

# Check whether sides form a triangle
'''
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("Triangle can be formed")
else:
    print("Triangle cannot be formed")
'''

# Find the type of triangle
'''
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")
elif a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
'''

# Find largest of four numbers
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    print("Largest number is", a)
elif b >= a and b >= c and b >= d:
    print("Largest number is", b)
elif c >= a and c >= b and c >= d:
    print("Largest number is", c)
else:
    print("Largest number is", d)
'''

# Check three-digit number
'''
num = int(input("Enter a number: "))

if 100 <= abs(num) <= 999:
    print("Three-digit number")
else:
    print("Not a three-digit number")
'''

# Calculate electricity bill
'''
units = float(input("Enter units consumed: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 1.50
    print("Electricity bill:", bill)
elif units <= 200:
    bill = 100 * 1.50 + (units - 100) * 2.50
    print("Electricity bill:", bill)
elif units <= 500:
    bill = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4
    print("Electricity bill:", bill)
else:
    bill = 100 * 1.50 + 100 * 2.50 + 300 * 4 + (units - 500) * 6
    print("Electricity bill:", bill)
'''

# Calculate income tax using example slabs
'''
income = float(input("Enter annual taxable income: "))

if income < 0:
    print("Invalid income")
elif income <= 300000:
    tax = 0
    print("Income tax:", tax)
elif income <= 600000:
    tax = (income - 300000) * 0.05
    print("Income tax:", tax)
elif income <= 900000:
    tax = 15000 + (income - 600000) * 0.10
    print("Income tax:", tax)
elif income <= 1200000:
    tax = 45000 + (income - 900000) * 0.15
    print("Income tax:", tax)
else:
    tax = 90000 + (income - 1200000) * 0.20
    print("Income tax:", tax)
'''

# Check student result
'''
subjects = int(input("Enter number of subjects: "))
passed = True

if subjects <= 0:
    print("Invalid number of subjects")
else:
    for i in range(1, subjects + 1):
        marks = int(input("Enter marks for subject " + str(i) + ": "))

        if marks < 0 or marks > 100:
            print("Invalid marks")
            passed = False
            break
        elif marks < 35:
            passed = False

    if passed:
        print("Student passed")
    else:
        print("Student failed or entered invalid marks")
'''

# Check number within a range
'''
num = int(input("Enter a number: "))
start = int(input("Enter starting value: "))
end = int(input("Enter ending value: "))

if start > end:
    print("Invalid range")
elif start <= num <= end:
    print("Number is within the range")
else:
    print("Number is outside the range")
'''

# Simple calculator using if-elif-else
'''
a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/':
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", a / b)
else:
    print("Invalid operator")
'''

# Check century leap year
'''
year = int(input("Enter a year: "))

if year <= 0:
    print("Invalid year")
elif year % 100 == 0 and year % 400 == 0:
    print("Century leap year")
elif year % 100 == 0:
    print("Century year but not a leap year")
elif year % 4 == 0:
    print("Leap year but not a century year")
else:
    print("Not a leap year")
'''

# Find season using month number
'''
month = int(input("Enter month number (1-12): "))

if month == 12 or month == 1 or month == 2:
    print("Winter")
elif month >= 3 and month <= 5:
    print("Summer")
elif month >= 6 and month <= 9:
    print("Monsoon")
elif month == 10 or month == 11:
    print("Post-monsoon / Autumn")
else:
    print("Invalid month")
'''

# Find number of days in a month
'''
month = int(input("Enter month number (1-12): "))
year = int(input("Enter year: "))

if month < 1 or month > 12 or year <= 0:
    print("Invalid month or year")
elif month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("29 days")
    else:
        print("28 days")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30 days")
else:
    print("31 days")
'''

# Check password conditions
'''
password = input("Enter a password: ")

if len(password) >= 8 and any(ch.isdigit() for ch in password) and any(ch.isupper() for ch in password) and any(ch.islower() for ch in password) and any(not ch.isalnum() for ch in password):
    print("Password meets all conditions")
else:
    print("Password does not meet all conditions")
    print("Use 8 characters, uppercase, lowercase, a digit and a special character")
'''

# Calculate ticket price based on age
'''
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age < 5:
    print("Ticket price: Rs. 0")
elif age <= 12:
    print("Ticket price: Rs. 100")
elif age <= 59:
    print("Ticket price: Rs. 200")
else:
    print("Ticket price: Rs. 120")
'''

# Calculate discount on purchase
'''
amount = float(input("Enter purchase amount: "))

if amount < 0:
    print("Invalid amount")
elif amount >= 5000:
    discount = amount * 0.20
    print("Discount:", discount)
    print("Final amount:", amount - discount)
elif amount >= 3000:
    discount = amount * 0.15
    print("Discount:", discount)
    print("Final amount:", amount - discount)
elif amount >= 1000:
    discount = amount * 0.10
    print("Discount:", discount)
    print("Final amount:", amount - discount)
else:
    print("No discount")
    print("Final amount:", amount)
'''

# Check basic driving licence conditions
'''
age = int(input("Enter your age: "))
eyesight = input("Do you meet the required eyesight standard? (yes/no): ").lower()

if age < 0:
    print("Invalid age")
elif eyesight != "yes" and eyesight != "no":
    print("Please enter yes or no")
elif age >= 18 and eyesight == "yes":
    print("You meet the basic practice conditions")
else:
    print("You do not meet the basic practice conditions")
'''

# Simple login system
'''
username = input("Enter username: ")
password = input("Enter password: ")

if username == "student" and password == "Python@123":
    print("Login successful")
else:
    print("Invalid username or password")
'''

# Menu-driven calculator
'''
while True:
    print("\n--- Calculator Menu ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Exiting calculator")
        break

    elif choice == "1" or choice == "2" or choice == "3" or choice == "4":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", a + b)
        elif choice == "2":
            print("Result:", a - b)
        elif choice == "3":
            print("Result:", a * b)
        elif choice == "4":
            if b == 0:
                print("Cannot divide by zero")
            else:
                print("Result:", a / b)
    else:
        print("Invalid choice")
'''