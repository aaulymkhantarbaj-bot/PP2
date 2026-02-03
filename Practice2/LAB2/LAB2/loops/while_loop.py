#1
i = 1
while i <= 5:
    print(i)
    i += 1

#2
j = 10
while j >= 1:
    print(j)
    j -= 1

#3
total = 0
num = int(input("Сан енгізіңіз (0 аяқтау үшін): "))
while num != 0:
    total += num
    num = int(input("Келесі санды енгізіңіз (0 аяқтау үшін): "))
print(f"Жалпы қосынды: {total}")

#4
n = 1
while n <= 5:
    cube = n ** 3
    print(f"{n}³ = {cube}")
    n += 1

#5
correct_password = "python123"
attempts = 3

while attempts > 0:
    password = input(f"Парольды енгізіңіз ({attempts} әрекет қалды): ")
    if password == correct_password:
        print("Қош келдіңіз!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Қате пароль. Қайталап көріңіз.")
else:
    print("Пароль бұғатталды!")