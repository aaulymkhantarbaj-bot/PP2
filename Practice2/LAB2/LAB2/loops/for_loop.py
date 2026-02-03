#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#2
for i in range(1, 11):
    print(i, end=" ")

#3
word = "Python"
for letter in word:
    print(letter)

#4
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Матрица:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # Жаңа жол

#5
student = {
    "name": "Аyau",
    "age": 18,
}

print("KBTUstudent:")
for key, value in student.items():
    print(f"{key}: {value}")