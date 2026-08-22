1.
def check(first, second):
    if first < second:
        for number in range(first, second + 1):
            is_prime = True
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime == True:
                print(number)
    else:
        print("second number should be greater than first number")

check(int(input("enter the first number: ")),
      int(input("enter the second number: ")))



2.
# VERSION2.1
remaining = int(input("enter the number of the stars: "))
line = 1
for line in range(1, remaining + 1):
    print("*" * line)
    remaining = remaining - line
    if remaining <= line:
        break

# VERSION2.2
star = int(input("enter the number of the lines:" ))
for number in range(1,star):
    print("*" * number)


3.#(25% AI)
menu = [
    {"name": "Baja Taco",        "price": 4.25},
    {"name": "Burrito",          "price": 7.5},
    {"name": "Bowl",             "price": 8.5},
    {"name": "Nachos",           "price": 11.00},
    {"name": "Quesadilla",       "price": 8.5},
    {"name": "Super Burrito",    "price": 8.5},
    {"name": "Super Quesadilla", "price": 9.5},
    {"name": "Taco",             "price": 3.00},
    {"name": "Tortilla Salad",   "price": 8.00}
]
for item in menu:
    print(item["name"])

total = 0
while True:
    try:
        order = str(input("what do you like to eat? "))
        for item in menu:
            if order.lower() == item["name"].lower():
                total += item["price"]
    except EOFError:
        # press ctrl + z (or ctrl + d) to end
        print(f"Total: ${total}")
        break



4.#(25% AI)

import random

while True:
    try:
        lvl = input("define range: ")
        lvl = int(lvl)
        if lvl > 0:
            break
    except ValueError:
        pass

num = random.randint(1, lvl)

while True:
    try:
        g_num = int(input("guess the number: "))
        if g_num == num:
            print("just right!")
            break
        elif g_num > num:
            print("too large")
        elif g_num < num:
            print("too small")
    except ValueError:
        pass



5.#(30% AI)
import random


def get_num():
    num1 = random.randint(100, 999)
    num2 = random.randint(100, 999)
    total = num1 + num2
    is_correct = False

    for i in range(3):
        if i == 0:
            answer = int(input(f"what is the result of {num1} + {num2}? "))

        if answer == total:
            print("EXCELLENT!")
            is_correct = True
            break
        elif i != 2:
            answer = int(input("TRY AGAIN: "))
        else:
            break

    if not is_correct:
        print(f"ops. the answer is {total}")


while True:
    get_num()
