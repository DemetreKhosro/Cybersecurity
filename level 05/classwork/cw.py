# მომახმარებელს შემოატანინეთ 2 რიცხვი, რომელსაც გარდაქმნით მტელ რიცხვად, შემდეგ კი ჩაატარეთ ყველა მათემატიკური ოპერაცია, არითმეტიკული და შედარების ოპერაციები ამ ორ რიცხვს შორის. > < >= <= ==

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(a // b)
print(a % b)

print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)


# გამოიყენეთ and/or ლოგიკური ოპერაციები ყველა შესაძლო ვარიანტით რომ შეამოწმოთ შედეგები.
# print(True and False)
# print(True and True)
# და ასშ.

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)


# 3)

# 1.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 > num2)
print(num1 == num2)
print(num1 != num2)

# 2.
age = int(input("Enter age: "))

print(age >= 18)
print(age < 13)
print(age >= 13 and age <= 18)

# 3.
password = input("Enter password: ")

print(len(password) >= 8)
print(len(password) < 8)
print(len(password) == 12)

# 4.
number = int(input("Enter number: "))

print(number > 0)
print(number >= 1 and number <= 100)
print(number != 50)

# 5.
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print(n1 % 2 == 0 and n2 % 2 == 0)
print(n1 % 2 != 0 or n2 % 2 != 0)
print(n1 == n2)