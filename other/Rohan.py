# # 1
# num = int(input("Enter a natural number: "))
# fact = 1
#
# if num < 0:
#     print("Factorial is not a defined for negative number.")
# elif num == 0:
#     print("The factorial of 0 is 1.")
# else:
#     for i in range(1, num + 1):
#         fact *= i
#     print("The factorial of", num, "is", fact)

# # 2
# num = int(input("the number of terms you want to generate: "))
# a, b = 0, 1
#
# for i in range(num):
#     print(a, end=" ")
#     a, b = b, a
#
# numbers = []

# # 3
# numbers = []
# n = int(input("the number of elements you want to add to the list: "))
#
# for i in range(n):
#     num = int(input("Enter a number: "))
#     numbers.append(num)
#
# num_sum = 0
# for number in numbers:
#     num_sum += number
#
# print("The sum of all the elements in the list is: ", num_sum)

# # 4
# string = input("Enter a word: ")
# if string == string[::-1]:
#     print(string, " is a palindrome.")
# else:
#     print(string, " is not a palindrome.")

# # 5
# import random
#
# num = random.randint(1, 6)
# print("random number: ", num)

# # 6
# file = open("Test_file.txt", "r")
# line_count = 0
#
# for line in file:
#     line_count =+ 1
#
# print("The program has", line_count, "lines.")

# # 7
# fh = open("Test_file.txt", "r")
# data = fh.readlines()
# for i in data:
#     print(i.replace(" ", "#"))

# # 8
# f1 = open("Test_file.txt", "r")
# f2 = open("Test_file2.txt", "w")
#
# for line in f1:
#     if 'A' in line:
#         f2.write(line)
# f1.close()
# f2.close()
#
# f3 = open("Test_file2.txt", "r")
# output = f3.read()
# print(output)
# f3.close()

# # 9
# import random
# fh = open("Test_file.txt", "r")
# l = fh.readlines()
# rl = random.choice(l)
# print(rl)
# fh.close()

# # 10
# import pickle
#
# def create(fn, data):
#     fh = open(fn, 'wb')
#     pickle.dump(data, fh)
#
# def read():
#     fl = open(fn, 'rb')
#     data = pickle.load(fl)
#     return data
#
# fn = "data.bin"
# data = {'name': 'John', 'age': 30, 'city': 'New York'}
# create(fn, data)
# read_data = read()
# print(read_data)

# # 11
# import pickle
# data = {'name': 'John', 'age': 30, 'city': 'New York'}
# fh = open("data.bin", 'wb')
# pickle.dump(data, fh)
# print("Data Stored")
# fh.close()

# # 12
# db = {}
#
# def insert():
#     name = input('Enter name: ')
#     age = int(input('Enter age: '))
#     db[name] = {'age': age}
#     print('Record inserted')
#
# def search():
#     name = input('Enter name: ')
#     if name in db:
#         print('Name: {}'.format(name))
#         print(' Age: {}'.format(db[name]['age']))
#     else:
#         print('Record not found')
#
# def update():
#     name = input('Enter name: ')
#     if name in db:
#         age = int(input('Enter new age: '))
#         db[name]['age'] = age
#         print('Record updated')
#     else:
#         print('Record not found')
#
# def display():
#     if Len(db) == 0:
#         print('Database is empty')
#     else:
#         for name, record in db.items():
#             print('Name: {}'.format(name))
#             print(' Age: {}'.format(record['age']))
#
# def delete():
#     name = input('Enter name: ')
#     if name in db:
#         del db[name]
#         print('Record deleted')
#     else:
#         print('Record not found')
#
# print('l. Insert record')
# print('2. Search record')
# print('3. Update record')
# print('4. Display records')
# print('5. Delete record')
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
#         display ( )
#     elif choice == 5:
#         delete()
#     else:
#         print('Invalid entry')

# # 13
# marks = {"Rohan": 99, "Arjun": 98, "Ansh" : 88}
# print("Records with marks greater than 95:")
# for name, mark in marks.items():
#     if mark > 95:
#         print(name, mark)

# # 14
# import csv
#
# data = [
#     ['Rohan', '17'],
#     ['Arjun', '17'],
#     ['Ansh', '16']
# ]
#
# fh = open('data.csv', 'w', newline='')
# write = csv.writer(fh)
# write.writerows(data)
# print("Data written")
# fh.close()

