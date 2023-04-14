# The login page for c.s project
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.geometry("1000x768")
# root.attributes('-fullscreen', True)

# login program
# if rl is false is runs the login program
def tab1():
    root.title("Login")

    label1 = tk.Label(root, text="Login", font=('Segoe Ui', 60))
    label1.pack(padx=20, pady=110)

    textbox1 = tk.Label(root, height=1, text="Username", font=('Segoe Ui', 20))
    textbox1.pack(padx=20)

    myentry1 = tk.Entry(root)
    myentry1.pack(padx=20, pady=10)

    textbox2 = tk.Label(root, height=1, text="Password", font=('Segoe Ui', 20))
    textbox2.pack(padx=20)

    str_va = tk.StringVar()

    myentry2 = tk.Entry(root, show='*', textvariable=str_va)
    myentry2.pack(padx=20, pady=10)

    c1_va = tk.IntVar(value=0)

    def my_show():
        if c1_va.get() != 0:
            myentry2.config(show='')
        else:
            myentry2.config(show='*')

    c1 = tk.Checkbutton(root, text="Show Password", font=('Segoe Ui', 11), variable=c1_va, onvalue=1, offvalue=0, command=my_show)
    c1.pack(padx=20, pady=10)

    check_state = tk.IntVar()

    def check_login():
        if check_state.get() == 1:
            fh = open('login remember.txt', 'w')
            str1 = "true"
            print(str1)
            fh.write(str1)
            fh.close()
        elif check_state.get() == 0:
            fh = open('login remember.txt', 'w')
            str2 = "false"
            print(str2)
            fh.write(str2)
            fh.close()

    check1 = tk.Checkbutton(root, text="Remember Me", font=('Segoe Ui', 11), variable=check_state, command=check_login)
    check1.pack(padx=10, pady=15)

    def destory_login():
        label1.destroy()
        textbox1.destroy()
        myentry1.destroy()
        textbox2.destroy()
        myentry2.destroy()
        c1.destroy()
        check1.destroy()
        cbutton1.destroy()
        _quit.destroy()
        t3.destroy()
        text_name.destroy()
        tab2()

    t3 = textbox3 = tk.Label(root, height=5, text="*Incorrect* \n *Username or Password*", font=('Segoe Ui', 13))

    def login_details():
        if myentry1.get() == "Admin" and myentry2.get() == "Admin123":
            destory_login()
        else:
            t3
            textbox3.pack(padx=20, )
            textbox3.place(relx=0.55, rely=0.5, anchor=tk.W)

    cbutton1 = tk.Button(root, text="Login", font=('Segoe Ui', 22), command=login_details)
    cbutton1.pack(padx=10, pady=30)

    _quit = tk.Button(root, text="Quit", font=('Segoe Ui', 10), command=root.destroy)
    _quit.pack(pady=60)
    _quit.place(relx=0.95, rely=0.95, anchor=tk.NW)

    name = "The Mallus"
    text_name = tk.Label(root, height=5, text=name, font=('Segoe Ui', 13))
    text_name.pack(padx=0, pady=0)
    text_name.place(relx=0.065, rely=0.91, anchor=tk.NE)

# program lobby
# if rl is true it skips login and runs the program
def tab2():
    root.title("Time Management System")

    def logout():
        fh = open('login remember.txt', 'w')
        str2 = "false"
        print(str2)
        fh.write(str2)
        fh.close()
        view_button.destroy()
        add_button.destroy()
        sub_button.destroy()
        label1.destroy()
        logout1.destroy()
        _quit.destroy()
        tab1()

    def destroy_tab2():
        view_button.destroy()
        add_button.destroy()
        sub_button.destroy()
        label1.destroy()
        logout1.destroy()
        text_name.destroy()
        _quit.destroy()

    label1 = tk.Label(root, text="Time Management System", font=('Segoe Ui', 35))
    label1.pack(padx=20, pady=100)

    def button_view():
        destroy_tab2()
        tabview()

    def button_add():
        destroy_tab2()
        tabadd()

    def button_sub():
        destroy_tab2()
        tabsub()

    view_button = tk.Button(root, text="View Timetable", font=('Segoe Ui', 30), command=button_view)
    view_button.pack(padx=10, pady=30)

    add_button = tk.Button(root, text="Manage Timetables", font=('Segoe Ui', 30), command=button_add)
    add_button.pack(padx=10, pady=30)

    sub_button = tk.Button(root, text="Substitute Absent Teachers", font=('Segoe Ui', 30), command=button_sub)
    sub_button.pack(padx=10, pady=30)

    logout1 = tk.Button(root, text="Logout", font=('Segoe Ui', 10), command=logout)
    logout1.pack(padx=10, pady=10)
    logout1.place(relx=0.95, rely=0.91, anchor=tk.NW)

    _quit = tk.Button(root, text="Quit", font=('Segoe Ui', 10), command=root.destroy)
    _quit.pack(pady=60)
    _quit.place(relx=0.95, rely=0.95, anchor=tk.NW)

    name = "The Mallus"
    text_name = tk.Label(root, height=5, text=name, font=('Segoe Ui', 13))
    text_name.pack(padx=0, pady=0)
    text_name.place(relx=0.065, rely=0.91, anchor=tk.NE)

