#1
def squares(n):
    for i in range(1, n + 1):
        yield i * i

n = int(input())

for num in squares(n):
    print(num)

#2
def func(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input())

first = True
for i in func(n):
    if not first:
        print(",", end="")
    print(i, end="")
    first = False


#3
def func(n):
    for i in range(0, n + 1):
        if i % 12 == 0:
            yield i

n = int(input())

first = True
for i in func(n):
    if not first:
        print(" ", end="")
    print(i, end="")
    first = False


#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a, b = map(int, input().split())

for value in squares(a, b):
    print(value)


#5
def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())

for number in countdown(n):
    print(number)


#6
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

n = int(input())

first = True
for num in fibonacci(n):
    if not first:
        print(",", end="")
    print(num, end="")
    first = False

#7
class Reverse:
    def __init__(self, string):
        self.string = string
        self.index = len(string) - 1  # start from the last character

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        char = self.string[self.index]
        self.index -= 1
        return char

# Read input
s = input()

# Use the Reverse iterator
rev_iter = Reverse(s)
for c in rev_iter:
    print(c, end='')

#8
def primes_up_to(n):
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num

# Input
n = int(input())

# Output
for p in primes_up_to(n):
    print(p, end=' ')


#9
def powers_of_two(n):
    power = 1
    for _ in range(n+1):
        yield power
        power *= 2

# Input
n = int(input())

# Output
for p in powers_of_two(n):
    print(p, end=' ')

#10
def limited_cycle(lst, n):
    for _ in range(n):
        for item in lst:
            yield item

# Input
lst = input().split()
n = int(input())

# Output
for x in limited_cycle(lst, n):
    print(x, end=' ')


#11
import json

def patch(source, patch_obj):
    for key, value in patch_obj.items():
        if value is None:
            if key in source:
                del source[key]
        elif key in source and isinstance(source[key], dict) and isinstance(value, dict):
            patch(source[key], value)
        else:
            source[key] = value
    return source

# Input
source = json.loads(input())
patch_obj = json.loads(input())

# Apply patch
result = patch(source, patch_obj)

# Output compact JSON with sorted keys
print(json.dumps(result, separators=(',', ':'), sort_keys=True))
