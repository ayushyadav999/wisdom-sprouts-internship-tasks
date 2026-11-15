def task1():
    values = [10, "hello", 3.5, True, [1, 2], (4, 5), {1, 2}]
    for value in values:
        print(value, ":", type(value).__name__)


def task2():
    numbers = [[1, 2], [3, 4], [5, 6]]
    result = tuple(tuple(row) for row in numbers)
    print(result)


def task3():
    values = [1, "apple", 2, "apple", 1, 3, "banana", 2]
    result = []
    for value in values:
        if value not in result:
            result.append(value)
    print(result)


def task4():
    number = int(input("Enter a number: "))
    if number > 0 and (number & (number - 1)) == 0:
        print("Power of 2")
    else:
        print("Not a power of 2")


def task5():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("After swapping:", a, b)


def task6():
    number = int(input("Enter a number: "))
    if number % 4 == 0 and number % 6 == 0:
        print("Divisible by both 4 and 6")
    else:
        print("Not divisible by both 4 and 6")


def task7():
    units = int(input("Enter electricity units: "))
    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = 100 * 3 + (units - 100) * 5
    else:
        bill = 100 * 3 + 100 * 5 + (units - 200) * 7
    print("Electricity bill: Rs.", bill)


def task8():
    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))
    c = float(input("Enter third side: "))
    if a + b > c and a + c > b and b + c > a:
        print("These sides can form a triangle")
    else:
        print("These sides cannot form a triangle")


def task9():
    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))
    c = float(input("Enter third side: "))
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("Equilateral triangle")
        elif a == b or b == c or a == c:
            print("Isosceles triangle")
        else:
            print("Scalene triangle")
    else:
        print("Invalid triangle")


def task10():
    balance = 5000
    while True:
        print("\n1. Withdraw\n2. Deposit\n3. Balance\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            amount = float(input("Enter amount to withdraw: "))
            if 0 < amount <= balance:
                balance -= amount
                print("Please collect your cash")
            else:
                print("Invalid amount or insufficient balance")
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print("Amount deposited")
            else:
                print("Enter a valid amount")
        elif choice == "3":
            print("Balance:", balance)
        elif choice == "4":
            break
        else:
            print("Invalid choice")


def task11():
    income = float(input("Enter annual income: "))
    tax = 0
    if income > 1000000:
        tax += (income - 1000000) * 0.30
        income = 1000000
    if income > 500000:
        tax += (income - 500000) * 0.20
        income = 500000
    if income > 250000:
        tax += (income - 250000) * 0.05
    print("Calculated tax:", tax)


def task12():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
    choice = input("Choose an operation: ")
    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    elif choice == "3":
        print("Result:", a * b)
    elif choice == "4":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid choice")


def task13():
    n = int(input("Enter the limit: "))
    for number in range(2, n + 1):
        prime = True
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                prime = False
                break
        if prime:
            print(number, end=" ")
    print()


def task14():
    number = int(input("Enter a number: "))
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print("Factorial:", factorial)


def task15():
    terms = int(input("Enter number of terms: "))
    a, b = 0, 1
    for i in range(terms):
        print(a, end=" ")
        a, b = b, a + b
    print()


def task16():
    number = int(input("Enter a number: "))
    digits = str(abs(number))
    total = sum(int(digit) ** len(digits) for digit in digits)
    if number >= 0 and total == number:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")


def task17():
    number = int(input("Enter a number: "))
    reversed_number = int(str(abs(number))[::-1])
    if number < 0:
        reversed_number = -reversed_number
    print("Reversed number:", reversed_number)
    if number == reversed_number:
        print("Palindrome number")
    else:
        print("Not a palindrome number")


def task18():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    x, y = abs(a), abs(b)
    while y:
        x, y = y, x % y
    print("GCD:", x)


def task19():
    text = input("Enter a string: ")
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")


def task20():
    text = input("Enter a string: ").lower()
    vowels = 0
    consonants = 0
    for char in text:
        if char.isalpha():
            if char in "aeiou":
                vowels += 1
            else:
                consonants += 1
    print("Vowels:", vowels)
    print("Consonants:", consonants)


def task21():
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual rate (%): "))
    time = float(input("Enter time in years: "))
    simple_interest = principal * rate * time / 100
    compound_amount = principal * (1 + rate / 100) ** time
    compound_interest = compound_amount - principal
    print("Simple interest:", simple_interest)
    print("Compound interest:", compound_interest)


def task22():
    number = int(input("Enter a number: "))
    factors = []
    for i in range(1, abs(number) + 1):
        if number % i == 0:
            factors.append(i)
    print("Factors:", factors)


def task23():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    unique_numbers = sorted(set(numbers), reverse=True)
    if len(unique_numbers) >= 2:
        print("Second largest:", unique_numbers[1])
    else:
        print("Second largest number does not exist")


def task24():
    first = list(map(int, input("Enter first list: ").split()))
    second = list(map(int, input("Enter second list: ").split()))
    result = list(dict.fromkeys(first + second))
    print(result)


def task25():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    unique_numbers = sorted(set(numbers))
    if len(unique_numbers) >= 2:
        print("Second smallest:", unique_numbers[1])
        print("Second largest:", unique_numbers[-2])
    else:
        print("Not enough different numbers")


def task26():
    numbers = input("Enter list elements separated by spaces: ").split()
    k = int(input("Enter rotation count: "))
    if numbers:
        k = k % len(numbers)
        numbers = numbers[k:] + numbers[:k]
    print(numbers)


def task27():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    even = [number for number in numbers if number % 2 == 0]
    odd = [number for number in numbers if number % 2 != 0]
    print("Even numbers:", even)
    print("Odd numbers:", odd)


def task28():
    first = input("Enter first list elements: ").split()
    second = input("Enter second list elements: ").split()
    common = []
    for item in first:
        if item in second and item not in common:
            common.append(item)
    print("Common elements:", common)


def task29():
    values = tuple(input("Enter tuple elements separated by spaces: ").split())
    for value in set(values):
        print(value, ":", values.count(value))


def task30():
    first = set(map(int, input("Enter first set: ").split()))
    second = set(map(int, input("Enter second set: ").split()))
    print("Union:", first | second)
    print("Intersection:", first & second)
    print("Difference:", first - second)


def task31():
    first = set(map(int, input("Enter the first set: ").split()))
    second = set(map(int, input("Enter the second set: ").split()))
    if first.issubset(second):
        print("First set is a subset of second set")
    else:
        print("First set is not a subset of second set")


def task32():
    sentence = input("Enter a sentence: ").lower()
    words = sentence.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    print(frequency)


def task33():
    keys = input("Enter keys separated by spaces: ").split()
    values = input("Enter values separated by spaces: ").split()
    result = dict(zip(keys, values))
    print(result)


def task34():
    data = {"apple": 5, "banana": 2, "mango": 8, "orange": 3}
    sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))
    print(sorted_data)


