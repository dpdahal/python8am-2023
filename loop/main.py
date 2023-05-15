# what is loop?
# loop is repeat something again and again until the condition is false
# there are two types of loop
# 1. for loop: for loop is used to iterate over a sequence
# 2. while loop: while loop is used to iterate over a block of code as long as the condition is true
# 3. nested loop: nested loop is loop inside loop

# data = ['ram', 'sita', 'hari', 'gita', 'laxmi']
# total = 0
# for name in data:
#     print(name)
#     total += 1
#
# print('total user', total)
# print("total user ", len(data))

# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]
# total_even=0
# total_odd=0
# for num in number:
#     if num % 2 == 0:
#         total_even += 1
#     else:
#         total_odd += 1
# print('total even', total_even)
# print('total odd', total_odd)

# data = ['ram', 'sita', 'hari', 'gita', 'laxmi']
# for name in data:
#     if name == 'ram' or name == 'laxmi':
#         print(name)

#
# data = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 14]
# ]
# total_even = 0
# total_odd = 0
# for num in data:
#     for a in num:
#         if a % 2 == 0:
#             total_even += 1
#         else:
#             total_odd += 1
# print('total even', total_even)
# print('total odd', total_odd)


# data = [
#     {'name': 'ram', 'age': 20, 'gender': 'male', 'status': True},
#     {'name': 'sita', 'age': 21, 'gender': 'female', 'status': True},
#     {'name': 'hari', 'age': 21, 'gender': 'male', 'status': True},
#     {'name': 'gita', 'age': 21, 'gender': 'female', 'status': False},
#     {'name': 'madan', 'age': 21, 'gender': 'male', 'status': False},
#
# ]
# total_users = len(data)
# total_active_user = 0
# total_inactive_user = 0
# total_active_male = 0
# total_inactive_male = 0
# total_active_female = 0
# total_inactive_female = 0
# for user in data:
#     if user['status'] == True:
#         total_active_user += 1
#         if user['gender'] == 'male':
#             total_active_male += 1
#         if user['gender'] == 'female':
#             total_active_female += 1
#
#     else:
#         if user['gender'] == 'male':
#             total_inactive_male += 1
#         if user['gender'] == 'female':
#             total_inactive_female += 1
#         total_inactive_user += 1
#
# print('total users', total_users)
# print('total active user', total_active_user)
# print('total inactive user', total_inactive_user)
# print('total active male', total_active_male)
# print('total inactive male', total_inactive_male)
# print('total active female', total_active_female)
# print('total inactive female', total_inactive_female)

# x = 1
# data = []
# num = int(input('enter number'))
#
# while x <= num:
#     name = input('enter name')
#     data.append(name)
#     x += 1
#
# print(data)

# number of students
# nep,eng,math,sci,soc

# enter of times

# 1,2,3,4,5,6,7,2,3
# nested loop

# students =['ram','sita','hari','gita','madan']

# num = int(input("Enter number of students: "))
# x = 1
# students_marks = []
# while x <= num:
#     for a in range(1):
#         nepali = int(input("Enter nepali marks: "))
#         english = int(input("Enter english marks: "))
#         computer = int(input("Enter computer marks: "))
#         math = int(input("Enter math marks: "))
#         science = int(input("Enter science marks: "))
#         total = nepali + english + computer + math + science
#         students_marks.append(total)
#     x += 1
# for mark in students_marks:
#     percentage = mark / 5
#     if percentage > 35 and percentage <= 45:
#         print("C")
#     elif percentage > 45 and percentage <= 60:
#         print("B")
#     elif percentage > 60 and percentage <= 80:
#         print("A")
#     elif percentage > 80 and percentage <= 100:
#         print("A+")
#     else:
#         print("Fail")

# data = [
#     [
#         [1, 2, 3, 4, 5],
#         [11, 12, 13, 14, 15],
#         [81, 92, 93, 49, 95]
#     ]
# ]
# total = 0
# for x in data:
#     for a in x:
#         for y in a:
#             total+=y
#
# print(total)

#
# data = [
#     {'name': 'ram', 'age': 20, 'gender': 'male', 'status': True},
#     {'name': 'sita', 'age': 21, 'gender': 'female', 'status': True},
#     {'name': 'hari', 'age': 21, 'gender': 'male', 'status': True},
#     {'name': 'gita', 'age': 21, 'gender': 'female', 'status': False},
#     {'name': 'madan', 'age': 21, 'gender': 'male', 'status': False},
#
# ]
#
# total_users = len(data)
# total_active_user = 0
# total_inactive_user = 0
# total_active_male = 0
# total_inactive_male = 0
# total_active_female = 0
# total_inactive_female = 0
#
# x = 0
# while x < len(data):
#     if data[x]['status'] == True:
#         total_active_user += 1
#         if data[x]['gender'] == 'male':
#             total_active_male += 1
#         if data[x]['gender'] == 'female':
#             total_active_female += 1
#
#     else:
#         if data[x]['gender'] == 'male':
#             total_inactive_male += 1
#         if data[x]['gender'] == 'female':
#             total_inactive_female += 1
#         total_inactive_user += 1
#
#     x += 1
#
# print('total users', total_users)
# print('total active user', total_active_user)
# print('total inactive user', total_inactive_user)
# print('total active male', total_active_male)
# print('total inactive male', total_inactive_male)
# print('total active female', total_active_female)
# print('total inactive female', total_inactive_female)


data = [
    [1, 2, 3, 4, 5],
    [11, 12, 13, 14, 15],
    [81, 92, 93, 49, 95]
]

x=0
while x<len(data):
    y=0
    while y<len(data[x]):
        print(data[x][y])
        y+=1
    x+=1

# function