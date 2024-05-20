    
import sqlite3
from tkinter import *

from tkinter import ttk
def show_all_users(self):
        columns = ('Username', 'Full Name', 'Email', 'Phone Number', 'Is Admin')
        tree = ttk.Treeview(self.main_frame, columns=columns, show='headings')
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