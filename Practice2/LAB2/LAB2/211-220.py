#11
n, l, r = map(int, input().split())
a = list(map(int, input().split()))

l -= 1
r -= 1

while l < r:
    a[l], a[r] = a[r], a[l]
    l += 1
    r -= 1

for x in a:
    print(x, end=" ")

#12
n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    a[i] = a[i] * a[i]

for x in a:
    print(x, end=" ")

#13
n = int(input())

if n <= 1:
    print("No")
else:
    for i in range(2, n):
        if n % i == 0:
            print("No")
            break
    else:
        print("Yes")

#14
n = int(input())
a = list(map(int, input().split()))

freq = {}
for x in a:
    freq[x] = freq.get(x, 0) + 1

mx = max(freq.values())
ans = min(x for x in freq if freq[x] == mx)

print(ans)

#15
n = int(input())
surnames = set()

for _ in range(n):
    surnames.add(input())

print(len(surnames))

#16
n = int(input())
a = list(map(int, input().split()))

seen = set()
for x in a:
    if x in seen:
        print("NO")
    else:
        print("YES")
        seen.add(x)

#17
n = int(input())
freq = {}

for _ in range(n):
    num = input()
    freq[num] = freq.get(num, 0) + 1

count = 0
for v in freq.values():
    if v == 3:
        count += 1

print(count)

#18
n = int(input())
arr = []

for i in range(1, n + 1):
    s = input()
    arr.append((s, i))

first_pos = {}
for s, i in arr:
    if s not in first_pos:
        first_pos[s] = i

for s in sorted(first_pos):
    print(s, first_pos[s])

#18.1
n = int(input())
arr = []

for i in range(n):
    arr.append(input())

used = []
for s in arr:
    if s not in used:
        used.append(s)

used.sort()

for s in used:
    print(s, arr.index(s) + 1)


#19
n = int(input())
d = {}

for _ in range(n):
    name, k = input().split()
    k = int(k)
    d[name] = d.get(name, 0) + k

for name in sorted(d):
    print(name, d[name])

#20
import sys

input = sys.stdin.readline

n = int(input())
db = {}
out = []

for _ in range(n):
    line = input().rstrip('\n')

    if line.startswith("set"):
        parts = line.split(maxsplit=2)
        key = parts[1]
        value = parts[2] if len(parts) == 3 else ""
        db[key] = value

    else:  
        key = line.split()[1]
        if key in db:
            out.append(db[key])
        else:
            out.append(f"KE: no key {key} found in the document")

sys.stdout.write("\n".join(out))

#20.1
# Командалар санын оқу
n = int(input())

# Бос құжат (dictionary)
doc = {}

# Командаларды өңдеу
for _ in range(n):
    parts = input().split()  # Команданы бөліп алу
    command = parts[0]

    if command == "set":
        key = parts[1]
        value = parts[2]
        # Ключты қосу немесе жаңарту
        doc[key] = value
    elif command == "get":
        key = parts[1]
        # Егер ключ бар болса, мәнін шығару
        if key in doc:
            print(doc[key])
        else:
            # Егер ключ жоқ болса, қате хабар
            print("KE: no key", key, "found in the document")

