# what is list?
# list is a collection of items in a particular order
# list is mutable: changeable, addable, removable
# list index start from 0
# []: list

# example
# [ ]
# names = ['ram', 'shyam', 'hari', 12, 34]
# print(names[0])
# print(names[-0])

# data = [
#     ['ram', 'shyam', 'hari'],
#     ['ktm', 'pkr', 'bkt',[90]],
#     ['sophia', [[[[['gopal']]]]]]
# ]
# print(data[1][3][0])
# print(data[0][1])
# print(data[2][1][0][0][0][0][0])

# data = [
#     ['ram', 'sita', ['hari']],
#     ['ktm', 'pkr', 'bkt', ['pokhara']],
# ]

#
# 'append', 'clear', 'copy',
# 'count', 'extend', 'index', 'insert',
# 'pop', 'remove', 'reverse', 'sort'


# data = ['ram', 'hari']
# print(data)
# data[0] = 'sophia'
# print(data)

# data = []
# data.append('ram')
# data.append('hari')
# print(data)

# users = []
# name = input("Enter name: ")
# email = input("Enter email: ")
# phone = input("Enter phone: ")
# users.append(name)
# users.append(email)
# users.append(phone)
# print(users)

# data = ['ram', 'hari', 'sophia', 'gopal']
# data1=['madan', 'laxmi']
# data.append(data1)
# data.extend(data1)
# print(data)

# data.remove('hari')
# print(data)
# print(data.pop())
# print(data.count('ram'))
# data.insert(1, 'sita')
# data[1]= 'sita'
# print(data)
# data.append('sita')
# print(data)
# print(data)
# data.clear()
# print(data)


data=['ram','sita']
data[0]='hari'
print(data)