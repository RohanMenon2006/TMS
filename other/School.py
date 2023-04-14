    # insert list and add to even and less odd numbers
# L = []
#
# n = int(input("Enter number of elements : "))
# for i in range(0, n):
#     add = int(input())
#     L.append(add)
#
# def EOReplace():
#     L2 = []
#     for a in L:
#         if a % 2 == 0:
#             res = a+1
#             L2.append(res)
#         else:
#             res = a-1
#             L2.append(res)
#     print(L2)
#
# EOReplace()

    # program to insert, search, update, display and delete records
# db = {}
# def insert():
#     name = input('Enter name: ')
#     age = int(input('Enter age: '))
#     db[name] = {'age': age}
#     print('Record inserted')
# def search():
#     name = input('Enter name: ')
#     if name in db:
#         print('Name: {}'.format(name))
#         print('Age: {}'.format(db[name]['age']))
#     else:
#         print('Record not found')
# def update():
#     name = input('Enter name: ')
#     if name in db:
#         age = int(input('Enter new age: '))
#         db[name]['age'] = age
#         print('Record updated')
#     else:
#         print('Record not found')
# def display():
#     if len(db) == 0:
#         print('Database is empty')
#     else:
#         for name, record in db.items():
#             print('Name: {}'.format(name))
#             print('Age: {}'.format(record['age']))
# def delete():
#     name = input('Enter name: ')
#     if name in db:
#         del db[name]
#         print('Record deleted1')
#     else:
#         print('Record not found')
#
# print('1. Insert record')
# print('2. Search record')
# print('3. Update record')
# print('4. Display records')
# print('5. Delete record')
# print('6. Quit')
#
# while True:
#     choice = int(input('choose: '))
#     if choice == 1:
#         insert()
#     elif choice == 2:
#         search()
#     elif choice == 3:
#         update()
#     elif choice == 4:
#         display()
#     elif choice == 5:
#         delete()
#     elif choice == 6:
#         break
#     else:
#         print('Invalid')
