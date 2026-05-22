# 1)
registered_password = 'cybersecurity'
password_input = input("Enter password: ")

while registered_password != password_input:
  print('Incorrect password, try again')
  password_input = input("Enter password: ")
print('Logged in successfuly')


# 2)
num = int(input("Enter a number: "))
if num % 2 == 0:
  print("Even")
else:
  print("Odd")


# 3)
num1 = int(input("Enter a number:"))
if num1 % 2 == 0 and num1 > 0:
  print(range(0, num1))
else:
  print("error")


# 4)
age = int(input("Enter your age: "))

if 0 < age < 13:
  print("Child")
elif 13 < age < 18:
  print("Teen")
elif 18 < age < 59:
  print("Adult")
else:
  print("Senior")