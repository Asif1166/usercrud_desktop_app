from tkinter import *
from tkinter import messagebox
import sqlite3

class RegisterFrame(Frame):
    def __init__(self, parent, switch_frame):
        super().__init__(parent)
        self.switch_frame = switch_frame
        self.create_widgets()

    def create_widgets(self):
        label_full_name = Label(self, text="Full Name:", font=("Arial", 12))
        label_full_name.grid(row=0, column=0, padx=10, pady=5, sticky=E)
        self.entry_full_name = Entry(self, font=("Arial", 12))
        self.entry_full_name.grid(row=0, column=1, padx=10, pady=5)

        label_email = Label(self, text="Email:", font=("Arial", 12))
        label_email.grid(row=1, column=0, padx=10, pady=5, sticky=E)
        self.entry_email = Entry(self, font=("Arial", 12))
        self.entry_email.grid(row=1, column=1, padx=10, pady=5)

        label_phone_number = Label(self, text="Phone Number:", font=("Arial", 12))
        label_phone_number.grid(row=2, column=0, padx=10, pady=5, sticky=E)
        self.entry_phone_number = Entry(self, font=("Arial", 12))
        self.entry_phone_number.grid(row=2, column=1, padx=10, pady=5)

        label_new_username = Label(self, text="New Username:", font=("Arial", 12))
        label_new_username.grid(row=3, column=0, padx=10, pady=5, sticky=E)
        self.entry_new_username = Entry(self, font=("Arial", 12))
        self.entry_new_username.grid(row=3, column=1, padx=10, pady=5)

        label_new_password = Label(self, text="New Password:", font=("Arial", 12))
        label_new_password.grid(row=4, column=0, padx=10, pady=5, sticky=E)
        self.entry_new_password = Entry(self, show="*", font=("Arial", 12))
        self.entry_new_password.grid(row=4, column=1, padx=10, pady=5)

        register_button = Button(self, text="Register", command=self.save_registration, width=10, font=("Arial", 12), bg="green", fg="white")
        register_button.grid(row=5, column=0, columnspan=2, pady=10)

    def save_registration(self):
        username = self.entry_new_username.get()
        password = self.entry_new_password.get()
        full_name = self.entry_full_name.get()
        email = self.entry_email.get()
        phone_number = self.entry_phone_number.get()

        if not username or not password or not full_name or not email or not phone_number:
            messagebox.showerror("Registration Failed", "All fields are required.")
            return

        conn = sqlite3.connect('users.db')
        cur = conn.cursor()

        try:
            cur.execute('INSERT INTO users (username, password, full_name, email, phone_number, is_admin) VALUES (?, ?, ?, ?, ?, ?)', 
                        (username, password, full_name, email, phone_number, 0))
            conn.commit()
            messagebox.showinfo("Registration Successful", "User registered successfully!")
            self.switch_frame('show_login')
        except sqlite3.IntegrityError:
            messagebox.showerror("Registration Failed", "Username already exists.")

        conn.close()
