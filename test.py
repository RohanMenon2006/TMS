import tkinter as tk


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":
        username_label.destroy()
        username_entry.destroy()
        password_entry.destroy()
        password_label.destroy()
        login_button.destroy()
        error_label.destroy()
        open_main_page()
    else:
        error_label.config(text="Invalid username or password")

def open_main_page():

    title_label = tk.Label(frame1, text="Student Voting System", font=("Arial", 20, "bold"))
    title_label.pack(pady=20)

    def destroy_main():
        title_label.destroy()
        headboy_button.destroy()
        headgirl_button.destroy()
        lca_button.destroy()
        joint_lca_button.destroy()
        open_candidate_page()

    headboy_button = tk.Button(frame1, text="Head Boy", command=destroy_main, width=15, height=3)
    headboy_button.pack(pady=10)

    headgirl_button = tk.Button(frame1, text="Head Girl", command=destroy_main, width=15, height=3)
    headgirl_button.pack(pady=10)

    lca_button = tk.Button(frame1, text="LCA", command=destroy_main, width=15, height=3)
    lca_button.pack(pady=10)

    joint_lca_button = tk.Button(frame1, text="Joint LCA", command=destroy_main, width=15, height=3)
    joint_lca_button.pack(pady=10)


def open_candidate_page():

    candidate1_button = tk.Button(frame1, text="Candidate 1", command=cast_vote, width=15, height=3)
    candidate1_button.pack(pady=10)

    candidate2_button = tk.Button(frame1, text="Candidate 2", command=cast_vote, width=15, height=3)
    candidate2_button.pack(pady=10)

    candidate3_button = tk.Button(frame1, text="Candidate 3", command=cast_vote, width=15, height=3)
    candidate3_button.pack(pady=10)

    candidate4_button = tk.Button(frame1, text="Candidate 4", command=cast_vote, width=15, height=3)
    candidate4_button.pack(pady=10)

def cast_vote():

    message_label.config(text="Vote casted successfully!")



root = tk.Tk()
root.title("Student Voting System")
root.geometry("600x600")


frame1 = tk.Frame(root, width=600, height=600)
frame1.pack()


username_label = tk.Label(frame1, text="Username:")
username_label.pack()

username_entry = tk.Entry(frame1)
username_entry.pack()

password_label = tk.Label(frame1, text="Password:")
password_label.pack()

password_entry = tk.Entry(frame1, show="*")
password_entry.pack()


login_button = tk.Button(frame1, text="Login", command=login, width=10, height=2)
login_button.pack(pady=10)


error_label = tk.Label(frame1, fg="red")
error_label.pack()


message_label = tk.Label(root, fg="green")
message_label.pack()


root.mainloop()


