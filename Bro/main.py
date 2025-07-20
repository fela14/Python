import math
import time
import random
import string
from PyQt5 import QtWidgets
from enum import nonmember
from test.test_codeccallbacks import PosReturn
from abc import ABC, abstractmethod
import os
import json
import csv
import datetime
#import pygame
import threading
import requests
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout,
                             QGridLayout, QPushButton, QCheckBox,
                             QRadioButton, QButtonGroup, QLineEdit)
from PyQt5.QtGui import QIcon, QFont, QPixmap, QFont, QFontDatabase
from PyQt5.QtCore import Qt,QTimer, QTime

"""
#x = 25.9
#print(math.pi)
#print(math.e)
#result = math.sqrt(x)
#result = math.ceil(x)
#result = math.floor(x)


radius = float(input("What is the radius of the circle?: "))
circumference = 2 * math.pi * radius
circumference = round(circumference)

print(f"The circumference of the circle is {circumference}cm")

radius = float(input("Enter the radius of a circle?: "))
area = math.pi * pow(radius, 2)
area = round(area, 2)
print(f"The radius of the circle is {area}")

a = float(input("Enter side A?: "))
b = float(input("Enter side B?: "))
c = round(math.sqrt(pow(a, 2) + pow(b, 2)), 2)

print(f"The hypothenus of the right angle triangle is {c}")


age = int(input("Enter your age?: "))

if age>=100:
    print("You are too old to sign up!")
elif age >= 18:
    print("You are signed up!")
elif age < 0:
    print("You havent been born yet!")
else:
    print("You must be 18+ to sign up!")


name = input("Enter your name?:")
if name == "":
    print("You did not enter your name")
else:
    print(f"Hello {name}")

response = input("Would you like some food? (Y/N)?: ")
if response == "Y":
    print("Have some food!")
elif response == "N":
    print("No food for you!")
else: print("You entered a wrong response!")

online = True
if online:
    print("This user is online")
else:
    print("This user is offline")

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(round((num1 * num2), 3))
elif operator == "/":
    print(round((num1 / num2), 3))
else:
    print(f"{operator} is not a valid operator")

weight = float(input("Enter your weight: "))
unit = input("Pounds or kilograms? (K / l): ")

if unit == "K":
    weight = weight * 2.205
    unit = "lbs"
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "l":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} is not valid")

unit = input("Is this temperature in Celsius or Fahrenheit (C/F):")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((temp * 9 / 5 + 32, 1))
    print(f"The temperature in Fahrenheit is: {temp}F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}C")
else:
    print(f"{unit} is an invalid unit of measurement")

temp = 20
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

temp = 20
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is sunny")
elif temp <= 0 and is_sunny:
    print("It is COlD outside")
    print("It is sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("it is sunny")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside")
    print("It is cloudy")
elif temp <= 0 and not is_sunny:
    print("It is COlD outside")
    print("It is cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside")
    print("it is cloudy")

num = -1
print("Positive" if num > 0 else "Negative")

num = 9
result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

a = 2
b = -8
min_num = a if a<b else b
print(min_num)

age = 27
status = "Adult" if age>18 else "Minor"
print(status)

temp = 79
weather = "HOT" if temp > 20 else "COlD"
print(weather)

user_role = "marketing"
access_level = "FUll ACCESS" if user_role == "admin" else "lIMITED ACCESS"
print(access_level)

name = input("What is your name: ")
result = len(name)
result1 = name.find("b")
result2 = name.rfind("b")

print(result1)
print(result2)

name = input("what is your favorite food: ")
result1 = name.capitalize()
result2 = name.upper()
result3 = name.lower()
result4 = name.isdigit()
result5 = name.isalpha()

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)

phone = input("Enter your phone #:")
result1 = phone.count("")
result2 = phone.replace("7","4")
print(result1)
print(result2)

username = input("Enter your username: ")
result1 = len(username)
result2 = username.find(" ")
result3 = username.isalpha()
if result1 > 12:
    print("Your username can't be more than 12 characters")
elif result2 != -1:
    print("Your username must not contain spaces")
elif not result3:
    print("Your username must not contain any digits")
else:
    print(f"welcome {username}")

credit_num = "1234-5678-9012-3456"
last_digits = credit_num[-4]
print(credit_num[4])
print(credit_num[:8])
print(credit_num[5:9])
print(credit_num[10:-2])
print(credit_num[-3])
print(credit_num[::3])
print(credit_num[::-2])
print(credit_num[15::])
print(credit_num[5:9])
print(f"XXXX-XXXX-XXXX-{credit_num[-4:]}")
print(credit_num[::-1])

price1 = -11.77722
price2 = 22.44097
price3 = 12.33258
price4 = -1200000000000.7654

print(f"Price1 is {price1:.2f}")
print(f"Price2 is {price2:.4f}")
print(f"Price3 is {price3:.3f}")
print(f"Price1 is {price1:10}")
print(f"Price2 is {price2:010}")
print(f"Price3 is {price3:<15}")
print(f"Price1 is {price1:>15}")
print(f"Price2 is {price2:^15}")
print(f"Price3 is {price3:+}")
print(f"Price4 is {price4:,}")
print(f"Price4 is {price4:+,.2f}")

name = input("Enter your name: ")
while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")

food = input("Enter a food you like (q to quit): ")
while food != "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")
print("bye")

num = int(input("Enter a number between 1 and 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 and 10: "))
print(f"Your number is {num}")

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero")
    else:
        break
while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest can't be less than zero")
    else:
        break
while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than zero")
    else:
        break
total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s = ${total:.2f}")

for x in range(1, 11):
    print(x)
print("HAPPY NEW YEAR!")

for x in reversed(range(1, 11, 3)):
    print(x)
    
credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)
    
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)

time.sleep(3)
print("Time's up!")

my_time = int(input("Enter the time in seconds: "))
for x in range (my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hour = int(x / 3600)
    print(f"{hour:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time is up")

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of column: "))
symbol = input("Enter the symbol to use: ")


for x in range(rows):
    for y in range (columns):
        print(symbol, end="")
    print()

fruits = ["apple", "banana", "coconut", "orange", "pawpaw"]

print(fruits[0])
print(fruits[0:1])
print(fruits[::2])
print(fruits[::-1])
for x in fruits:
    print(x)
print(help(fruits))
print(len(fruits))
print("apple" in fruits)
fruits.append("pineapple")
fruits.remove("apple")
fruits.insert(0, "pawpaw")
fruits.sort()
fruits.reverse()
fruits.clear()
print(fruits.index("pawpaw"))
print(fruits.count("pawpaw"))
print(fruits)

fruits = {"apple", "orange", "banana", "coconut", "banana"}
fruits.add("pineapple")
fruits.remove("apple")
fruits.pop()
fruits.clear()
print(fruits)

fruits = ("apple", "orange", "banana", "coconut", "banana")
for x in fruits:
    print(fruits)
print("apple" in fruits)
print(fruits.index("apple"))
print(fruits.count("banana"))
print(len(fruits))

foods = []
prices = []
total = 0

while True:
    food = (input("Enter a food to buy (q to quit): "))
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food in foods:
    print(food, end = " ")

for price in prices:
    total += price

print()
print(f"TOTAL = ${total}")

fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrot", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

fruits[0] = "pineapple"
fruits.insert(0, "tangerine")
print(fruits[::-2])
print(fruits)
print(vegetables)
print(meats)
print(groceries)
print(groceries[0])
print(groceries[1])
print(groceries[2])
print(groceries[0][2])
print(groceries[1][2])
print(groceries[2][2])

groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrot", "potatoes"],
             ["chicken", "fish", "turkey"]]
print(groceries)
print(groceries[0])
print(groceries[1])
print(groceries[2])
print(groceries[0][0])

for x in fruits:
    print(x)

for collection in groceries:
    for food in collection:
        print(food, end = " ")
    print()

num_pad =  ((1,2,3),
            (4,5,6),
            (7,8,9),
            ("*", "0", "#"))
for row in num_pad:
    for num in row:
        print(num, end = " ")
    print()

questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "WHat is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C","D","A","A","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print()
print("-------------------------------")
print("             RESUlTS           ")
print("-------------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = score / len(questions) * 100
print(f"Your score is: {score}%")

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals.get("India"))
print(capitals.get("USA"))
print(capitals.get("China"))
print(capitals.get("Russia"))
print(capitals.get("Japan"))

if capitals.get("Japan"):
    print("This capital exists")
else:
    print("This capital doesn't exist")

if capitals.get("Russia"):
    print("This capital exists")
else:
    print("This capital doesn't exist")

capitals.update({"Germany": "Berlin"})
print(capitals)
capitals.update({"USA": "Detroit"})
print(capitals)
capitals.pop("China")
print(capitals)
capitals.popitem()
print(capitals)
#capitals.clear()
#print(capitals)
keys = capitals.keys()
print(keys)
for key in capitals.keys():
    print(key)
values = capitals.values()
print(values)
for value in capitals.values():
    print(value)
items = capitals.items()
print(items)
for item in capitals.items():
    print(item)
for key, value in capitals.items():
    print(f"{key}: {value}")

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}
cart = []
total = 0

print("--------MENU---------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("---------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print()
print("--------YOUR ORDER--------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(f"Total is ${total:.2f}")

number = random.randint(1, 20)
print(number)
low = 1
high = 100
number = random.randint(low, high)
print(number)
number = random.random()
print(number)

options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)

cards = ["2","3","4","5","6","7","8","9","J","Q","K","A"]
random.shuffle(cards)
print(cards)

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("PYTHON NUMBER GUESSING GAME")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False

    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)
running = True


while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    else:
        print("You lose!")

    if not input("Would you like to play again (y/n): ").lower() == "y":
        running = False


print("Thanks for playing!")

print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
#● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),

    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")

}

dice = []
total = 0
num_of_dice = int(input("How many dice? "))


for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

#for die in range(num_of_dice):
    #for line in dice_art.get(dice[die]):
        #print(line)
        
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end= "")
    print()


for die in dice:
    total += die
print(f"total: {total}")

def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old")
    print("Happy birthday to you!")
    print()

happy_birthday("Bro", 20)
happy_birthday("Ola", 34)
happy_birthday("Shayo", 45)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due on {due_date}")

display_invoice("Chloe", 20, "10/January/2025")
display_invoice("Martin", 10.006, "10/February/2025")
display_invoice("Etta", 34550, "10/June/2025")
display_invoice("Joy", 660, "10/September/2025")

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1,2))
print(subtract(3,7))
print(divide(18, 2))
print(multiply(5, 6))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name1 = create_name("martin", "hale")
full_name2 = create_name("etta", "caroll")

print(full_name1)
print(full_name2)

def net_price (list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 0.1, 0))

def timer(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE")

timer(0, 10)

def timer(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE")

timer(10)
timer(5, 1)

def hello(greeting, title, first, last):
    print(f"{greeting} {title}. {first} {last}")

hello("Hello", "Mr", "Spongebob", "Squarepants")
hello("Hi", last = "Hale", title = "Dr", first = "Martin")

for x in range(1, 11):
    print(x, end=" ", sep = "-")
print()
print("1", "2", "3", "4", "5", sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"
phone_num = get_phone(last = 890, first = 567, area = 234, country = +1)
print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1, 2, 7))

def display_name(*args):
    for arg in args:
        print(arg, end = " ")
display_name("Dr", "Spongebob", "Harold", "Squarepants")

def print_address(**kwargs):
    #print(type(kwargs))
    for value in kwargs.values():
        print(value)
    for key in kwargs.keys():
        print(key)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(country = "USA",
              state = "CA",
              city = "SAN DIEGO",
              street = "123, FAKE STR.",
              apt = "100",
              zip = "12345")

def shopping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print()
    #for value in kwargs.values():
        #print(value, end = " ")
    if 'apt' in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif 'pobox' in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")


    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shopping_label("Dr", "Martin", "Hale", "III",
               country = "UK",
               state = "Southampton",
               city = "Sarisbury Green",
               street = "Fake Str.",
               pobox = "PO box #10001",
               zip = "XYZ56")

numbers = [1,2,3,4,5]
for number in numbers:
    print(number)
for number in reversed(numbers):
    print(number, end = " - ")
print()
numbers = (1,2,3,4,5)
for number in numbers:
    print(number)

fruits = {"apple", "orange", "banana", "coconut"}
for fruit in (fruits):
    print(fruit)

name = "Martin Hale"
for character in name:
    print(character, end = " ")
print()

my_dictionary = {"A": 1, "B": 2, "C": 3}
for key in my_dictionary:
    print(key)

for value in my_dictionary.values():
    print(value)
for key, value in my_dictionary.items():
    print(key, value)
    print(f"{key} = {value}")

word = "APPLE"
letter = input("Guess a letter in the secret word? ").upper()

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")

letter = input("Guess a letter in the secret word? ").upper()

students = {"Spongebob", "Patrick", "Sandy"}
student = input("Enter the name of a student: ").capitalize()
if student not in students:
    print(f"{student} was not found")
else:
    print(f"{student} is a student")

grades = {"Sandy": "A",
          "Squidward": "B",
          "Spongebob": "C",
          "Patrick": "D"}
student = input("Enter the name of a student: ")

if student in grades:
    print(f"Student's grade is {grades[student]}")
else:
    print(f"{student} was not found")

email = "martinhale@fake.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")

doubles = []
for x in range(1, 11):
    doubles.append(x * 2)
print(doubles)

fruits = ["apples", "orange", "banana", "coconut"]
doubles = [x * 2 for x in range (1, 11)]
triples = [x * 3 for x in range (1, 11)]
squares = [x * x for x in range (1, 11)]
fruits = [fruit.upper() for fruit in fruits]
fruits = [fruit[0] for fruit in fruits]
print(doubles)
print(triples)
print(squares)
print(fruits)

numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]
print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)

def day_of_week(day):
    if day == 1:
        return "It is Sunday"
    elif day == 2:
        return "It is Monday"
    elif day == 3:
        return "It is Tuesday"
    elif day == 4:
        return "It is Wednesday"
    elif day == 5:
        return "It is Thursday"
    elif day == 6:
        return "It is Friday"
    elif day == 7:
        return "It is Saturday"
    else:
        return "Not a valid day"
        
print(day_of_week("pizza"))

def day_of_week(day):
    match day:
        case "Sunday":
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:
            return "Not a valid day"
print(day_of_week(3))
print(day_of_week("pizza"))

def is_weekend(day):
    match day:
        case "Sunday":
            return True
        case "Monday":
            return False
        case "Tuesday":
            return False
        case "Wednesday":
            return False
        case "Thursday":
            return False
        case "Friday":
            return False
        case "Saturday":
            return True
        case _:
            return False
print(is_weekend("Saturday"))

def is_running(day):
    match day:
        case "Saturday"|"Sunday":
            return True
        case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
            return False
        case _:
            return False
print(is_running("Friday"))

import math as m
from math import pi
from math import e
print(pi)
print(e)

import math
a,b,c,d, e = 1,2,3,4,5
print( math.e ** a)
print( e ** b)
print( e ** c)
print( e ** d)
print( e ** e)

import example

result = example.pi
result = example.square(3)
result = example.cube(4)
result = example.circumference(4)
result = example.area(4)

def func1():
    a = 1
    print(a)
def func2():
    b = 2
    print(b)
def func3():
    b = 3
    print(b)
def func4():
    x = 1
    print(x)
def func5():
    print(x)
x = 3

func1()
func2()
func3()
func4()
func5()

from math import e
def func6():
    print(e)
e = 3
func6()

def show_balance(balance):
    print("***********************8")
    print(f"Your balance is ${balance:.2f}")
    print("***********************8")

def deposit():
    print("***********************8")
    amount = float(input("Enter an amount to be deposited: "))
    print("***********************8")

    if amount < 0:
        print("***********************8")
        print("That's not a valid amount")
        print("***********************8")
        return 0
    else:
        return amount
def withdraw(balance):
    print("***********************8")
    amount = float(input("Enter amount to be withdrawn"))
    print("***********************8")

    if amount > balance:
        print("***********************8")
        print("Insufficient funds")
        print("***********************8")
        return 0
    elif amount< 0:
        print("***********************8")
        print("Amount must be greater than 0")
        print("***********************8")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("***********************8")
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdrawal")
        print("4. Exit")
        print("***********************8")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)

        elif choice == '2':
            balance += deposit()

        elif choice == '3':
            balance -= withdraw(balance)

        elif choice == '4':
            is_running = False

        else:
            print("***********************8")
            print("That is not a valid choice")
            print("***********************8")

    print("***********************8")
    print("Thank you for banking with us!")
    print("***********************8")


if __name__ == '__main__':
    main()

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
    print("***************")
    print(" | ".join(row))
    print("***************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0

def main():
    balance = 100

    print("***********************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("************************")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount: $")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insuffucient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if play_again != "Y":
            break

    print("*******************************************")
    print(f"Game over! Your final balance is {balance}")
    print("*******************************************")

if __name__ == '__main__':
    main()

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"keys: {key}")

#ENCRYPT

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

#ENCRYPT

cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted message: {cipher_text}")
print(f"original message: {plain_text}")

#Hangman in Python

from wordslist import words

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o  ",
                   "/|\\",
                   "   "),
               5: (" o  ",
                   "/|\\",
                   "/   "),
               6: (" o  ",
                   "/|\\",
                   "/ \\")}

#for line in hangman_art[6]:
    #print(line)

def display_man(wrong_guesses):
    print("*****************************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*****************************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:

        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)


        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN")
            is_running = False

        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False


if __name__ == '__main__':
    main()

from car import Car
from car import Student

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)
print(car1.model)
print(car2.year)
print(car1.colour)
print(car2.for_sale)
print(car3.model)
print(car3.colour)

car1.drive()
car2.stop()
car3.describe()

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Sandra", 29)
student4 = Student("Jay", 4)

print(student1.name)
print(student1.age)
#print(student1.class_year)
#print(student2.class_year)
print(Student.class_year)
print(Student.num_students)
print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

from car import Animal
from car import Dog
from car import Cat
from car import Mouse

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Micky")

print(dog.name)
print(mouse.is_alive)
dog.eat()
cat.sleep()
dog.speak()
cat.speak()
mouse.speak()

from benz import Mercedes
from benz import Animal
from benz import Dog
from benz import Cat
from benz import Mouse

Mercedes1 = Mercedes("E350", 2025, "black", "selling")
Mercedes2 = Mercedes("300D", 1982, "white", "not selling")
Mercedes3 = Mercedes("G-wagon", 2025, "black", "not selling")

Mercedes1.drive()
Mercedes1.park()
Mercedes1.sell()
print()
Mercedes2.drive()
Mercedes2.park()
Mercedes2.sell()
print()
Mercedes3.drive()
Mercedes3.park()
Mercedes1.sell()
print()
print(f"There are a total of {Animal.num} animals in the year {Animal.year}")
print()

dog = Dog("Garfield", "is")
cat = Cat( "Timtim", "is not")
mouse = Mouse("Jearr", "is still")

dog.eating()
dog.sleeping()
dog.alive()
dog.speak()
print()
cat.eating()
cat.sleeping()
cat.alive()
cat.speak()
print()
mouse.eating()
mouse.sleeping()
mouse.alive()
mouse.speak()

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"This {self.name} is eating")

    def sleep(self):
        print(f"This {self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"This {self.name} is fleeing")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Tony")
hawk = Hawk()
fish = Fish("Montana")

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
rabbit.eat()
rabbit.sleep()
fish.eat()
fish.sleep()
rabbit.flee()
fish.flee()

class Shape:
    def __init__(self, colour, is_filled):
        self.colour = colour
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.colour} and {'filled' if self.is_filled == True else 'not filled'}")

class Circle(Shape):
    def __init__(self, colour, is_filled, radius):
        super().__init__(colour, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"It's is a circe with an area of {3.14 * self.radius * self.radius}cm^2")

class Square(Shape):
    def __init__(self, colour, is_filled, width):
        super().__init__(colour, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"It's is a square with an area of {self.width * self.width}cm^2")


class Triangle(Shape):
    def __init__(self, colour, is_filled, width, height):
        super().__init__(colour, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It's is a triangle with an area of {self.width * self.height / 2}cm^2")


circle = Circle("red", True, 5)
square = Square("blue", False, 6)
triangle = Triangle("yellow", True, 7, 8)

print(circle.colour)
print(circle.is_filled)
print(f"{circle.radius}cm")
print(square.colour)
print(square.is_filled)
print(f"{square.width}cm")
print(triangle.colour)
print(triangle.is_filled)
print(f"{triangle.width}cm")
circle.describe()
square.describe()
triangle.describe()

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2

class Pizza(Circle):
    def __init__(self, radius, topping):
        self.topping = topping
        super().__init__(radius)

shapes = [Circle(4), Square(5), Triangle(6,7), Pizza(15, "peperoni")]

for shape in shapes:
    print(f"{shape.area()}cm^2")

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:
    alive = False
    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name}= {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

print(Employee.is_valid_position("Cook"))
print(Employee.is_valid_position("Scientist"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

class Student:

    count = 0
    total = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total += gpa

    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name}: {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total / cls.count:.2f}"

student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.8)
student3 = Student("Sandy", 4.0)

print(student1.get_info())
print(student2.get_info())
print(student3.get_info())
print(Student.get_count())
print(Student.get_average_gpa())

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else:
            return f"Key '{key}' was not found"

book1 = Book("The Hobbit", "J.R.R Tolkein", 310)
book2 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The lion, the Witch and the Wardrobe", "C.S. lewis", 172)
book4 = Book("The Hobbit", "J.R.R Tolkein", 310)

print(book1)
print(book2)
print(book3)
print(book1 == book2)
print(book1 == book4)
print(book2 < book3)
print(book3 < book1)
print(book2 > book3)
print(book3 > book1)
print(book1 + book4)
print("lion" in book3)
print("lion" in book1)
print("Rowling" in book3)
print("Rowling" in book2)
print(book1['title'])
print(book2['author'])
print(book3['num_pages'])
print(book1['audio'])

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("height must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")

rectangle = Rectangle(3,4)
rectangle.width = 5
rectangle.height = 4

print(rectangle._width)
print(rectangle._height)
print(rectangle.width)
print(rectangle.height)

del rectangle.width
del rectangle.height

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You add sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge")
        func(*args, **kwargs)
    return wrapper

@add_fudge
@add_sprinkles
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream")

get_ice_cream("vanilla")

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Enter only numbers please!")
except Exception:
    print("Something went wrong")
finally:
    print("Do some cleanup here")

file_path = "stuff/test.txt"
file_path1 = "C:/Users/KehindeFakeye/Desktop/test.txt"
file_path2 = "C:/Users/KehindeFakeye/Desktop/test"

if os.path.exists(file_path):
    print(f"The location '{file_path2}' exists")
    if os.path.isfile(file_path1):
        print("That is a file")
    elif os.path.isdir(file_path2):
        print("That is a directory")
else:
    print("That location doesn't exist")

txt_data = "I like pizza"
file_path = "output.txt"
file_path1 = "C:/Users/KehindeFakeye/Desktop/output.txt"
with open (file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file {file_path} was created")

with open (file_path1, "w") as file:
    file.write(txt_data)
    print(f"txt file {file_path1} was created")

txt_data4 = "CCNP ENCOR exam"
file_path4 = "C:/Users/KehindeFakeye/Desktop/exam.txt"
try:
    with open (file_path4, "x") as file:
        file.write(txt_data4)
        print(f"txt file '{file_path4}' was created")
except FileExistsError:
    print("file already exists")

with open (file_path4, "a") as file:
    file.write("\n" + txt_data4)
    print(f"txt file '{file_path4}' was created")

employees = ["Eugene", "Squidward", "spongebob", "Patrick"]
file_path = "C:/Users/KehindeFakeye/Desktop/employee.txt"

with open (file_path, "x") as file:
    for employee in employees:
        file.write(employee + "\n" )
    print(f"txt file '{file_path}' was created")

employee = {
    "name": "Bob",
    "age": 45,
    "job": "Manager"

}
file_path = "C:/Users/KehindeFakeye/Desktop/output.json"
with open (file_path, "x") as file:
    json.dump(employee, file, indent = 4)
    print(f"json file '{file_path}' has been created")

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path = "C:/Users/KehindeFakeye/Desktop/file.csv"

try:
    with open (file_path, "w", newline = "") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path} has been created")
except FileExistsError:
    print("That file already exists")

file_path = "C:/Users/KehindeFakeye/Desktop/output.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read this file")

file_path = "C:/Users/KehindeFakeye/Desktop/output.json"

try:
    with open (file_path, "r") as file:
        content = json.load(file)
        print(content["job"])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You don't have permission to read this file")

file_path = "C:/Users/KehindeFakeye/Desktop/citizen.csv"

try:
    with open (file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[2])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You don't have permission to read this file")

date = datetime.date(2025, 1, 2)
today = datetime.date.today()
time = datetime.time(12, 30, 0)
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %m-%d-%y")

target_datetime = datetime.datetime(2020,1,2, 12, 30, 1)
current_datetime = datetime.datetime.now()

print(today)
print(date)
print(time)
print(now)

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "joy_is_coming.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP! 😏")

            is_running = False

        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)

def walk_dog(first, last):
    time.sleep(8)
    print(f"You finish walking the {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("You take out trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

#walk_dog()
#take_out_trash()
#get_mail()

chore1 = threading.Thread(target=walk_dog, args=("Scooby","Doo"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()
print("All chores are complete")
time.sleep(1)

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        pokemon_data = response.json()
        print("Data retrieved")
        #print(pokemon_data)
        return pokemon_data
    else:
        print(f"Failed to retrieve data{response.status_code}")

pokemon_name= "typhlosion"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.setGeometry = (700,500,500,500)
        self.setWindowIcon(QIcon("cisco logo.png"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 20))
        label.setGeometry(0,0,500,100)
        #label.setStyleSheet("color: blue")
        label.setStyleSheet("color: #292929;"
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        #label.setAlignment(Qt.AlignTop)
        #label.setAlignment(Qt.AlignBottom)
        #label.setAlignment(Qt.AlignVCenter) vertically center
        #label.setAlignment(Qt.AlignRight) horizontally right
        #label.setAlignment(Qt.AlignHCenter) horizontally center
        #label.setAlignment(Qt.AlignLeft)
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        label.setAlignment(Qt.AlignCenter)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.setGeometry = (700,500,500,500)
        self.setWindowIcon(QIcon("cisco logo.png"))

        label = QLabel(self)
        label.setGeometry(0,0,250,250)

        pixmap = QPixmap("cisco logo.png")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        label.setGeometry((self.width() - label.width()) // 2,
                          (self.height() - label.height()) // 2,
                          label.width(),
                          label.height())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.setGeometry = (700,500,500,500)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: purple;")

        #vbox = QVBoxLayout()
        #vbox = QHBoxLayout()
        grid = QGridLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)

        central_widget.setLayout(vbox)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 2, 2)

        central_widget.setLayout(grid)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.setGeometry = (700,500,500,500)
        self.button = QPushButton("Click me!", self)
        self.label = QLabel("Hello", self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(150,300,200,100)
        self.label.setStyleSheet("font-size: 50px;")

    def on_click(self):
        print("Button clicked")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)

        self.label.setText("Goodbye")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.setGeometry = (700,500,500,500)
        self.checkbox = QCheckBox("Do you like food?", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(10,0,500,200)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Arial;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("You like food")
        else:
            print("You do not like food")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.setGeometry = (700,500,500,500)
        self.radio1 = QRadioButton("visa", self)
        self.radio2 = QRadioButton("Masetercard", self)
        self.radio3 = QRadioButton("Giftcard", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(0,0,300,50)
        self.radio2.setGeometry(0,50,300,50)
        self.radio3.setGeometry(0,100,300,50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)

        self.setStyleSheet("QRadioButton{"
                           "font-size: 40px;"
                           "font-family: Arial;"
                           "padding: 10px;"
                           "}")
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.setGeometry = (700,500,500,500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.setWindowIcon(QIcon("cisco logo.png"))
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10,10,200,40)
        self.button.setGeometry(210,10,100,40)
        self.line_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial;")
        self.button.setStyleSheet("font-size: 25px;"
                                  "font-family: Arial;")
        self.line_edit.setPlaceholderText("Enter your name")
        self.button.clicked.connect(self.submit)

    def submit(self):
        text = self.line_edit.text()
        print(f"Hello {text}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet(""
            QPushButton{
                font-size: 40px;
                font-family: Arial;
                padding: 15px, 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 15px;
            }
            QPushButton#button1{
                background-color: hsl(28, 78%, 51%);
            }
            QPushButton#button2{
                background-color: hsl(123, 85%, 52%);
            }
            QPushButton#button3{
                background-color: hsl(294, 82%, 51%);
            }
            QPushButton#button1:hover{
                background-color: hsl(28, 78%, 81%);
            }
            QPushButton#button2:hover{
                background-color: hsl(123, 85%, 82%);
            }
            QPushButton#button3:hover{
                background-color: hsl(294, 82%, 81%);
            }
        "")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.setStyleSheet(""
            QPushButton, QLabel{
                padding: 20px;
                font-weight: bold;
                font-family: calibri;
            }
            QPushButton{
                font-size: 50px;
            }
            QLabel{
                font-size: 120px;
                background-color: hsl(200, 100%, 85%);
                border-radius : 20px
            }
        
        "")

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)


    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"


    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600,400,300,100)
        self.setStyleSheet("background: black")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size: 75px;"
                                      "color: hsl(106, 98%, 51%)")

        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
    
    API = d9469dd49f05d30e50002863265a33a6
"""

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet ("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 75px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "d9469dd49f05d30e50002863265a33a6"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:

            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied")
                case 404:
                    self.display_error("Not Found:\nCity not found")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down")
                case 504:
                    self.display_error("Gateway timeout:\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occurred:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")


    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px;")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        temperature_f = temperature_k * (9/5) - 459.67
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]

        self.temperature_label.setText(f"{temperature_f:.0f}°F")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):

        if 200 >= weather_id <= 232:
            return "🌩️"

        elif 300 <= weather_id <= 321:
            return "⛅"

        elif 500 <= weather_id <= 531:
            return "🌧️"

        elif 600 <= weather_id <= 622:
            return "❄️"

        elif 701 <= weather_id <= 741:
            return "🌫️"

        elif weather_id == 762:
            return "🌋"

        elif weather_id == 771:
            return "💨"

        elif weather_id == 781:
            return "🌪️"

        elif weather_id == 800:
            return "☀️️"

        elif 801 <= weather_id <= 804:
            return "☁️"

        else:
            return ""






if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())