def task35():
    filename = input("Enter file name: ")
    try:
        with open(filename, "r") as file:
            content = file.read()
        print("Lines:", len(content.splitlines()))
        print("Words:", len(content.split()))
        print("Characters:", len(content))
    except FileNotFoundError:
        print("File not found")


def task36():
    source = input("Enter source file name: ")
    destination = input("Enter destination file name: ")
    try:
        with open(source, "r") as file:
            lines = file.readlines()
        with open(destination, "w") as file:
            for number, line in enumerate(lines, start=1):
                if number % 2 == 0:
                    file.write(line)
        print("Even-numbered lines copied")
    except FileNotFoundError:
        print("Source file not found")


def task37():
    try:
        number = int(input("Enter an integer: "))
        print("You entered:", number)
    except ValueError:
        print("Invalid input. Please enter an integer.")


def task38():
    filename = input("Enter file name: ")
    try:
        with open(filename, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found")


def task39():
    import random
    import string

    length = int(input("Enter password length: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    print("Generated password:", password)


def task40():
    from datetime import datetime

    first_date = input("Enter first date (YYYY-MM-DD): ")
    second_date = input("Enter second date (YYYY-MM-DD): ")
    date1 = datetime.strptime(first_date, "%Y-%m-%d")
    date2 = datetime.strptime(second_date, "%Y-%m-%d")
    print("Number of days:", abs((date2 - date1).days))


tasks = {
    1: task1, 2: task2, 3: task3, 4: task4, 5: task5,
    6: task6, 7: task7, 8: task8, 9: task9, 10: task10,
    11: task11, 12: task12, 13: task13, 14: task14, 15: task15,
    16: task16, 17: task17, 18: task18, 19: task19, 20: task20,
    21: task21, 22: task22, 23: task23, 24: task24, 25: task25,
    26: task26, 27: task27, 28: task28, 29: task29, 30: task30,
    31: task31, 32: task32, 33: task33, 34: task34, 35: task35,
    36: task36, 37: task37, 38: task38, 39: task39, 40: task40
}

print("Python Mixed Practice Assignment")
print("Enter a question number from 1 to 40, or 0 to exit.")

while True:
    choice = input("\nEnter question number: ")
    if choice == "0":
        print("Program ended")
        break
    if choice.isdigit() and int(choice) in tasks:
        tasks[int(choice)]()
    else:
        print("Please enter a number between 1 and 40")
