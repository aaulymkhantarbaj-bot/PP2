#1
i = 0
while i < 10:
    i += 1
    if i % 2 != 0:  # Тақ сан болса
        continue
    print(f"Жұп сан: {i}")

#2
num = 1
while num <= 20:
    if num % 3 == 0:
        num += 1
        continue
    print(num)
    num += 1

#3
total = 0
count = 0
while count < 5:
    number = int(input(f"{count + 1}-санды енгізіңіз: "))
    if number < 0:
        print("Теріс сан өткізіп жіберілді")
        continue
    total += number
    count += 1
print(f"Оң сандардың қосындысы: {total}")

#4
sentence = "Python!@#PP2$%^&*()"
result = ""
index = 0

while index < len(sentence):
    char = sentence[index]
    if not char.isalpha() and char != " ":
        index += 1
        continue
    result += char
    index += 1

print(f"Бастапқы: {sentence}")
print(f"Соңғы: {result}")

#5
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  