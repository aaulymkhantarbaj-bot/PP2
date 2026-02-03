# 1. Тек жұп сандарды шығару
for num in range(1, 7):
    if num % 2 == 1:  # тақ сан
        continue
    print(num)

# 2. "алма" өткізіп жіберу
fruits = ["алма", "алмұрт", "алма", "банан"]
for fruit in fruits:
    if fruit == "алма":
        continue
    print(fruit)

# 3. Теріс сандарды өткізіп жіберу
numbers = [5, -2, 3, -1, 4]
total = 0
for num in numbers:
    if num < 0:
        continue
    total = total + num
print("Оң сандар қосындысы:", total)

# 4. 3-ке бөлінетін сандарды өткізіп жіберу
for num in range(1, 11):
    if num % 3 == 0:
        continue
    print(num)

# 5. Бос жолдарды өткізіп жіберу
lines = ["one", "", "two", "", "three"]
for line in lines:
    if line == "":
        continue
    print(line)
