#11
s=input()
print(s[0],s[-1])

#12
s=input()
print(s[2:5])

#13
s=input()
print(s[::-1])

#14
name=input()
age=int(input())
print(f"Hello, {name}. You are {age} years old.")

#15
long=input()
short=input()
print(short in long)

#16
a=input()
b=input()
print(a+b)

#17
a=input()
b=input()
print(b,a)

#18
a=int(input())
if a%2==0:
    print("even")
else:
    print("odd") 

#19
sent=input()
target=input()
repl=input()
print(sent.replace(target, repl))

#20
a=int(input())
b=int(input())
if a>b:
    print(a)
elif a<b:
    print(b)
else:
    print("equal")