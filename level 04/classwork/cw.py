'''
1) შექმენით ისეთი პროგრამა რომელიც გამოითვლის კვადრატული განტოლების ფესვებს.

პირველ რიგში შემოატანინეთ მომხმარებელს 3 რიცხვი 

შემდეგ გამოითვალეთ დისკრიმინატი

შემდეგ კი ფესვები.
'''

a = int(input("Enter a (first number): "))
b = int(input("Enter b (second number): "))
c = int(input("Enter c (third number): "))

discriminant = (b ** 2) - (4 * a * c)

x1 = (-b + discriminant ** 0.5) / (2 * a)
x2 = (-b - discriminant ** 0.5) / (2 * a)

print(x1, x2)



# 1)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1 + num2)

# 2)
age = int(input("Enter your age: "))
print(f"age after 15 years: {age + 15}")

# 3)
print(num1 > num2)
print(num1 < num2)
print(num1 == num2)
print(num1 >= num2)
print(num1 <= num2)

# 4)
print(num1 and num2)
print(num1 or num2)