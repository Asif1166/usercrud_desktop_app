from tkinter import *
from tkinter import ttk
import sqlite3

class UserListFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        columns = ('Username', 'Full Name', 'Email', 'Phone Number', 'Is Admin')
        tree = ttk.Treeview(self, columns=columns, show='headings')
        tree.heading('Username', text='Username')
        tree.heading('Full Name', text='Full Name')
        tree.heading('Email', text='Email')
        tree.heading('Phone Number', text='Phone Number')
        tree.heading('Is Admin', text='Is Admin')

        tree.pack(fill=BOTH, expand=True)

        conn = sqlite3.connect('users.db')
        cur = conn.cursor()

        cur.execute('SELECT username, full_name, email, phone_number, is_admin FROM users')
        for row in cur.fetchall():
            tree.insert('', 'end', values=row)

        conn.close()
