# learning gui 1

# import tkinter as tk
# root = tk.Tk()
#
# root.geometry("800x500")   # ---> the size of the window
# root.title("A Simple GUI")  # ---> the title
#
# label = tk.Label(root, text="A Simple GUI", font=('Arial', 18))  # ---> to add a label
# label.pack(padx=20, pady=20)
#
# textbox = tk.Text(root, height=5, font=('Arial', 16))   # ---> to add a textbox
# textbox.pack(padx=10)
#
# myentry = tk.Entry(root)  # ---> to add an entry textbox
# myentry.pack(padx=10, pady=10)
#
# button = tk.Button(root, text="Enter", font=('Arial', 18))  # ---> to add a button
# button.pack(padx=10, pady=10)
#
# buttonframe = tk.Frame(root)  # ---> to make a grid of buttons *
# buttonframe.columnconfigure(0, weight=1)
# buttonframe.columnconfigure(1, weight=1)
# buttonframe.columnconfigure(2, weight=1)
#
# btn1 = tk.Button(buttonframe, text='1', font=('Arial', 18))
# btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
#
# btn2 = tk.Button(buttonframe, text='2', font=('Arial', 18))
# btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
#
# btn3 = tk.Button(buttonframe, text='3', font=('Arial', 18))
# btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
#
# btn4 = tk.Button(buttonframe, text='4', font=('Arial', 18))
# btn4.grid(row=1, column=0, sticky=tk.W+tk.E)
#
# btn5 = tk.Button(buttonframe, text='5', font=('Arial', 18))
# btn5.grid(row=1, column=1, sticky=tk.W+tk.E)
#
# btn6 = tk.Button(buttonframe, text='6', font=('Arial', 18))
# btn6.grid(row=1, column=2, sticky=tk.W+tk.E)
#
# buttonframe.pack(fill='x', padx=20, pady=20)  # ---> to make a grid of buttons **
#
# root.mainloop()

# learning gui 2

# import tkinter as tk
# from tkinter import messagebox
#
# class MyGUI:   # ---> making a class
#
#     def __init__(self):
#
#         self.root = tk.Tk()
#
#         self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
#         self.label.pack(padx=10, pady=10)
#
#         self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
#         # self.textbox.bind("<KeyPress>", self.shortcut())  ---> to map a key for a function
#         self.textbox.pack(padx=10, pady=10)
#
#         self.check_state = tk.IntVar()  # ---> to check integer
#
#         self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 16), variable=self.check_state)
#         self.check.pack(padx=10, pady=10)  # ---> to make a checkbox
#
#         self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command=self.show_message)
#         self.button.pack(padx=10, pady=10)
#
#         self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # ---> quit conformation
#         self.root.mainloop()
#
#     def show_message(self):
#         if self.check_state.get() == 0:  # ---> to check if the checkbox is checked or not
#             print(self.textbox.get('1.0', tk.END))   # ---> check box unchecked nothing happens
#         else:
#             messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))   # ---> check box is checked
#                                                                                                  # message is shown
#
#     # def shortcut(self, event):
#     #     if event.state == 12 and event.keysym == "Return":
#     #         self.show_message()  # ---> to map a key for a function
#
#     def on_closing(self):
#         if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
#             self.root.destroy()  # ---> quit conformation
#
# MyGUI()

# button check program

# import tkinter as tk
#
# root = tk.Tk()
#
# root.geometry("200x100")
# root.title("Login")
#
# check_state = tk.IntVar()
#
# def check_login():
#     if check_state.get() == 1:
#         print("true")
#     elif check_state.get() == 0:
#         print("false")
#
# check1 = tk.Checkbutton(root, text="Remember Me", font=('Arial', 16), variable=check_state, command=check_login)
# check1.pack(padx=10, pady=10)
#
# root.mainloop()


