from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry('800x600')

        self.main_frame = Frame(self.root, padx=10, pady=10)
        self.main_frame.pack(expand=True, fill=BOTH)

        self.show_login()

    def switch_frame(self, new_frame_func):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        new_frame_func()

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
            if len(user) > 6 and user[6] == 1:  # Check if user is admin
                # messagebox.showinfo("Login Successful", "Welcome, Admin!")
                self.switch_frame(self.show_all_users)
            else:
                # messagebox.showinfo("Login Successful", "Welcome, " + user[3] + "!")
                self.switch_frame(lambda: self.show_user_data(user))
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
        
        conn.close()

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

    def show_user_data(self, user):
        columns = ('Username', 'Full Name', 'Email', 'Phone Number')
        tree = ttk.Treeview(self.main_frame, columns=columns, show='headings')
        tree.heading('Username', text='Username')
        tree.heading('Full Name', text='Full Name')
        tree.heading('Email', text='Email')
        tree.heading('Phone Number', text='Phone Number')

        tree.pack(fill=BOTH, expand=True)
        tree.insert('', 'end', values=(user[1], user[3], user[4], user[5]))

    def register(self):
        def save_registration():
            username = entry_new_username.get()
            password = entry_new_password.get()
            full_name = entry_full_name.get()
            email = entry_email.get()
            phone_number = entry_phone_number.get()
            
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
                self.switch_frame(self.show_login)
            except sqlite3.IntegrityError:
                messagebox.showerror("Registration Failed", "Username already exists.")
            
            conn.close()

        for widget in self.main_frame.winfo_children():
            widget.destroy()

        label_full_name = Label(self.main_frame, text="Full Name:", font=("Arial", 12))
        label_full_name.grid(row=0, column=0, padx=10, pady=5, sticky=E)
        entry_full_name = Entry(self.main_frame, font=("Arial", 12))
        entry_full_name.grid(row=0, column=1, padx=10, pady=5)

        label_email = Label(self.main_frame, text="Email:", font=("Arial", 12))
        label_email.grid(row=1, column=0, padx=10, pady=5, sticky=E)
        entry_email = Entry(self.main_frame, font=("Arial", 12))
        entry_email.grid(row=1, column=1, padx=10, pady=5)

        label_phone_number = Label(self.main_frame, text="Phone Number:", font=("Arial", 12))
        label_phone_number.grid(row=2, column=0, padx=10, pady=5, sticky=E)
        entry_phone_number = Entry(self.main_frame, font=("Arial", 12))
        entry_phone_number.grid(row=2, column=1, padx=10, pady=5)

        label_new_username = Label(self.main_frame, text="New Username:", font=("Arial", 12))
        label_new_username.grid(row=3, column=0, padx=10, pady=5, sticky=E)
        entry_new_username = Entry(self.main_frame, font=("Arial", 12))
        entry_new_username.grid(row=3, column=1, padx=10, pady=5)

        label_new_password = Label(self.main_frame, text="New Password:", font=("Arial", 12))
        label_new_password.grid(row=4, column=0, padx=10, pady=5, sticky=E)
        entry_new_password = Entry(self.main_frame, show="*", font=("Arial", 12))
        entry_new_password.grid(row=4, column=1, padx=10, pady=5)

        register_button = Button(self.main_frame, text="Register", command=save_registration, width=10, font=("Arial", 12), bg="green", fg="white")
        register_button.grid(row=5, column=0, columnspan=2, pady=10)

    def show_login(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        label_title = Label(self.main_frame, text="Login", font=("Arial", 20, "bold"))
        label_title.grid(row=0, column=0, columnspan=2, pady=20)

        label_username = Label(self.main_frame, text="Username:", font=("Arial", 14))
        label_username.grid(row=1, column=0, padx=10, pady=5, sticky=E)
        self.entry_username = Entry(self.main_frame, font=("Arial", 14))
        self.entry_username.grid(row=1, column=1, padx=10, pady=5)

        label_password = Label(self.main_frame, text="Password:", font=("Arial", 14))
        label_password.grid(row=2, column=0, padx=10, pady=5, sticky=E)
        self.entry_password = Entry(self.main_frame, show="*", font=("Arial", 14))
        self.entry_password.grid(row=2, column=1, padx=10, pady=5)

        login_button = Button(self.main_frame, text="Login", command=self.login, width=10, font=("Arial", 14, "bold"))
        login_button.grid(row=3, column=0, columnspan=2, pady=10)

        register_button_main = Button(self.main_frame, text="Register", command=lambda: self.switch_frame(self.register), width=10, font=("Arial", 14, "bold"))
        register_button_main.grid(row=4, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
