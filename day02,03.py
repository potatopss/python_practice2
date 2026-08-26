# more examples about OOP.
# + one practice

# 1
class Car:
    def __init__(self, brand, speed):
        if speed < 0:
            raise ValueError("Speed cannot be negative")
        self.brand = brand
        self.speed = speed


car = Car("Toyota", 180)
print(car.brand, car.speed)

# 2
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def __str__(self):
        return f"{self.brand}: {self.speed} km/h"


car = Car("Toyota", 180)
print(car)

# 3
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self._radius = radius

    def area(self):
        return 3.14159 * self._radius ** 2


c = Circle(5)
print(c.area())

# 4
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


r = Rectangle(4, 5)
print(r.area)

# 5
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_input(cls):
        name = input("Name: ")
        salary = float(input("Salary: "))
        return cls(name, salary)

emp = Employee.from_input()
print(emp.name, emp.salary)


# 6
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

s = Student("Ali", "Computer Engineering")
print(s.name, s.major)

# 7
class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("Woof!")


class Cat(Animal):
    def speak(self):
        print("Meow!")


animals = [Dog(), Cat()]
for a in animals:
    a.speak()


# 8
class Wallet:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount


w = Wallet(100)
w.deposit(50)
w.withdraw(30)
print(w.balance)


# 9
class Wallet:
    def __init__(self, balance=0):
        self.balance = balance

    def __add__(self, other):
        return Wallet(self.balance + other.balance)

    def __str__(self):
        return f"${self.balance}"


w1 = Wallet(100)
w2 = Wallet(50)
total = w1 + w2
print(total)


# 10
class Book:
    def __init__(self, title, price):
        if not title:
            raise ValueError("Title cannot be empty")
        self.title = title
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self._price = price

    def __str__(self):
        return f"{self.title} - ${self.price}"

    @classmethod
    def from_input(cls):
        title = input("Title: ")
        price = float(input("Price: "))
        return cls(title, price)


book = Book("Harry Potter", 15)
print(book)


# ONE
class Jar:

    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return "cookie " * self.size

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Invalid capacity")

        self._capacity = capacity

    @property
    def size(self):
        return self._size

    def deposit(self, n):
        if n < 0:
            raise ValueError("Invalid number of cookies")

        if self.size + n > self.capacity:
            raise ValueError("Too many cookies")

        self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Invalid number of cookies")

        if n > self.size:
            raise ValueError("Not enough cookies")

        self._size -= n