import tkinter as tk
from auth import LoginScreen, JoinScreen
from aid import AidScreen
from learn import LearnScreen

class UnityApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x450")
        self.configure(bg="#F7F7F7")
        self.overrideredirect(True)
        self.container = tk.Frame(self, bg="#F7F7F7")
        self.container.pack(fill="both", expand=True)
        self.frames = {
            "Login": LoginScreen(self.container, self),
            "Join": JoinScreen(self.container, self),
            "Aid": AidScreen(self.container, self),
            "Learn": LearnScreen(self.container, self)
        }
        for f in self.frames.values(): f.grid(row=0, column=0, sticky="nsew")
        self.show("Login")

    def show(self, name): self.frames[name].tkraise()

if __name__ == "__main__":
    UnityApp().mainloop()