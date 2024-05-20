from tkinter import *
from sidebar import Sidebar
from login import LoginFrame
from registration import RegisterFrame
from user_list import UserListFrame
from user_data import UserInfoFrame

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry('800x600')

        self.main_frame = Frame(self.root, padx=10, pady=10)
        self.main_frame.pack(expand=True, fill=BOTH, side=RIGHT)

        self.sidebar = Sidebar(self.root, self.switch_frame)
        self.sidebar.hide()  # Initially hide the sidebar

        self.current_user = None  # To store logged-in user data
        self.is_admin = False  # To track if the current user is an admin

        self.show_login()

    def switch_frame(self, frame_name, is_admin=None):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        if is_admin is not None:
            self.is_admin = is_admin
        
        if self.is_admin:
            self.sidebar.show()
        else:
            self.sidebar.hide()

        if frame_name == 'show_account_info':
            frame = UserInfoFrame(self.main_frame, self.current_user)
            frame.pack(expand=True, fill=BOTH)
        elif frame_name == 'register':
            frame = RegisterFrame(self.main_frame, self.switch_frame)
            frame.pack(expand=True, fill=BOTH)
        elif frame_name == 'show_all_users':
            frame = UserListFrame(self.main_frame)
            frame.pack(expand=True, fill=BOTH)
        elif frame_name == 'show_login':
            frame = LoginFrame(self.main_frame, self.switch_frame, self.set_current_user)
            frame.pack(expand=True, fill=BOTH)

    def set_current_user(self, user):
        self.current_user = user

    def show_login(self):
        self.switch_frame('show_login', is_admin=False)

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
