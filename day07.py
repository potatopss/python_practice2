a = [1, 2, 3, 4]
b = "sample string"

print (str(a))
print (repr(a))

print (str(b))
print (repr(b))

f = open("sample.txt", "w")
f.write("lorem ipsum dolor sit amet, consectetur adipiscing elit.")
f.close()

#

from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    yield f
    f.close()

with open_file("sample.txt", "w") as f:
    f.write("lorem ipsom blabla blabla")

print(f.closed)


# classic calculator
a = int(input("enter the first number: "))
x = int(input(" what do you want to do with a? \n type 1 for + \n type 2 for - \n type 3 for /\n type 4 for *"))
b = int(input("enter the second number: "))
if x == 1:
    q = a + b
    print(q)
elif x == 2:
    q = a - b
    print(q)
elif x == 3:
    q = a / b
    print(q)
elif x == 4:
    q = a * b
    print(q)
else:
    pass

#
print("3".isdigit())
print("+".isdigit())
print(" ".isdigit())