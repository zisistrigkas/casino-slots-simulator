# Casino Slots Simulator

A Python-based slot machine simulation that demonstrates game logic, weighted probability distributions, and GUI development.

## 🎰 Features
- **Weighted Probabilities:** Uses a custom probability pool to define the rarity of different symbols (e.g., Diamonds are rarer than Cherries).
- **Game Engine:** Handles bets, lines, and payouts dynamically based on user input.
- **Interactive UI:** Built with `tkinter`, featuring status updates and balance management.

## ⚙️ How it Works
1. **Balance Management:** The system validates bets against the current balance.
2. **Animation Loop:** Uses a `root.after` loop to simulate spinning reels.
3. **Logic Engine:** Checks for matching symbols across selected lines and calculates total winnings.

## 🛠 Prerequisites
- Python 3.x
- `tkinter`

## 🚀 How to Run
1. Clone this repository: `git clone https://github.com/zisistrigkas/casino-slots-simulator.git`
2. Run the application:
   ```bash
   python betting_project.py
