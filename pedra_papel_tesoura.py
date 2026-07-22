"""
Create a Rock Paper Scissors game with a GUI using Tkinter.
The player clicks buttons for their choice and plays against a computer.
The game shows who won each round, tracks scores, and has a quit button.
"""
import random
import tkinter as tk
from tkinter import messagebox
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])
def determine_winner(player, computer):
    if player == computer:
        return 'tie'
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return 'player'
    else:
        return 'computer'
class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        self.root.configure(bg="#f0f0f0")  # Set background color
        self.player_points = 0
        self.computer_points = 0

        # Labels
        self.title_label = tk.Label(root, text="Rock, Paper, Scissors!", font=("Helvetica", 20, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        self.score_label = tk.Label(root, text=f"Score - You: {self.player_points} | Computer: {self.computer_points}", font=("Helvetica", 14), bg="#f0f0f0")
        self.score_label.pack(pady=10)

        self.computer_choice_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f0f0f0")
        self.computer_choice_label.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 16, "italic"), bg="#f0f0f0")
        self.result_label.pack(pady=20)

        # Buttons
        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.pack(pady=20)

        self.rock_button = tk.Button(self.button_frame, text="Rock", command=lambda: self.play('rock'), width=10, bg="#ffcccb", font=("Helvetica", 12))
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(self.button_frame, text="Paper", command=lambda: self.play('paper'), width=10, bg="#add8e6", font=("Helvetica", 12))
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", command=lambda: self.play('scissors'), width=10, bg="#90ee90", font=("Helvetica", 12))
        self.scissors_button.grid(row=0, column=2, padx=10)

        self.quit_button = tk.Button(root, text="Quit", command=self.quit_game, width=10, bg="#d3d3d3", font=("Helvetica", 12))
        self.quit_button.pack(pady=20)

    def play(self, player_choice):
        computer_choice = get_computer_choice()
        self.computer_choice_label.config(text=f"Computer chose: {computer_choice}")
        winner = determine_winner(player_choice, computer_choice)
        if winner == 'tie':
            result = "It's a tie!"
        elif winner == 'player':
            result = "You win!"
            self.player_points += 1
        else:
            result = "Computer wins!"
            self.computer_points += 1
        self.result_label.config(text=result)
        self.score_label.config(text=f"Score - You: {self.player_points} | Computer: {self.computer_points}")

    def quit_game(self):
        messagebox.showinfo("Game Over", f"Thanks for playing!\nFinal Score:\nYou: {self.player_points}\nComputer: {self.computer_points}")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()