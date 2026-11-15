def task1():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


def task2():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    if a >= b and a >= c:
        print("Largest number:", a)
    elif b >= a and b >= c:
        print("Largest number:", b)
    else:
        print("Largest number:", c)


def task3():
    number = int(input("Enter a number: "))
    if number < 2:
        print("Not a prime number")
    else:
        prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                prime = False
                break
        if prime:
            print("Prime number")
        else:
            print("Not a prime number")


def task4():
    terms = int(input("Enter number of terms: "))
    a, b = 0, 1
    for i in range(terms):
        print(a, end=" ")
        a, b = b, a + b
    print()


def task5():
    number = int(input("Enter a number: "))
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print("Factorial:", factorial)


def task6():
    text = input("Enter a string: ")
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    print("Reversed string:", reversed_text)


def task7():
    text = input("Enter a string: ")
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")


def task8():
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


def task9():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    total = 0
    for number in numbers:
        total += number
    print("Sum:", total)


def task10():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    if numbers:
        largest = numbers[0]
        smallest = numbers[0]
        for number in numbers:
            if number > largest:
                largest = number
            if number < smallest:
                smallest = number
        print("Largest:", largest)
        print("Smallest:", smallest)
    else:
        print("List is empty")


def task11():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    result = []
    for number in numbers:
        if number not in result:
            result.append(number)
    print("List without duplicates:", result)


def task12():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    print(frequency)


def task13():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
    if len(unique_numbers) >= 2:
        largest = unique_numbers[0]
        second_largest = None
        for number in unique_numbers[1:]:
            if number > largest:
                second_largest = largest
                largest = number
            elif second_largest is None or number > second_largest:
                second_largest = number
        print("Second largest:", second_largest)
    else:
        print("Second largest number does not exist")


def task14():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    for i in range(len(numbers)):
        for j in range(0, len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    print("Sorted list:", numbers)


def task15():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    print("Even numbers:", even_numbers)


def task16():
    text = input("Enter a string: ")
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    print(frequency)


def task17():
    first = input("Enter first string: ").lower()
    second = input("Enter second string: ").lower()
    first = first.replace(" ", "")
    second = second.replace(" ", "")
    if sorted(first) == sorted(second):
        print("The strings are anagrams")
    else:
        print("The strings are not anagrams")


def task18():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    duplicates = []
    for number in numbers:
        if numbers.count(number) > 1 and number not in duplicates:
            duplicates.append(number)
    print("Duplicate values:", duplicates)


def task19():
    words = input("Enter a sentence: ").split()
    if words:
        longest = words[0]
        for word in words:
            if len(word) > len(longest):
                longest = word
        print("Longest word:", longest)
    else:
        print("No words entered")


def task20():
    marks = []
    for i in range(1, 6):
        mark = float(input("Enter marks for subject " + str(i) + ": "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / 5

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "F"

    print("Total marks:", total)
    print("Percentage:", percentage, "%")
    print("Grade:", grade)

    if all(mark >= 40 for mark in marks):
        print("Result: Passed")
    else:
        print("Result: Failed")


tasks = {
    1: task1, 2: task2, 3: task3, 4: task4, 5: task5,
    6: task6, 7: task7, 8: task8, 9: task9, 10: task10,
    11: task11, 12: task12, 13: task13, 14: task14, 15: task15,
    16: task16, 17: task17, 18: task18, 19: task19, 20: task20
}

print("Python Practice Assignment")
print("Enter a question number from 1 to 20, or 0 to exit.")

while True:
    choice = input("\nEnter question number: ")
    if choice == "0":
        print("Program ended")
        break
    if choice.isdigit() and int(choice) in tasks:
        tasks[int(choice)]()
    else:
        print("Please enter a number between 1 and 20")