# user profile
# import customtkinter as ctk
# from PIL import ImageTk
# from PIL import Image
#
# root = ctk.CTk()
#
# ctk.set_appearance_mode("system")
# ctk.set_default_color_theme("green")
#
# root.overrideredirect(True)
# root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
#
# frame = ctk.CTkFrame(master=root, corner_radius=15)
# frame.pack(fill="both", expand=True)
#
# def account():
#
#     is_dropdown_open = False
#
#     user_image = ctk.CTkImage(Image.open("User.png"), size=(32, 32))
#
#     acc_frame_margin = 16
#     acc_frame_padding = 8
#
#     acc_frame = ctk.CTkFrame(master=frame, height=45, corner_radius=10, fg_color="#383838")
#     acc_frame.pack(side=ctk.TOP, anchor=ctk.E, padx=acc_frame_margin, pady=acc_frame_margin)
#
#     dropdown_frame = ctk.CTkFrame(master=frame, corner_radius=15, fg_color="#383838")
#
#     def open_settings():
#         settings_frame = ctk.CTkFrame(master=frame, corner_radius=15)
#         settings_frame.pack(fill="both", expand=True)
#
#         settings_1 = ctk.CTkFrame(master=settings_frame, corner_radius=30)
#         settings_1.pack(pady=60, padx=550, fill="both", expand=True)
#
#         settings_label = ctk.CTkLabel(master=settings_1, text="Settings", font=('Segoe Ui', 55))
#         settings_label.pack(padx=10, pady=12)
#         settings_label.place(relx=0.5, rely=0.08, anchor=ctk.N)
#
#         def change_appearance_mode_event(new_appearance_mode: str):
#             ctk.set_appearance_mode(new_appearance_mode)
#             fa = open("appearance.txt", "w")
#             fa.write(new_appearance_mode)
#             fa.close()
#
#         appearance_mode_label = ctk.CTkLabel(master=settings_1, text="Appearance Mode:", font=('Segoe Ui', 20))
#         appearance_mode_label.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)
#         appearance_mode_option = ctk.CTkOptionMenu(settings_1, values=["Dark", "Light", "System"],
#                                                    command=change_appearance_mode_event, font=('Segoe Ui', 15))
#         appearance_mode_option.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)
#
#         def change_scaling_event(new_scaling: str):
#             new_scaling_float = int(new_scaling.replace("%", "")) / 100
#             ctk.set_widget_scaling(new_scaling_float)
#             fs = open('Scale.txt', 'w')
#             n_scaling = new_scaling.replace("%", "")
#             fs.write(n_scaling)
#             fs.close()
#
#         scaling_label = ctk.CTkLabel(master=settings_1, text="UI Scaling:", font=('Segoe Ui', 20))
#         scaling_label.place(relx=0.5, rely=0.55, anchor=ctk.CENTER)
#         scaling_option = ctk.CTkOptionMenu(master=settings_1, values=["100%", "110%", "120%"],
#                                            command=change_scaling_event, font=('Segoe Ui', 15))
#         scaling_option.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)
#
#         def destroy_settings():
#             settings_frame.destroy()
#             settings_1.destroy()
#             settings_label.destroy()
#             appearance_mode_label.destroy()
#             appearance_mode_option.destroy()
#             scaling_label.destroy()
#             scaling_option.destroy()
#             _save.destroy()
#
#         _save = ctk.CTkButton(master=settings_1, text="Save", font=('Segoe Ui', 15), command=destroy_settings)
#         _save.pack(padx=10, pady=12)
#         _save.place(relx=0.5, rely=0.8, anchor=ctk.CENTER)
#
#     def logout():
#         fh = open('login remember teach.txt', 'w')
#         str2 = "false"
#         print(str2)
#         fh.write(str2)
#         fh.close()
#         destroy_tab2()
#         tab1()
#         destroy_dropdown(True)
#
#     def destroy_tab2():
#         label1.destroy()
#         view_button.destroy()
#         sub_button.destroy()
#         man_button.destroy()
#         dropdown_frame.destroy()
#
#     settings_button = ctk.CTkButton(master=dropdown_frame, text="Settings", font=('Segoe Ui', 15), command=open_settings)
#
#     logout1 = ctk.CTkButton(master=dropdown_frame, text="Logout", font=('Segoe Ui', 15), command=logout)
#
#     _quit = ctk.CTkButton(master=dropdown_frame, text="Quit", font=('Segoe Ui', 15), command=exit)
#
#     def place_dropdown():
#         dropdown_frame.pack(side=ctk.TOP, anchor=ctk.NE, padx=acc_frame_margin)
#
#         settings_button.pack(padx=10, pady=10)
#         logout1.pack(padx=10)
#         _quit.pack(padx=10, pady=10)
#
#     def destroy_dropdown(do_logout=False):
#         dropdown_frame.pack_forget()
#         if do_logout:
#             acc_frame.pack_forget()
#
#     def toggle_dropdown():
#         nonlocal is_dropdown_open
#         destroy_dropdown() if is_dropdown_open else place_dropdown()
#         is_dropdown_open = not is_dropdown_open
#
#     # user_icon = ctk.CTkLabel(master=acc_frame, text="", image=user_image)
#     # user_icon.pack(side=ctk.LEFT, padx=acc_frame_padding)
#
#     user_button = ctk.CTkButton(master=acc_frame, image=user_image, text="  Teacher", font=('Segoe Ui', 18), fg_color="#383838", hover_color="#383838",
#                                 command=toggle_dropdown, anchor="w", compound="left")
#     user_button.pack(padx=acc_frame_padding, pady=acc_frame_padding)
#
# account()
#
# root.mainloop()


