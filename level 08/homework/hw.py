# 1.შექმენი ლისტი 5 რიცხვით და დაბეჭდე.
numbers1 = [1, 2, 3, 4, 5]
print(numbers1)


# 2. numbers = [10, 20, 30, 40, 50], დაბეჭდე პირველი და ბოლო ელემენტი.
numbers2 = [10, 20, 30, 40, 50]
print(numbers2[0])
print(numbers2[-1])


# 3. numbers = [1, 2, 3, 4, 5], შეცვალე მესამე ელემენტი (3) 100-ით.
numbers3 = [1, 2, 3, 4, 5]
numbers3[2] = 100


# 4. numbers = [5, 10, 15, 20, 25], დაბეჭდე რამდენი ელემენტია ლისტში.
numbers4 = [5, 10, 15, 20, 25]
print(len(numbers4))


# 5. numbers = [2, 4, 6, 8, 10], for ციკლით დაბეჭდე ყველა ელემენტი ცალ-ცალკე.
numbers5 = [2, 4, 6, 8, 10]
for i in numbers5:
  print(i)


# 6. მომხმარებელს შემოატანინე 3 რიცხვი და ჩაწერე ლისტში.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

numbers6 = [num1, num2, num3]


# 7. numbers = [1, 2, 3], გამოითვალე ჯამი.
numbers7 = [1, 2, 3]
print(sum(numbers7))


# 8. numbers = [8, 3, 12, 1, 6], იპოვე ყველაზე პატარა რიცხვი(min - ის გარეშე).
numbers8 = [8, 3, 12, 1, 6]
lowest = numbers8[0]
for i in numbers8:
  if i < lowest:
    lowest = i
print(lowest)


# 9. numbers = [1, 2, 3, 4, 5, 6], დაბეჭდე მხოლოდ ლუწი რიცხვების ჯამი.
numbers9 = [1, 2, 3, 4, 5, 6]
evens_sum = 0
for i in numbers9:
  if i % 2 == 0:
    evens_sum += i
print(evens_sum)


# 10. numbers = [10, 15, 20, 25, 30, 35], დაბეჭდე მხოლოდ კენტი რიცხვები.
numbers10 = [10, 15, 20, 25, 30, 35]
odds_sum = 0
for i in numbers10:
  if i % 2 != 0:
    odds_sum += i
print(odds_sum)