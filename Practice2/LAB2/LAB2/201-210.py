#1
year = int(input())

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("YES")
else:
    print("NO")

#2
n = int(input())
total = 0
for i in range(1, n + 1):
    total += i
print(total)

#3
n = int(input())
a = list(map(int, input().split()))

s = 0
for i in range(n):
    s = s + a[i]

print(s)

#4
n = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if a[i] > 0:
        cnt += 1

print(cnt)

#5
n = int(input())

if n <= 0:
    print("NO")
else:
    while n % 2 == 0:
        n = n // 2

    if n == 1:
        print("YES")
    else:
        print("NO")

#6
n = int(input())
a = input().split()

mx = int(a[0])
for i in range(1, n):
    if int(a[i]) > mx:
        mx = int(a[i])

print(mx)

#7
n = int(input())
a = list(map(int, input().split()))

max_value = a[0]
max_pos = 1 

for i in range(1, n):
    if a[i] > max_value:
        max_value = a[i]
        max_pos = i + 1  

print(max_pos)

#8
n = int(input())

power = 1
while power <= n:
    print(power, end=" ")
    power *= 2

#9
n = int(input())
a = list(map(int, input().split()))

mx = max(a)
mn = min(a)

for i in range(n):
    if a[i] == mx:
        a[i] = mn

for x in a:
    print(x, end=" ")

#10
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
print(*a)


