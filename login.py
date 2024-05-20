from tkinter import *
from tkinter import messagebox
import sqlite3

class LoginFrame(Frame):
    def __init__(self, parent, switch_frame, set_current_user):
        super().__init__(parent)
        self.switch_frame = switch_frame
        self.set_current_user = set_current_user
        self.create_widgets()

    def create_widgets(self):
        label_title = Label(self, text="Login", font=("Arial", 20, "bold"))
        label_title.grid(row=0, column=0, columnspan=2, pady=20)

        label_username = Label(self, text="Username:", font=("Arial", 14))
        label_username.grid(row=1, column=0, padx=10, pady=5, sticky=E)
        self.entry_username = Entry(self, font=("Arial", 14))
        self.entry_username.grid(row=1, column=1, padx=10, pady=5)

        label_password = Label(self, text="Password:", font=("Arial", 14))
        label_password.grid(row=2, column=0, padx=10, pady=5, sticky=E)
        self.entry_password = Entry(self, show="*", font=("Arial", 14))
        self.entry_password.grid(row=2, column=1, padx=10, pady=5)

        login_button = Button(self, text="Login", command=self.login, width=10, font=("Arial", 14, "bold"))
        login_button.grid(row=3, column=0, columnspan=2, pady=10)

        register_button = Button(self, text="Register", command=lambda: self.switch_frame('register'), width=10, font=("Arial", 14, "bold"))
        register_button.grid(row=4, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if not username or not password:
            messagebox.showerror("Login Failed", "Username and password cannot be empty.")
            return

        conn = sqlite3.connect('users.db')
        cur = conn.cursor()

        cur.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user = cur.fetchone()

        if user:
            self.set_current_user(user)
            if len(user) > 6 and user[6] == 1:  # Check if user is admin
                self.switch_frame('show_all_users', is_admin=True)
            else:
                self.switch_frame('show_account_info', is_admin=False)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

        conn.close()