# # 15
# import csv
#
# fh = open('data.csv', 'r')
# reader = csv.reader(fh)
# for row in reader:
#     print(row)
# fh.close()

# # 16
# import numpy as np
# import matplotlib.pyplot as plt
#
# def Plot_Function():
#     x = np.linspace(-50, 50);
#     y = x**2
#     plt.plot(x, y, linestyle='-')
#     plt.show( )
#
# Plot_Function()

# # 17
# def check_stack(stk):
#     if stk == []:
#         return True
#     else:
#         return False
#
# def push(stk, e):
#     stk.append(e)
#     top = len(stk)-1
#
# def display(stk):
#     if check_stack(stk):
#         print("Stack is Empty")
#     else:
#         top = len(stk)-1
#         print(stk[top], "-Top")
#         for i in range(top-1,-1,-1):
#             print(stk[i])
#
# def pop_stack(stk):
#     if check_stack(stk):
#         return "UnderFlow"
#     else:
#         e = stk.pop()
#     if len(stk)==0:
#         top = None
#     else:
#         top = len(stk)-1
#         return e
#
# def peek(stk):
#     if check_stack(stk):
#         return "UnderFlow"
#     else:
#         top = len(stk)-1
#         return stk[top]
#
# s = []
# top = None
#
# def main_menu():
#     while True:
#         print("Stack Implementation")
#         print("1 - Push")
#         print("2 - Pop")
#         print("3 - Peek")
#         print("4 - Display")
#         print("5 - Exit")
#
#         ch = int(input("Enter option : "))
#         if ch == 1:
#             el = int(input("Enter value to push an element:"))
#             push(s,el)
#         elif ch == 2:
#             e = pop_stack(s)
#             if e == "UnderFlow":
#                 print("Stack underflow!")
#             else:
#                 print("Element popped: ", e)
#         elif ch == 3:
#             e = pop_stack(s)
#             if e == "UnderFlow":
#                 print("Stack underflow!")
#             else:
#                 print("The element on top is: ", e)
#         elif ch == 4:
#             display(s)
#         elif ch == 5:
#             break
#         else:
#             print("Invalid option")
#
# main_menu()

# # 18
# stk = []
# top = -1
#
# def line():
#     print('~'*100)
#
# def isEmpty():
#     global stk
#     if stk == []:
#         print("Stack is Empty")
#     else:
#         None
#
# def push():
#     global stk
#     global top
#     empno = int(input("Enter the employee number to push: "))
#     ename = input("Enter the employee name to push: ")
#     stk.append([empno, ename])
#     top = len(stk)-1
#
# def display():
#     global stk
#     global top
#     if top == -1:
#         isEmpty()
#     else:
#         top = len(stk)-1
#         print(stk[top], "<-top")
#         for i in range( top-1, -1, -1):
#             print(stk[i])
#
# def pop_ele():
#     global stk
#     global top
#     if top == -1:
#         isEmpty()
#     else:
#         stk.pop()
#         top = top-1
#
# def main():
#     while True:
#         line()
#         print("1 - Push")
#         print("2 - Pop")
#         print("3 - Display")
#         print("4 - Exit")
#         ch = int(input("Enter your choice : "))
#
#         if ch == 1:
#             push()
#             print("Element Pushed")
#         elif ch == 2:
#             pop_ele()
#         elif ch ==3:
#             display()
#         elif ch == 4:
#             break
#         else:
#             print("Invalid choice")
#
# line()
# main()


# # 1
# import mysql.connector
#
# def insert():
#     mydb = mysql.connector.connect(host="localhost", user="root", passwd="dbxcbe", database="STUDENTDATABASE")
#     mycursor = mydb.cursor()
#     print("Database Connected")
#
#     R = []
#     reg = int(input("Enter Regn No.: "))
#     R.append(reg)
#     nm = input("Enter name: ")
#     R.append(nm)
#     cl = int(input("Enter class: "))
#     R.append(cl)
#     gen = input("Enter Gender (M/F): ")
#     R.append(gen)
#
#     NEWR = R
#     Q = "INSERT INTO STUDENT(REGN, NAME, CLASS GANDER)VALUES(%S,%S,%S,%S)"
#     mycursor.execute(Q, NEWR)
#     mydb.commit()
#     print("insertion completed")
# insert()

