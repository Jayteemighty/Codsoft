import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Colorful Rock-Paper-Scissors")
        self.master.configure(bg='#F0F0F0')

        # Score variables
        self.user_score = 0
        self.computer_score = 0

        # Choices
        self.choices = ["Rock", "Paper", "Scissors"]

        # Labels
        tk.Label(master, text="Choose Rock, Paper, or Scissors:", bg='#F0F0F0', font=('Arial', 12)).grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Buttons
        self.buttons = []
        for i, choice in enumerate(self.choices):
            button = tk.Button(master, text=choice, command=lambda ch=choice: self.play_game(ch), bg='#4CAF50', fg='white', font=('Arial', 12))
            button.grid(row=1, column=i, padx=5, pady=5, sticky="ew")
            self.buttons.append(button)

        # Score display
        self.score_label = tk.Label(master, text="User: 0   Computer: 0", bg='#F0F0F0', font=('Arial', 12))
        self.score_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    def play_game(self, user_choice):
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(user_choice, computer_choice)

        messagebox.showinfo("Result", f"User chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

        if result == "User wins!":
            self.user_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1

        self.update_score()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            return "User wins!"
        else:
            return "Computer wins!"

    def update_score(self):
        self.score_label.config(text=f"User: {self.user_score}   Computer: {self.computer_score}")

def main():
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
