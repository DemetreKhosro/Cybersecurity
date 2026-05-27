# 1)
numbers = []
for i in range(5):
  num = int(input("Enter a number: "))
  numbers.append(num)

print(numbers)
print(numbers[0])
print(numbers[-1])
print(numbers[-5])
print(numbers[4])
print(numbers[::-1])


# 2)
animals = ["dog", "cat", "lion", "tiger", "elephant"]

print(animals[1])
print(animals[-4])

print(animals[4])
print(animals[-1])

print(animals[0:3])
print(animals[-5:-2])

print(animals[0::2])
print(animals[-5::2])

print(animals[::-1])
print(animals[-1:-6:-1])


# 3)
# for loop
names = []
for i in range(6):
  name = input()
  names.append(name)

print(names)
print(names[0:3])
print(names[4:6])
print(names[0::2])

# while loop
names = []
i = 0
while i < 6:
  name = input()
  names.append(name)
  i += 1

print(names)
print(names[0:3])
print(names[4:6])
print(names[0::2])


# 4)
colors = ["red", "blue", "green", "yellow", "black", "white"]

for i in range(len(colors)):
  print(f"{i} {colors[i]}")


# 5)
letters = ["a", "b", "c", "d", "e", "f", "g"]

print(letters[-5])
print(letters[1::2])
print(letters[0:4])
print(letters[4:7])
print(letters[::-1])