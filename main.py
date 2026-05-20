import tkinter as tk
import os

# --- BRAND GUIDELINES (STRICT) ---
PURPLE = "#490D52"
PLUM = "#0D030E"
YELLOW = "#FFC815"
OFFWHITE = "#F7F7F7"
SMOKE = "#C0C0C0"
WHITE = "#FFFFFF"

# Gets the absolute path so the image is guaranteed to be found
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(BASE_DIR, "Unity Logo.png")

class UnityApp(tk.Tk):
    def __init__(self):
        """Master Application Class. Fulfills OOP requirement."""
        super().__init__()
        
        # 1. WINDOW SETUP (Strict 800x450)
        self.geometry("800x450")
        self.configure(bg=OFFWHITE)
        self.overrideredirect(True) # Hides OS title bar
        self.center_window()
        
        # 2. CUSTOM PURPLE TITLE BAR
        self.title_bar = tk.Frame(self, bg=PURPLE, height=30)
        self.title_bar.pack(fill="x", side="top")
        
        self.close_btn = tk.Button(self.title_bar, text="✕", bg=PURPLE, fg=WHITE, 
                                   activebackground="#e81123", activeforeground=WHITE,
                                   bd=0, font=("Arial", 12), command=self.destroy)
        self.close_btn.pack(side="right", padx=10)

        # 3. SCREEN CONTAINER
        self.container = tk.Frame(self, bg=OFFWHITE)
        self.container.pack(fill="both", expand=True)
        
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        # 4. MEMORY SAFE IMAGE LOADING
        self.images = {}
        self.load_images()
        
        self.frames = {}
        self.build_frames()

    def load_images(self):
        """Locks images in memory so Tkinter doesn't accidentally delete them."""
        try:
            self.images["logo"] = tk.PhotoImage(file=LOGO_PATH)
            self.images["logo_small"] = tk.PhotoImage(file=LOGO_PATH).subsample(2, 2)
        except Exception as e:
            print(f"Failed to load image at {LOGO_PATH}: {e}")
            self.images["logo"] = None
            self.images["logo_small"] = None

    def build_frames(self):
        """Initializes and stacks all screens."""
        for F in (SplashScreen, LoginScreen, JoinScreen):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("SplashScreen")

    def show_frame(self, page_name):
        """Brings specific frame to front."""
        frame = self.frames[page_name]
        frame.tkraise()

    def center_window(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (800 // 2)
        y = (self.winfo_screenheight() // 2) - (450 // 2)
        self.geometry(f'800x450+{x}+{y}')

# ==========================================
# SCREEN: SPLASH
# ==========================================
class SplashScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=OFFWHITE)
        self.controller = controller
        
        # BULLETPROOF CENTERING
        wrapper = tk.Frame(self, bg=OFFWHITE)
        wrapper.pack(expand=True)
        
        # Check if the image loaded successfully
        if controller.images["logo"]:
            tk.Label(wrapper, image=controller.images["logo"], bg=OFFWHITE).pack(pady=(0, 10))
        else:
            tk.Label(wrapper, text="UNITY APP", font=("Arial", 40, "bold"), bg=OFFWHITE, fg=PURPLE).pack(pady=(0, 10))
            
        tk.Label(wrapper, text='"Peace starts from sharing"', font=("Arial", 16, "italic"), bg=OFFWHITE, fg=PLUM).pack()
        
        self.after(3000, lambda: controller.show_frame("LoginScreen"))

# ==========================================
# SCREEN: LOGIN
# ==========================================
class LoginScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=OFFWHITE)
        self.controller = controller
        
        wrapper = tk.Frame(self, bg=OFFWHITE)
        wrapper.pack(expand=True)
        
        if controller.images["logo_small"]:
            tk.Label(wrapper, image=controller.images["logo_small"], bg=OFFWHITE).pack()
        
        tk.Label(wrapper, text='"Peace starts from sharing"', font=("Arial", 11, "italic"), bg=OFFWHITE, fg=PLUM).pack(pady=(0, 15))

        card = tk.Frame(wrapper, bg=WHITE, highlightbackground=PLUM, highlightthickness=2, padx=40, pady=25)
        card.pack()

        tk.Label(card, text="Username:", font=("Arial", 10, "bold"), bg=WHITE, fg=PURPLE).pack(anchor="w")
        user_ent = tk.Entry(card, width=32, bd=1, relief="solid", highlightbackground=SMOKE, font=("Arial", 11))
        user_ent.pack(pady=(2, 12), ipady=5)

        tk.Label(card, text="Password:", font=("Arial", 10, "bold"), bg=WHITE, fg=PURPLE).pack(anchor="w")
        pass_ent = tk.Entry(card, width=32, bd=1, relief="solid", highlightbackground=SMOKE, show="*", font=("Arial", 11))
        pass_ent.pack(pady=(2, 18), ipady=5)

        login_btn = tk.Button(card, text="Login to Account", bg=YELLOW, fg=PLUM, font=("Arial", 11, "bold"),
                              bd=1, relief="solid", cursor="hand2", command=lambda: print("Login logic goes here"))
        login_btn.pack(fill="x", ipady=5, pady=(0, 10))

        link = tk.Label(card, text="Create New Account", font=("Arial", 9, "underline", "bold"), 
                 bg=WHITE, fg=PLUM, cursor="hand2")
        link.bind("<Button-1>", lambda e: controller.show_frame("JoinScreen"))
        link.pack()

# ==========================================
# SCREEN: JOIN
# ==========================================
class JoinScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=OFFWHITE)
        self.controller = controller

        header = tk.Frame(self, bg=OFFWHITE)
        header.pack(fill="x", padx=30, pady=(20, 0))
        
        tk.Button(header, text="←", bg=YELLOW, fg=PLUM, bd=1, relief="solid", font=("Arial", 14, "bold"),
                  width=3, cursor="hand2", command=lambda: controller.show_frame("LoginScreen")).pack(side="left")

        wrapper = tk.Frame(self, bg=OFFWHITE)
        wrapper.pack(expand=True)

        tk.Label(wrapper, text="Join Unity", font=("Arial", 22, "bold"), bg=OFFWHITE, fg=PLUM).pack(pady=(0, 15))

        card = tk.Frame(wrapper, bg=WHITE, highlightbackground=PLUM, highlightthickness=2, padx=40, pady=25)
        card.pack()

        for label_text in ["Choose Username:", "Password:", "Confirm Password:"]:
            tk.Label(card, text=label_text, font=("Arial", 10, "bold"), bg=WHITE, fg=PURPLE).pack(anchor="w")
            ent = tk.Entry(card, width=32, bd=1, relief="solid", highlightbackground=SMOKE, font=("Arial", 11))
            if "Password" in label_text:
                ent.config(show="*")
            ent.pack(pady=(2, 10), ipady=4)

        tk.Button(card, text="Register Account", bg=PURPLE, fg=WHITE, font=("Arial", 11, "bold"),
                  bd=1, relief="solid", cursor="hand2", command=lambda: controller.show_frame("LoginScreen")).pack(fill="x", ipady=5, pady=(10, 0))

if __name__ == "__main__":
    app = UnityApp()
    app.mainloop()