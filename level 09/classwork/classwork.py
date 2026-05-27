# 1)
numbers = []
for i in range(10):
  num = int(input("Enter a number"))
  numbers.append(num)

even_sum = 0
odd_sum = 0

for num in numbers:
  if num % 2 == 0:
    print("Even")
    even_sum += num
  else:
    print("Odd")
    odd_sum += num

print(even_sum)
print(odd_sum)


# 2)
numbers = []

for i in range(5):
  num = int(input("Enter a number: "))
  if num % 2 == 0:
    numbers.append(num ** 2)


# 3)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in a[4:10]:
  if num % 2 == 0:
    print("Even")
  else:
    print("Odd")

# 4)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = a[::-1]
print(b)