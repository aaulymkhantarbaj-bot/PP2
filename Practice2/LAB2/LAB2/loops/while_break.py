#1
num = 1
while True:
    print(num)
    if num == 7:
        print("7 табылды! Цикл тоқтатылды.")
        break
    num += 1

#2
total = 0
i = 1
while True:
    total += i
    print(f"{i} қосылды. Қосынды: {total}")
    if total > 100:
        print(f"Қосынды 100-ден асты! Соңғы қосылған сан: {i}")
        break
    i += 1

#3
while True:
    word = input("Кез келген сөз енгізіңіз ('stop' аяқтау үшін): ")
    if word.lower() == 'stop':
        print("Бағдарлама аяқталды.")
        break
    print(f"Сіз енгіздіңіз: {word}")

#4
import random
attempts = 0
while True:
    random_num = random.randint(1, 10)
    attempts += 1
    print(f"Әрекет {attempts}: {random_num}")
    if random_num == 5:
        print(f"5 табылды! {attempts} әрекет қажет болды.")
        break

#5
factorial = 1
n = 1
while True:
    factorial *= n
    print(f"{n}! = {factorial}")
    if factorial > 1000000:  # 1 миллионнан асқанда
        print(f"Факториал 1,000,000-нан асты! n = {n}")
        break
    n += 1
    