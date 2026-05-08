# 1) შექმენი ცვლადი და დაბეჭდე მისი ტიპი.
x = 25
print(type(x))

# 2) შექმენი ცვლადი და შეამოწმე არის თუ არა str.
word = "Hello"
print(isinstance(word, str))

# 3) შექმენი და დაბეჭდე მისი ტიპი.
z = 3
print(type(z))

# 4) მომხმარებელს შემოატანინე მონაცემი და შეამოწმე რა ტიპია.
data = input("Enter something: ")
print(type(data))

# 5) სტრინგი გადააქციე integer-ად.
s_num = "10"
i_num = int(s_num)

# 6) integer გადააქციე string-ად.
number = 50
text = str(number)

# 7) სტრინგი გადააქციე float-ად.
s_float = "12.5"
f_num = float(s_float)

# 8) float გადააქციე integer-ად.
price = 99.99
whole_price = int(price)

# 9) მომხმარებლის შემოტანილი რიცხვი string-იდან integer-ად გადააქციე.
user_input = input("Enter a number: ")
convert_input = int(user_input)

# 10) კოდი არასწორად აერთიანებს რიცხვებს, გაასწორე:
num1 = "10"
num2 = "20"
print(int(num1) + int(num2))

# 11) კოდი ტექსტს ვერ უმატებს რიცხვს, გაასწორე:
age = 15
print("Age: " + str(age))

# 12) შეამოწმე არის თუ არა 10 მეტი 5-ზე.
print(10 > 5)

# 13) შეამოწმე არის თუ არა ორი რიცხვი ტოლი.
print(5 == 5)

# 14) შეამოწმე არის თუ არა 3 ნაკლები 1-ზე.
print(3 < 1)

# 15) მომხმარებლის ასაკი შეადარე 18-ს.
user_age = int(input("Enter your age: "))
print(user_age >= 18)