#1
n = input().strip()

valid = True
for digit in n:
    if int(digit) % 2 != 0:
        valid = False
        break

if valid:
    print("Valid")
else:
    print("Not valid")


#2
def isUsual(num):
    if num <= 0:
        return False

    while num % 2 == 0:
        num //= 2
    while num % 3 == 0:
        num //= 3
    while num % 5 == 0:
        num //= 5

    return num == 1


n = int(input())

if isUsual(n):
    print("Yes")
else:
    print("No")

#3
d = {
    "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
    "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"
}
rd = {v: k for k, v in d.items()}

s = input()

# операторды табу
for op in "+-*":
    if op in s:
        a, b = s.split(op)
        break

# string → сан
x = int("".join(d[a[i:i+3]] for i in range(0, len(a), 3)))
y = int("".join(d[b[i:i+3]] for i in range(0, len(b), 3)))

# есептеу
if op == "+":
    res = x + y
elif op == "-":
    res = x - y
else:
    res = x * y

# сан → string
if res == 0:
    print("ZER")
else:
    print("".join(rd[c] for c in str(res)))


#4
s=input()
d=s.upper()
print(d)

#5
s=int(input())
d=s**2
print(d)

#6
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l, self.w = l, w
    def area(self):
        return self.l * self.w

l, w = map(int, input().split())
print(Rectangle(l, w).area())

#7
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx*dx + dy*dy)


# Кірістерді оқу
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# Объектілерді жасау
p1 = Point(x1, y1)
p1.show()          # бастапқы координаттар
p1.move(x2, y2)
p1.show()          # жаңа координаттар

p2 = Point(x3, y3)
distance = p1.dist(p2)
print(f"{distance:.2f}")

#8
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        else:
            self.balance -= amount
            return self.balance


# Кірістерді оқу
balance, withdraw_amount = map(int, input().split())

# Объектіні жасау (аты маңызды емес)
acc = Account("User", balance)

# Шығару
print(acc.withdraw(withdraw_amount))

#9
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


r = int(input())
c = Circle(r)
print(f"{c.area():.2f}")


#10
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, gpa):
        super().__init__(name)
        self.gpa = gpa

    def display(self):
        print(f"Student: {self.name}, GPA: {self.gpa}")

# Кірістерді оқу
data = input().split()
name = data[0]
gpa = float(data[1])

# Объектіні жасау және шығару
s = Student(name, gpa)
s.display()

#11
class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, other):
        return Pair(self.a + other.a, self.b + other.b)

# Кірістерді оқу
x1, y1, x2, y2 = map(int, input().split())

p1 = Pair(x1, y1)
p2 = Pair(x2, y2)
result = p1.add(p2)

print(f"Result: {result.a} {result.b}")


#12
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def total_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    def total_salary(self):
        return self.salary * (1 + self.bonus / 100)

class Developer(Employee):
    def __init__(self, name, salary, projects):
        super().__init__(name, salary)
        self.projects = projects
    def total_salary(self):
        return self.salary + 500 * self.projects

class Intern(Employee):
    pass

# Кірісті оқу
data = input().split()
role, name, salary = data[0], data[1], int(data[2])

if role == "Manager":
    emp = Manager(name, salary, int(data[3]))
elif role == "Developer":
    emp = Developer(name, salary, int(data[3]))
else:
    emp = Intern(name, salary)

print(f"Name: {emp.name}, Total: {emp.total_salary():.2f}")


#13
import math
f=lambda n:n>1 and all(n%i for i in range(2,int(math.isqrt(n))+1))
a=list(map(int,input().split()))
p=list(filter(f,a))
print(*p) if p else print("No primes")

#14
# Кіріс
n = int(input())
arr = list(map(int, input().split()))
q = int(input())

# Операцияларды оқу
ops = [input().split() for _ in range(q)]

for op in ops:
    if op[0] == "add":
        x = int(op[1])
        arr = list(map(lambda a: a + x, arr))
    elif op[0] == "multiply":
        x = int(op[1])
        arr = list(map(lambda a: a * x, arr))
    elif op[0] == "power":
        x = int(op[1])
        arr = list(map(lambda a: a ** x, arr))
    elif op[0] == "abs":
        arr = list(map(lambda a: abs(a), arr))

# Нәтижені шығару
print(*arr)

