import tkinter as tk
from tkinter import messagebox
import random

# --- Ρυθμίσεις Παιχνιδιού ---
ROWS, COLS = 3, 3
axia_symbolwn = {
    "💎": 50, 
    "🍎": 20, 
    "🔔": 10, 
    "🍒": 5   
}
emfanisi_symbolwn = {"💎": 2, "🍎": 4, "🔔": 6, "🍒": 8}

class CasinoPro:
    def __init__(self, root):
        self.root = root
        self.root.title("Golden Slots Pro 🎰")
        self.root.geometry("600x850")
        self.root.configure(bg="#0a0a0a")

        self.ypoloipo = 0
        self.setup_ui()

    def setup_ui(self):
        # --- Τίτλος ---
        tk.Label(self.root, text="V I P  S L O T S", font=("Impact", 35), 
                 fg="#FFD700", bg="#0a0a0a").pack(pady=10)

        # --- Πίνακας Κερδών ---
        paytable_frame = tk.Frame(self.root, bg="#1a1a1a", bd=2, relief="groove")
        paytable_frame.pack(pady=5, padx=20, fill="x")
        
        tk.Label(paytable_frame, text="ΠΙΝΑΚΑΣ ΚΕΡΔΩΝ (Multiplier x Bet)", 
                 font=("Arial", 10, "bold"), fg="#FFD700", bg="#1a1a1a").pack()
        
        grid_pay = tk.Frame(paytable_frame, bg="#1a1a1a")
        grid_pay.pack(pady=5)
        
        col_idx = 0
        for sym, val in axia_symbolwn.items():
            tk.Label(grid_pay, text=f"{sym}: x{val}", font=("Arial", 12, "bold"), 
                     fg="white", bg="#1a1a1a", padx=10).grid(row=0, column=col_idx)
            col_idx += 1

        # --- Υπόλοιπο ---
        self.label_ypoloipo = tk.Label(self.root, text=f"BALANCE: ${self.ypoloipo}", 
                                       font=("Consolas", 25, "bold"), fg="#00FFCC", 
                                       bg="#111", width=18, bd=3, relief="sunken")
        self.label_ypoloipo.pack(pady=10)

        # --- Slots Frame ---
        self.outer_reels = tk.Frame(self.root, bg="#FFD700", padx=5, pady=5)
        self.outer_reels.pack(pady=15)

        self.inner_reels = tk.Frame(self.outer_reels, bg="black")
        self.inner_reels.pack()

        self.labels = []
        for r in range(ROWS):
            row_lbls = []
            for c in range(COLS):
                lbl = tk.Label(self.inner_reels, text="✨", font=("Arial", 40), 
                               width=3, bg="#1a1a1a", fg="white", bd=1, relief="flat")
                lbl.grid(row=r, column=c, padx=2, pady=2)
                row_lbls.append(lbl)
            self.labels.append(row_lbls)

        # --- Control Panel ---
        ctrl_frame = tk.Frame(self.root, bg="#0a0a0a")
        ctrl_frame.pack(pady=10)

        s = {"font": ("Arial", 10, "bold"), "fg": "#aaa", "bg": "#0a0a0a"}
        e = {"font": ("Arial", 14, "bold"), "bg": "#222", "fg": "white", "justify": "center"}

        tk.Label(ctrl_frame, text="ΚΑΤΑΘΕΣΗ", **s).grid(row=0, column=0)
        self.in_dep = tk.Entry(ctrl_frame, width=8, **e)
        self.in_dep.grid(row=1, column=0, padx=10)
        tk.Button(ctrl_frame, text="ADD", command=self.add_money, bg="#2ecc71", fg="black").grid(row=2, column=0, pady=5)

        tk.Label(ctrl_frame, text="ΓΡΑΜΜΕΣ (1-3)", **s).grid(row=0, column=1)
        self.in_lines = tk.Entry(ctrl_frame, width=5, **e)
        self.in_lines.insert(0, "3")
        self.in_lines.grid(row=1, column=1, padx=10)

        tk.Label(ctrl_frame, text="BET / LINE", **s).grid(row=0, column=2)
        self.in_bet = tk.Entry(ctrl_frame, width=8, **e)
        self.in_bet.insert(0, "10")
        self.in_bet.grid(row=1, column=2, padx=10)

        self.btn_spin = tk.Button(self.root, text="S P I N 🎰", font=("Arial", 24, "bold"), 
                                  bg="#e74c3c", fg="white", command=self.spin, 
                                  width=12, cursor="hand2")
        self.btn_spin.pack(pady=15)

        self.status = tk.Label(self.root, text="ΚΑΛΩΣΗΡΘΕΣ! ΒΑΛΕ ΛΕΦΤΑ ΚΑΙ ΠΑΙΞΕ.", 
                               font=("Arial", 11), fg="#FFD700", bg="#0a0a0a")
        self.status.pack()

    def add_money(self):
        val = self.in_dep.get()
        if val.isdigit() and int(val) > 0:
            self.ypoloipo += int(val)
            self.label_ypoloipo.config(text=f"BALANCE: ${self.ypoloipo}")
            self.status.config(text="Η κατάθεση έγινε!", fg="#2ecc71")
        else:
            messagebox.showerror("Λάθος", "Βάλε ένα σωστό ποσό!")

    def spin(self):
        try:
            lines = int(self.in_lines.get())
            bet = int(self.in_bet.get())
        except ValueError:
            messagebox.showwarning("Προσοχή", "Δώσε αριθμούς!")
            return

        total = lines * bet
        if not (1 <= lines <= 3):
            messagebox.showwarning("Γραμμές", "Διάλεξε 1 έως 3 γραμμές!")
            return
        if total > self.ypoloipo:
            messagebox.showwarning("Υπόλοιπο", "Δεν έχεις αρκετά λεφτά!")
            return

        self.ypoloipo -= total
        self.label_ypoloipo.config(text=f"BALANCE: ${self.ypoloipo}")
        self.btn_spin.config(state="disabled")
        
        for r in range(ROWS):
            for c in range(COLS):
                self.labels[r][c].config(bg="#1a1a1a", fg="white")

        self.animate(0, lines, bet)

    def animate(self, step, lines, bet):
        symbols = list(axia_symbolwn.keys())
        if step < 8:
            for r in range(ROWS):
                for c in range(COLS):
                    self.labels[r][c].config(text=random.choice(symbols), fg="#555")
            self.root.after(100, lambda: self.animate(step + 1, lines, bet))
        else:
            self.show_result(lines, bet)

    def show_result(self, lines_played, bet_per_line):
        pool = []
        for s, count in emfanisi_symbolwn.items():
            pool.extend([s] * count)
        
        res = []
        for _ in range(COLS):
            col = random.sample(pool, ROWS)
            res.append(col)

        for r in range(ROWS):
            for c in range(COLS):
                self.labels[r][c].config(text=res[c][r], fg="white")

        total_win = 0
        winning_lines = []
        
        for i in range(3):
            if i + 1 > lines_played:
                break
                
            symbol = res[0][i]
            match = True
            for c in range(COLS):
                if res[c][i] != symbol:
                    match = False
                    break
            
            if match:
                line_profit = axia_symbolwn[symbol] * bet_per_line
                total_win += line_profit
                winning_lines.append(i + 1)
                for c in range(COLS):
                    self.labels[i][c].config(bg="#27ae60")

        self.ypoloipo += total_win
        self.label_ypoloipo.config(text=f"BALANCE: ${self.ypoloipo}")
        
        if total_win > 0:
            self.status.config(text=f"💸 ΚΕΡΔΙΣΕΣ ${total_win}! (Γραμμές: {winning_lines})", fg="#2ecc71")
        else:
            self.status.config(text="Δεν έκατσε... Ξαναδοκίμασε!", fg="#ff4d4d")

        self.btn_spin.config(state="normal")

if __name__ == "__main__":
    app_root = tk.Tk()
    game = CasinoPro(app_root)
    app_root.mainloop()