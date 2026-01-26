# Simple string assignment
b = "Hello"
c = "World"
print(b)
print(b.lower())
print(b.upper())
d = b + " " + c
print(d)


# Multiline Strings using three quotes
multiline_text = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(multiline_text)

# Strings are Arrays: Get the character at position 1
a = "Hello, World!"
print(a[1])

# Check String Length
print(len(a))

# Check if a phrase is present in a string
txt = "The best things in life are free!"
print("free" in txt)

print(txt[:4])
print(txt[3:6])
print(txt[-7:-3])

#format
age = 18
aya = f"My name is Ayau, I am {age}"
print(aya)
