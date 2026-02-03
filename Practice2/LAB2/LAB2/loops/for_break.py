#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
#2
numbers = [2, 4, 6, 5, 8, 10]
for num in numbers:
    print(num)
    if num == 5:
        break

#3
for num in [3, 7, 12, 5, 9]:
    if num > 10:
        print(num, "10-нан үлкен")
        break

#4
total = 0
for n in [5, 3, 8, 4, 6]:
    total = total + n
    if total > 15:
        print("Қосынды 15-тен асты:", total)
        break

#5
for num in [3, 7, 4, 9, 2]:
    if num % 2 == 0:
        print("Бірінші жұп сан:", num)
        break
    