# to view the timetable
def tabview():
    root.title("View Timetable")

    view_label = tk.Label(root, text="View Timetable", font=('Segoe Ui', 35))
    view_label.pack(padx=20, pady=100)

    wip_label = tk.Label(root, text="Work in progress", font=('Segoe Ui', 35))
    wip_label.pack(padx=20, pady=100)

    name = "The Mallus"
    text_name = tk.Label(root, height=5, text=name, font=('Segoe Ui', 13))
    text_name.pack(padx=0, pady=0)
    text_name.place(relx=0.065, rely=0.91, anchor=tk.NE)

    def _back():
        view_label.destroy()
        view_back.destroy()
        text_name.destroy()
        wip_label.destroy()
        tab2()

    view_back = tk.Button(root, text="Back", font=('Segoe Ui', 10), command=_back)
    view_back.pack(pady=60)
    view_back.place(relx=0.95, rely=0.95, anchor=tk.NW)

# to manage timetables
def tabadd():
    root.title("Manage Timetables")

    add_label = tk.Label(root, text="Manage Timetables", font=('Segoe Ui', 35))
    add_label.pack(padx=20, pady=100)

    wip_label = tk.Label(root, text="Work in progress", font=('Segoe Ui', 35))
    wip_label.pack(padx=20, pady=100)

    wip_label2 = tk.Label(root, text="will be added later on...", font=('Segoe Ui', 20))
    wip_label2.pack(padx=20, pady=10)

    name = "The Mallus"
    text_name = tk.Label(root, height=5, text=name, font=('Segoe Ui', 13))
    text_name.pack(padx=0, pady=0)
    text_name.place(relx=0.065, rely=0.91, anchor=tk.NE)

    def _back():
        add_label.destroy()
        add_back.destroy()
        wip_label.destroy()
        wip_label2.destroy()
        text_name.destroy()
        tab2()

    add_back = tk.Button(root, text="Back", font=('Segoe Ui', 10), command=_back)
    add_back.pack(pady=60)
    add_back.place(relx=0.95, rely=0.95, anchor=tk.NW)

# to substitute absent teachers
def tabsub():
    root.title("Substitute Absent Teachers")

    sub_label = tk.Label(root, text="Substitute Absent Teachers", font=('Segoe Ui', 35))
    sub_label.pack(padx=20, pady=100)

    wip_label = tk.Label(root, text="Work in progress", font=('Segoe Ui', 35))
    wip_label.pack(padx=20, pady=100)

    name = "The Mallus"
    text_name = tk.Label(root, height=5, text=name, font=('Segoe Ui', 13))
    text_name.pack(padx=0, pady=0)
    text_name.place(relx=0.065, rely=0.91, anchor=tk.NE)

    def _back():
        sub_label.destroy()
        sub_back.destroy()
        wip_label.destroy()
        text_name.destroy()
        tab2()

    sub_back = tk.Button(root, text="Back", font=('Segoe Ui', 10), command=_back)
    sub_back.pack(pady=60)
    sub_back.place(relx=0.95, rely=0.95, anchor=tk.NW)

# to check login
def login():
    fp = open('login remember.txt', 'r')
    rl = fp.read()
    if rl == "false":
        tab1()
    else:
        tab2()

# starting of the program
def starting():
    root.title("Time Management System")

    heading = tk.Label(root, text="Time Management System", font=('Segoe Ui', 45))
    heading.pack(padx=10, pady=10)
    heading.place(relx=0.5, rely=0.08, anchor=tk.N)

    heading2 = tk.Label(root, text="Helps you manage your timetables :)", font=('Segoe Ui', 12))
    heading2.pack(padx=10, pady=10)
    heading2.place(relx=0.5, rely=0.2, anchor=tk.N)

    team = "By: The Mallus"
    members = tk.Label(root, text=team, font=('Segoe Ui', 24))
    members.pack(padx=10, pady=10)
    members.place(relx=0.5, rely=0.86, anchor=tk.S)
    name = "Rohan & Libin"
    members2 = tk.Label(root, text=name, font=('Segoe Ui', 17))
    members2.pack(padx=10, pady=10)
    members2.place(relx=0.5, rely=0.9, anchor=tk.S)

    def enter_program():
        heading.destroy()
        heading2.destroy()
        members.destroy()
        members2.destroy()
        ebutton.destroy()
        _quit.destroy()
        login()

    ebutton = tk.Button(root, text="Enter", font=('Segoe Ui', 22), command=enter_program)
    ebutton.pack()
    ebutton.place(relx=0.5, rely=0.52, anchor=tk.S)

    _quit = tk.Button(root, text="Quit", font=('Segoe Ui', 22), command=root.destroy)
    _quit.pack(padx=10, pady=10)
    _quit.place(relx=0.5, rely=0.52, anchor=tk.N)

starting()

root.mainloop()
