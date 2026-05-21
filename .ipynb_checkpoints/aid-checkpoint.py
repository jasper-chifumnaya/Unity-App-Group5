import tkinter as tk
//It processe donations
class AidScreen(tk.Frame):
    def __init__(self, parent, ctrl):
        super().__init__(parent, bg="#F7F7F7")
        self.amt = tk.Entry(self); self.amt.pack(pady=10)
        tk.Button(self, text="Donate Cash", bg="#FFC815", command=self.add).pack()
    def add(self):
        with open('donations.csv', 'a', newline='') as f:
            csv.writer(f).writerow([self.amt.get(), "Donation"])