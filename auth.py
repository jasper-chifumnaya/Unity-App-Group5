import tkinter as tk
import csv
#Gift wrote this function which runs and displays the login screen when called by main
class LoginScreen(tk.Frame):
    def __init__(self, parent, ctrl):
        super().__init__(parent, bg="#F7F7F7")
        self.u = tk.Entry(self); self.u.pack(pady=5)
        self.p = tk.Entry(self, show="*"); self.p.pack(pady=5)
        tk.Button(self, text="LOGIN", bg="#490D52", fg="white", command=self.login).pack()
    def login(self):
        with open('users.csv', 'r') as f:
            for r in csv.reader(f):
                if r[0] == self.u.get() and r[1] == self.p.get():
                    Self.master.master.master.show("Aid")


#Anthony wrote this function which allows new users to create an account which is saved on users.csv

class JoinScreen(tk.Frame):
    def __init__(self, parent, ctrl):
        super().__init__(parent, bg="#F7F7F7")
        self.u = tk.Entry(self); self.u.pack()
        self.p = tk.Entry(self, show="*"); self.p.pack()
        tk.Button(self, text="REGISTER", bg="#490D52", fg="white", command=self.save).pack()
    def save(self):
        with open('users.csv', 'a', newline='') as f:
            csv.writer(f).writerow([self.u.get(), self.p.get()])
            self.master.master.master.show("Login")