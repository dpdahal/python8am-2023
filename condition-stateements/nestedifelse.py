# username = 'admin'
# password = 'admin123'
#
# if username == 'admin':
#     if password == 'admin123':
#         print('Welcome')
#     else:
#         print("password is incorrect")
# else:
#     print("username is incorrect")

# 18> <40
# 18-25:


# 10000

# if username == 'admin' and password == 'admin123':
#     print('Welcome')
# else:
#     print("username or password is incorrect")


# print("Welcome to the ATM")
# pin = input("Enter your pin: ")
# if pin == '1234':
#     total_amount = 10000
#     print(f"your balance is {total_amount}")
#     question = input("Do you want to withdraw money? ")
#     if question == 'yes':
#         amount = int(input("Enter the amount: "))
#         if amount <= total_amount:
#             total_amount = total_amount - amount
#             print("Your balance is: ", total_amount)
#             print("Please collect your cash")
#         else:
#             print("You don't have enough balance")
#     else:
#         print("Thank you for using our ATM")
# else:
#     print("Invalid pin")

# age = int(input("Enter your age: "))
# if age < 18:
#     print("You are too young to vote")
#
# elif age >= 18 and age <= 40:
#     if age >= 18 and age <= 25:
#         print("wine")
#     else:
#         print("beer")
#
# else:
#     print("You are too old to vote")

# x = 7
# y = 8
# z = 9
#
# if x > y:
#     if x > z:
#         print("x is greater")
#     else:
#         print("z is greater")
# else:
#     if y > z:
#         print("y is greater")
#     else:
#         print("z is greater")

# if x > y and x > z:
#     print("x is greater")
# elif y > x and y > z:
#     print("y is greater")
# else:
#     print("z is greater")


# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
#
# if x > y:
#     print(x, y)
# else:
#     print(y, x)

#
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
#
#
# if a > b and a > c:
#     if b > c:
#         print(a, b, c)
#     else:
#         print(a, c, b)
# elif b > a and b > c:
#     if a > c:
#         print(b, a, c)
#     else:
#         print(b, c, a)
#
# else:
#     if a > b:
#         print(c, a, b)
#     else:
#         print(c, b, a)

# data = [1, 2, 3, 4]
# print(data[2])

# data = [
#     [1, 2, 4],
#     [5, 6, 7],
# ]
# print(data[1][0])


# users = [
#     ['ram', 'ram002'],
#     ['admin', 'admin002']
# ]
#
# username = input("Enter username: ")
# password = input("Enter password: ")
#
# if users[0][0] == username and users[0][1] == password:
#     print("Welcome")
# elif users[1][0] == username and users[1][1] == password:
#     print("Welcome")
# else:
#     print("Invalid username or password")

# if [username, password] in users:
#     print("Welcome")
# else:
#     print("Invalid username or password")

# WAP to enter username and password and check if the user is valid or not

# students = [
#     {'name': 'ram', 'age': 20},
#     {'name': 'shyam', 'age': 21},
#
# ]
# print(students[0]['name'])
# print(students[2][0])

# data = [
#     {'name': 'ram', 'gender': 'male', 'status': True,
#          "address": {
#          "country": "nepal",
#              }
#      },
#     {'name': 'sita', 'gender': 'female', 'status': True,
#          "address": {
#              "country": "pokhara",
#          }
#      },
#     {'name': 'laxmi', 'gender': 'female', 'status': True,
#          "address": {
#              "country": "kathmandu"
#          }
#      },
# ]
#
# # print(data[0]['name'])
# print(data[1]['address']['country'])

# data = [1, 2, 3]
# a, b, c = data
# a = data[0]
# b = data[1]
# c = data[2]

# data =[]
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
# data.append(a)
# data.append(b)
# data.append(c)
# print(data)
#
# data = {
#     'name': '',
#     'email': '',
#     'address': '',
# }
#
# data['name'] = input("Enter name: ")
# data['email'] = input("Enter email: ")
# data['address'] = input("Enter address: ")
# # print(data)
# # name,email,address
# users = [
#     {'username': 'admin', 'password': 'admin123'},
#     {'username': 'ram', 'password': 'ram002'}
# ]

# data={'name':'ram','email':'ram@gamil.com','address':'kathmandu'

# even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# wap to enter any number and check it is divisible by 3 and 5 or not

# loop: for,while,nested loop