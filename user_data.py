from tkinter import *
from tkinter import ttk

class UserInfoFrame(Frame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.user = user
        self.create_widgets()

    def create_widgets(self):
        if self.user is None:
            Label(self, text="User data not found.", font=("Arial", 14)).pack(pady=20)
            return

        columns = ('Username', 'Full Name', 'Email', 'Phone Number')
        tree = ttk.Treeview(self, columns=columns, show='headings')
        tree.heading('Username', text='Username')
        tree.heading('Full Name', text='Full Name')
        tree.heading('Email', text='Email')
        tree.heading('Phone Number', text='Phone Number')

        tree.pack(fill=BOTH, expand=True)
        tree.insert('', 'end', values=(self.user[1], self.user[3], self.user[4], self.user[5]))
