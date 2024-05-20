from tkinter import *

class Sidebar(Frame):
    def __init__(self, parent, switch_frame):
        super().__init__(parent)
        self.parent = parent
        self.switch_frame = switch_frame

        self.configure(width=200, bg='#2E4053', relief='sunken', borderwidth=2)
        self.pack_forget()  # Initially hide the sidebar

        self.add_sidebar_button("Account Info", lambda: self.switch_frame('show_account_info'))
        self.add_sidebar_button("Add User", lambda: self.switch_frame('register'))
        self.add_sidebar_button("User List", lambda: self.switch_frame('show_all_users'))

    def add_sidebar_button(self, text, command):
        button = Button(self, text=text, command=command, font=("Arial", 12), bg="#4CAF50", fg="white")
        button.pack(padx=10, pady=10, fill='x')

    def hide(self):
        self.pack_forget()

    def show(self):
        self.pack(side=LEFT, fill=Y)
