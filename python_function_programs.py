# 1. Even or Odd Function
def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(is_even(8))
print(is_even(7))
# 2. Largest of Two Numbers
def largest(a, b):
    if a > b:
        return a
    else:
        return b
print(largest(12, 25))
# 3. Print Numbers
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)
print_numbers(5)
# 4. Sum of Numbers
def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total
print(sum_n(5))
# 5. Multiplication Table
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
table(3)
# 6. Count Even Numbers
def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count = count + 1
    return count
1
print(count_even([1, 2, 3, 4, 6]))
# 7. Find Maximum
def find_maximum(numbers):
    if len(numbers) == 0:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
print(find_maximum([12, 45, 7, 89, 23]))
# 11. FizzBuzz
def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
fizz_buzz()
# 12. Palindrome Checker
def is_palindrome(text):
    text = text.lower()
    if text == text[::-1]:
        return True
    else:
        return False
print(is_palindrome("madam"))
print(is_palindrome("python"))
# 13. Count Vowels
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count = count + 1
    return count
print(count_vowels("Education"))
# 14. Second Largest Number
2
def second_largest(numbers):
    largest = None
    second = None
    for num in numbers:
        if largest is None or num > largest:
            second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num
    return second
print(second_largest([10, 5, 20, 8, 20]))
# 15. Guessing Game
import random
def guessing_game():
    secret_number = random.randint(1, 10)
    guess = 0
    while guess != secret_number:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Correct! You guessed the number.")
guessing_game()
# Grade Function
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
print(grade(95))
print(grade(85))
print(grade(75))
print(grade(65))
print(grade(40))
3