# # 2
# import mysql.connector
#
# def view():
#     mydb = mysql.connector.connect(host="localhost", user="root", passwd="dbxcbe", database="STUDENTDATABASE")
#     mycursor = mydb.cursor()
#     print("Database Connected.... Record view Facility")
#     v = int(input("1. All Records \n2. Particular Record \nEnter Choice: "))
#     if v == 1:
#         Q = "SELECT * FROM STUDENT"
#         mycursor.execute(Q)
#         res = mycursor.fetchall()
#         print("Details Are Given Bellow: ")
#         print("----------------------------------------------")
#         print('Regn       Name        Class       Gander')
#         print("----------------------------------------------")
#         c = 0
#         for x in res:
#             print(x[O], "\t", x[1], "\t\t", x[2], "\t", x[3])
#             c = c+l
#             print("\n—--------------------------------------------")
#             print("\n Total Records Are: ", c)
#
#     elif v == 2:
#         r = input("Enter Regn No.: ")
#         reg = (r, )
#         Q = "SELECT * FROM STUDENT WHERE REGN = %S"
#         mycursor.execute(Q, reg)
#         res = mycursor.fetchall()
#         print("Details Are Given Bellow: ")
#         print("----------------------------------------------")
#         print('Regn       Name        Class       Gander')
#         print("----------------------------------------------")
#         for x in res:
#             print (x[O], "\t", x[1], "\t\t", x[2], "\t", x[3])
# view()

# # Output
# print("Database Connected.... Record view Facility")
# v = int(input("1. All Records \n2. Particular Record \nEnter Choice: "))
# Q = "SELECT * FROM STUDENT"
# print("Details Are Given Bellow: ")
# print("----------------------------------------------")
# print('Regn       Name        Class       Gander')
# print("----------------------------------------------")
# print('1          Rohan          12          M')
# print('2          ROHAN          12          M')
# print(" ")
# print("----------------------------------------------")
# print("\n Total Records Are: 2")

# # 3
# import mysql.connector
#
# def Delete():
#     mydb = mysql.connector.connect(host="localhost", user="root", passwd="dbxcbe", database="STUDENTDATABASE")
#     mycursor = mydb.cursor()
#     print("Database Connected.... Record view Facility")
#     r = input("Enter Regn No. to Delete the Record: ")
#     reg = (r, )
#     Q = "DELETE FROM STUDENT WHERE REGN = %s"
#     mycursor.execute(Q, reg)
#     mydb.commit()
#     print("Deletion completed")
# Delete()

# # 4
# import mysql.connector
#
# def Search():
#     mydb = mysql.connector.connect(host="localhost", user="root", passwd="dbxcbe", database="STUDENTDATABASE")
#     mycursor = mydb.cursor()
#     print ("Database Connected.... Record Search Facility")
#     r = input("Enter Regn No.: ")
#     reg = (r, )
#     Q = "SELECT * FROM STUDENT WHERE REGN = %s"
#     mycursor.execute(Q, reg)
#     res = mycursor.fetchall()
#     print("Details Are Given Bellow: ")
#     print("----------------------------------------------")
#     print('Regn       Name        Class       Gander')
#     print("----------------------------------------------")
#     f = 1
#     for x in res:
#         print(x[O], "\t", x[1], "\t\t", x[2], "\t", x[3])
#         f = 1
#     if f == 0:
#         print("Record Not Available")
#     else:
#         print("Total Records Are: 1")
# Search()

# # 5
# import mysql.connector
#
# def Update():
#     mydb = mysql.connector.connect(host="localhost", user="root", passwd="dbxcbe", database="STUDENTDATABASE")
#     mycursor = mydb.cursor()
#     print ("Database Connected.... Record Search Facility")
#     L = []
#     reg = input("Enter Regn No.: ")
#     L.append(reg)
#     nm = input("Enter New Name: ")
#     L.append (rum)
#     cl = int(input("Enter New Class: "))
#     L.append(cl)
#     gen = input("Enter New Gender (M/F): ")
#     L.append(gen)
#     R = L
#     Q = "UPDATE STUDENT SET NAME = %s, CLASS = %s, GENDER = %s, WHERE REGN = %s"
#     mycursor.execute(Q, R)
#     mydb.commit()
#     Q = "SELECT * FROM STUDENT"
#     mycursor.execute(Q)
#     res = mycursor.fetchall()
#     print("Details Are Given Bellow: ")
#     print("----------------------------------------------")
#     print('Regn       Name        Class       Gander')
#     print("----------------------------------------------")
#     for x in res:
#         print(x[O], "\t", x[1], "\t\t", x[2], "\t", x[3])
# Update()