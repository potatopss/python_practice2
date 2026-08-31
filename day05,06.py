first, _ = input("What's your name? ").split(" ")
print(f"hello, {first}")

#

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts
# 17 sickles = 1 galleons
# 29 knuts = 1 sickes

print(total(100, 50, 25), "Knuts")

#unpacking

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

print(total(coins[0], coins[1], coins[2]), "Knuts")

#

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

print(total(*coins), "Knuts")

#

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts")

#args & kwargs
import sys
print(sep=' ', end='\n', file=sys.stdout, flush=False)

#

def f(*args, **kwargs):
    print("Positional:", args)


f(100, 50, 25)

#map

def f(*args, **kwargs):
    print("Named:", kwargs)

f(galleons=100, sickles=50, knuts=25)

#

def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

main()

#

def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


main()

#

def main():
    yell("this", "is", "cs50")

def yell(*words):
    uppercased = [arg.upper() for arg in words]
    print(*uppercased)

main()

#list comprehension

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]
for gryffindor in sorted(gryffindors):
    print(gryffindor)

#

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]


gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])

#

students = ["Hermione", "Harry", "Ron"]

gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)

#enumerate

students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i + 1, student)

#


def main():
    n = int(input("What's n? "))
    for i in range(n + 1):
        print(sheep(i))

def sheep(n):
    return "sheep " * n


main()

#generator


def main():
    n = int(input("What's n? "))
    for j in sheep(n):
        print(j)


def sheep(n):
    flock = []
    for i in range(n):
        flock.append("sheep " * (i + 1))
    return flock


main()


#

def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "sheep " * (i + 1)

main()

#last project(just copy pasteing this one)

import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()