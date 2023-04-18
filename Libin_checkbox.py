'''code to take teacher attendance'''
'''made by Rohan, modified and improved by his brother X_X'''

import customtkinter as ctk
# dictinory is saved in a json file
import json

root = ctk.CTk()
root.geometry("200x400")
root.title("Login")
ctk.set_default_color_theme("green")

checkBoxes = []

# get list of teachers
with open('Teachers.json', 'r') as file:
    getTeachers = json.load(file)
    
    Teachers = {}

    # get the checkbox output as true or false and mark the teacher present or absent
    def check_login(teacher, state):
        if state.get():
            Teachers[teacher] = 'Present'
        else:
            Teachers[teacher] = 'Absent'
        print("{teacher}: {state}".format(teacher=teacher, state=Teachers[teacher]))

    # create instance of checkbox for each teacher
    for teacher in getTeachers:
        
        Teachers[teacher] = 'Absent'
        
        teacher_state = ctk.BooleanVar()
        
        checkBoxes.append(ctk.CTkCheckBox(master=root, text=teacher, font=('Century Gothic', 12), variable=teacher_state,
                                command=lambda teacher=teacher, state=teacher_state: check_login(teacher, state)))

# pack all checkboxes
for checkbox in checkBoxes:
    checkbox.pack(padx=10, pady=10)

root.mainloop()

